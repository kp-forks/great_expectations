import logging
import pathlib
from dataclasses import dataclass
from typing import List

import pytest

import great_expectations.exceptions as ge_exceptions
from great_expectations.alias_types import PathStr
from great_expectations.experimental.datasources.interfaces import (
    BatchSortersDefinition,
)
from great_expectations.experimental.datasources.spark_datasource import (
    CSVSparkAsset,
    SparkDatasource,
)

logger = logging.getLogger(__name__)


@pytest.fixture
def spark_datasource(test_backends) -> SparkDatasource:
    if "SparkDFDataset" not in test_backends:
        pytest.skip("No spark backend selected.")

    return SparkDatasource(name="spark_datasource")


@pytest.fixture
def csv_path() -> pathlib.Path:
    relative_path = pathlib.Path(
        "..", "..", "test_sets", "taxi_yellow_tripdata_samples"
    )
    abs_csv_path = (
        pathlib.Path(__file__).parent.joinpath(relative_path).resolve(strict=True)
    )
    return abs_csv_path


@pytest.mark.unit
def test_construct_spark_datasource(spark_datasource: SparkDatasource):
    assert spark_datasource.name == "spark_datasource"


@pytest.mark.unit
def test_add_csv_asset_to_datasource(
    spark_datasource: SparkDatasource, csv_path: pathlib.Path
):
    asset = spark_datasource.add_csv_asset(
        name="csv_asset",
        base_directory=csv_path,
        regex=r"yellow_tripdata_sample_(\d{4})-(\d{2}).csv",
    )
    assert asset.name == "csv_asset"
    assert asset.base_directory == csv_path
    assert asset.regex.match("random string") is None
    assert asset.regex.match("yellow_tripdata_sample_11D1-22.csv") is None
    m1 = asset.regex.match("yellow_tripdata_sample_1111-22.csv")
    assert m1 is not None


@pytest.mark.unit
def test_construct_csv_asset_directly(csv_path: pathlib.Path):
    # noinspection PyTypeChecker
    asset = CSVSparkAsset(
        name="csv_asset",
        base_directory=csv_path,
        regex=r"yellow_tripdata_sample_(\d{4})-(\d{2}).csv",  # Ignoring IDE warning (type declarations are consistent).
    )
    assert asset.name == "csv_asset"
    assert asset.base_directory == csv_path
    assert asset.regex.match("random string") is None
    assert asset.regex.match("yellow_tripdata_sample_11D1-22.csv") is None
    m1 = asset.regex.match("yellow_tripdata_sample_1111-22.csv")
    assert m1 is not None


@pytest.mark.unit
def test_csv_asset_with_regex_unnamed_parameters(
    spark_datasource: SparkDatasource, csv_path: pathlib.Path
):
    asset = spark_datasource.add_csv_asset(
        name="csv_asset",
        base_directory=csv_path,
        regex=r"yellow_tripdata_sample_(\d{4})-(\d{2}).csv",
    )
    options = asset.batch_request_options_template()
    assert options == {"batch_request_param_1": None, "batch_request_param_2": None}


@pytest.mark.unit
def test_csv_asset_with_regex_named_parameters(
    spark_datasource: SparkDatasource, csv_path: pathlib.Path
):
    asset = spark_datasource.add_csv_asset(
        name="csv_asset",
        base_directory=csv_path,
        regex=r"yellow_tripdata_sample_(?P<year>\d{4})-(?P<month>\d{2}).csv",
    )
    options = asset.batch_request_options_template()
    assert options == {"year": None, "month": None}


@pytest.mark.unit
def test_csv_asset_with_some_regex_named_parameters(
    spark_datasource: SparkDatasource, csv_path: pathlib.Path
):
    asset = spark_datasource.add_csv_asset(
        name="csv_asset",
        base_directory=csv_path,
        regex=r"yellow_tripdata_sample_(\d{4})-(?P<month>\d{2}).csv",
    )
    options = asset.batch_request_options_template()
    assert options == {"batch_request_param_1": None, "month": None}


@pytest.mark.unit
def test_csv_asset_with_non_string_regex_named_parameters(
    spark_datasource: SparkDatasource, csv_path: pathlib.Path
):
    asset = spark_datasource.add_csv_asset(
        name="csv_asset",
        base_directory=csv_path,
        regex=r"yellow_tripdata_sample_(\d{4})-(?P<month>\d{2}).csv",
    )
    with pytest.raises(ge_exceptions.InvalidBatchRequestError):
        # year is an int which will raise an error
        asset.get_batch_request({"year": 2018, "month": "04"})


@pytest.mark.unit
@pytest.mark.xfail(reason="temp xfail for release 0.15.47")
def test_get_batch_list_from_fully_specified_batch_request(
    spark_datasource: SparkDatasource, csv_path: pathlib.Path
):
    asset = spark_datasource.add_csv_asset(
        name="csv_asset",
        base_directory=csv_path,
        regex=r"yellow_tripdata_sample_(?P<year>\d{4})-(?P<month>\d{2}).csv",
    )
    request = asset.get_batch_request({"year": "2018", "month": "04"})
    batches = asset.get_batch_list_from_batch_request(request)
    assert len(batches) == 1
    batch = batches[0]
    assert batch.batch_request.datasource_name == spark_datasource.name
    assert batch.batch_request.data_asset_name == asset.name
    assert batch.batch_request.options == {"year": "2018", "month": "04"}
    assert batch.metadata == {
        "year": "2018",
        "month": "04",
        "path": asset.base_directory / "yellow_tripdata_sample_2018-04.csv",
    }
    assert batch.id == "spark_datasource-csv_asset-year_2018-month_04"


@pytest.mark.unit
@pytest.mark.xfail(reason="temp xfail for release 0.15.47")
def test_get_batch_list_from_partially_specified_batch_request(
    spark_datasource: SparkDatasource, csv_path: pathlib.Path
):
    # Verify test directory has files that don't match what we will query for
    file_name: PathStr
    all_files: List[str] = [
        file_name.stem for file_name in list(pathlib.Path(csv_path).iterdir())
    ]
    # assert there are files that are not csv files
    assert any([not file_name.endswith("csv") for file_name in all_files])
    # assert there are 12 files from 2018
    files_for_2018 = [
        file_name for file_name in all_files if file_name.find("2018") >= 0
    ]
    assert len(files_for_2018) == 12

    asset = spark_datasource.add_csv_asset(
        name="csv_asset",
        base_directory=csv_path,
        regex=r"yellow_tripdata_sample_(?P<year>\d{4})-(?P<month>\d{2}).csv",
    )
    request = asset.get_batch_request({"year": "2018"})
    batches = asset.get_batch_list_from_batch_request(request)
    assert (len(batches)) == 12
    batch_filenames = [pathlib.Path(batch.metadata["path"]).stem for batch in batches]
    assert set(files_for_2018) == set(batch_filenames)

    @dataclass(frozen=True)
    class YearMonth:
        year: str
        month: str

    expected_year_month = {
        YearMonth(year="2018", month=format(m, "02d")) for m in range(1, 13)
    }
    batch_year_month = {
        YearMonth(year=batch.metadata["year"], month=batch.metadata["month"])
        for batch in batches
    }
    assert expected_year_month == batch_year_month


@pytest.mark.unit
@pytest.mark.parametrize(
    "order_by",
    [
        ["+year", "month"],
        ["+year", "+month"],
        ["+year", "-month"],
        ["year", "month"],
        ["year", "+month"],
        ["year", "-month"],
        ["-year", "month"],
        ["-year", "+month"],
        ["-year", "-month"],
        ["month", "+year"],
        ["+month", "+year"],
        ["-month", "+year"],
        ["month", "year"],
        ["+month", "year"],
        ["-month", "year"],
        ["month", "-year"],
        ["+month", "-year"],
        ["-month", "-year"],
    ],
)
def test_spark_sorter(
    spark_datasource: SparkDatasource,
    csv_path: pathlib.Path,
    order_by: BatchSortersDefinition,
):
    # Verify test directory has files we expect
    years = ["2018", "2019", "2020"]
    months = [format(m, "02d") for m in range(1, 13)]
    file_name: PathStr
    all_files: List[str] = [
        file_name.stem for file_name in list(pathlib.Path(csv_path).iterdir())
    ]
    # assert there are 12 files for each year
    for year in years:
        files_for_year = [
            file_name
            for file_name in all_files
            if file_name.find(f"yellow_tripdata_sample_{year}") == 0
        ]
        assert len(files_for_year) == 12

    asset = spark_datasource.add_csv_asset(
        name="csv_asset",
        base_directory=csv_path,
        regex=r"yellow_tripdata_sample_(?P<year>\d{4})-(?P<month>\d{2}).csv",
        order_by=order_by,
    )
    batches = asset.get_batch_list_from_batch_request(asset.get_batch_request())
    assert (len(batches)) == 36

    @dataclass(frozen=True)
    class TimeRange:
        key: str
        range: List[str]

    ordered_years = reversed(years) if "-year" in order_by else years
    ordered_months = reversed(months) if "-month" in order_by else months
    if "year" in order_by[0]:
        ordered = [
            TimeRange(key="year", range=ordered_years),
            TimeRange(key="month", range=ordered_months),
        ]
    else:
        ordered = [
            TimeRange(key="month", range=ordered_months),
            TimeRange(key="year", range=ordered_years),
        ]

    batch_index = -1
    for range1 in ordered[0].range:
        key1 = ordered[0].key
        for range2 in ordered[1].range:
            key2 = ordered[1].key
            batch_index += 1
            metadata = batches[batch_index].metadata
            assert metadata[key1] == range1
            assert metadata[key2] == range2

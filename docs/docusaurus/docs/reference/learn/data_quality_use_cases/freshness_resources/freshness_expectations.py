"""
To run this test locally, use the postgresql database docker container.

1. From the repo root dir, run:
cd assets/docker/postgresql
docker compose up

2. Run the following command from the repo root dir in a second terminal:
pytest --postgresql --docs-tests -k "data_quality_use_case_freshness_expectations" tests/integration/test_script_runner.py
"""

# This section loads sample data to use for CI testing of the script.
import pathlib

import great_expectations as gx
import great_expectations.expectations as gxe
from tests.test_utils import load_data_into_test_database

CONNECTION_STRING = "postgresql+psycopg2://postgres:@localhost/test_ci"

GX_ROOT_DIR = pathlib.Path(gx.__file__).parent.parent

# Add test data to database for testing.
load_data_into_test_database(
    table_name="freshness_sensor_readings",
    csv_path=str(
        GX_ROOT_DIR
        / "tests/test_sets/learn_data_quality_use_cases/freshness_sensor_readings.csv"
    ),
    connection_string=CONNECTION_STRING,
)

context = gx.get_context()

datasource = context.data_sources.add_postgres(
    "postgres database", connection_string=CONNECTION_STRING
)

data_asset = datasource.add_table_asset(
    name="sensor readings", table_name="freshness_sensor_readings"
)
batch_definition = data_asset.add_batch_definition_whole_table("batch definition")
batch = batch_definition.get_batch()

suite = context.suites.add(gx.ExpectationSuite(name="example freshness expectations"))

#############################
# Start Expectation snippets.

suite.add_expectation(
    # <snippet name="docs/docusaurus/docs/reference/learn/data_quality_use_cases/freshness_resources/freshness_expectations.py ExpectColumnMaxToBeBetween">
    gxe.ExpectColumnMaxToBeBetween(
        column="reading_ts",
        min_value="2024-11-22 14:42:00",
    )
    # </snippet>
)

suite.add_expectation(
    # <snippet name="docs/docusaurus/docs/reference/learn/data_quality_use_cases/freshness_resources/freshness_expectations.py ExpectColumnMinToBeBetween">
    gxe.ExpectColumnMinToBeBetween(
        column="reading_ts",
        min_value="2024-11-22 00:00:00",
    )
    # </snippet>
)

results = batch.validate(suite)

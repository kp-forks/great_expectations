from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar, Dict, List, Optional, Set

import numpy as np

from great_expectations.compatibility.typing_extensions import override
from great_expectations.core.domain import Domain  # noqa: TCH001 # FIXME CoP
from great_expectations.experimental.rule_based_profiler.config import ParameterBuilderConfig
from great_expectations.experimental.rule_based_profiler.helpers.util import (
    NP_EPSILON,
    get_parameter_value_and_validate_return_type,
)
from great_expectations.experimental.rule_based_profiler.parameter_builder import (
    MetricSingleBatchParameterBuilder,
)
from great_expectations.experimental.rule_based_profiler.parameter_container import (
    DOMAIN_KWARGS_PARAMETER_FULLY_QUALIFIED_NAME,
    FULLY_QUALIFIED_PARAMETER_NAME_METADATA_KEY,
    FULLY_QUALIFIED_PARAMETER_NAME_VALUE_KEY,
    RAW_PARAMETER_KEY,
    ParameterContainer,
    ParameterNode,
)
from great_expectations.types.attributes import Attributes

if TYPE_CHECKING:
    from great_expectations.data_context.data_context.abstract_data_context import (
        AbstractDataContext,
    )


class ValueCountsSingleBatchParameterBuilder(MetricSingleBatchParameterBuilder):
    """
    Compute value counts using specified metric for one Batch of data.
    """

    exclude_field_names: ClassVar[Set[str]] = (
        MetricSingleBatchParameterBuilder.exclude_field_names
        | {
            "column_value_counts_metric_single_batch_parameter_builder_config",
            "column_values_nonnull_count_metric_single_batch_parameter_builder_config",
            "metric_name",
            "metric_domain_kwargs",
            "metric_value_kwargs",
            "enforce_numeric_metric",
            "replace_nan_with_zero",
            "reduce_scalar_metric",
        }
    )

    def __init__(
        self,
        name: str,
        suite_parameter_builder_configs: Optional[List[ParameterBuilderConfig]] = None,
        data_context: Optional[AbstractDataContext] = None,
    ) -> None:
        """
        Args:
            name: the name of this parameter -- this is user-specified parameter name (from configuration);
            it is not the fully-qualified parameter name; a fully-qualified parameter name must start with "$parameter."
            and may contain one or more subsequent parts (e.g., "$parameter.<my_param_from_config>.<metric_name>").
            suite_parameter_builder_configs: ParameterBuilder configurations, executing and making whose respective
            ParameterBuilder objects' outputs available (as fully-qualified parameter names) is pre-requisite.
            These "ParameterBuilder" configurations help build parameters needed for this "ParameterBuilder".
            data_context: AbstractDataContext associated with this ParameterBuilder
        """  # noqa: E501 # FIXME CoP
        self._column_value_counts_metric_single_batch_parameter_builder_config = (
            ParameterBuilderConfig(
                module_name="great_expectations.rule_based_profiler.parameter_builder",
                class_name="MetricSingleBatchParameterBuilder",
                name="column_value_counts_metric_single_batch_parameter_builder",
                metric_name="column.value_counts",
                metric_domain_kwargs=DOMAIN_KWARGS_PARAMETER_FULLY_QUALIFIED_NAME,
                metric_value_kwargs={
                    "sort": "value",
                },
                enforce_numeric_metric=False,
                replace_nan_with_zero=False,
                reduce_scalar_metric=False,
                suite_parameter_builder_configs=None,
            )
        )
        self._column_values_nonnull_count_metric_single_batch_parameter_builder_config = (
            ParameterBuilderConfig(
                module_name="great_expectations.rule_based_profiler.parameter_builder",
                class_name="MetricSingleBatchParameterBuilder",
                name="column_values_nonnull_count_metric_single_batch_parameter_builder",
                metric_name="column_values.nonnull.count",
                metric_domain_kwargs=DOMAIN_KWARGS_PARAMETER_FULLY_QUALIFIED_NAME,
                metric_value_kwargs=None,
                enforce_numeric_metric=False,
                replace_nan_with_zero=False,
                reduce_scalar_metric=False,
                suite_parameter_builder_configs=None,
            )
        )

        if suite_parameter_builder_configs is None:
            suite_parameter_builder_configs = [
                self._column_value_counts_metric_single_batch_parameter_builder_config,
                self._column_values_nonnull_count_metric_single_batch_parameter_builder_config,
            ]

        super().__init__(
            name=name,
            metric_name=None,
            metric_domain_kwargs=DOMAIN_KWARGS_PARAMETER_FULLY_QUALIFIED_NAME,
            metric_value_kwargs=None,
            enforce_numeric_metric=False,
            replace_nan_with_zero=False,
            reduce_scalar_metric=False,
            suite_parameter_builder_configs=suite_parameter_builder_configs,
            data_context=data_context,
        )

    @override
    def _build_parameters(
        self,
        domain: Domain,
        variables: Optional[ParameterContainer] = None,
        parameters: Optional[Dict[str, ParameterContainer]] = None,
        runtime_configuration: Optional[dict] = None,
    ) -> Attributes:
        """
        Builds ParameterContainer object that holds ParameterNode objects with attribute name-value pairs and details.

        Returns:
            Attributes object, containing computed parameter values and parameter computation details metadata.
        """  # noqa: E501 # FIXME CoP
        fully_qualified_column_values_nonnull_count_metric_parameter_builder_name: str = f"{RAW_PARAMETER_KEY}{self._column_values_nonnull_count_metric_single_batch_parameter_builder_config.name}"  # noqa: E501 # FIXME CoP
        # Obtain "column_values.nonnull.count" from "rule state" (i.e., variables and parameters); from instance variable otherwise.  # noqa: E501 # FIXME CoP
        column_values_nonnull_count_parameter_node: ParameterNode = get_parameter_value_and_validate_return_type(  # noqa: E501 # FIXME CoP
            domain=domain,
            parameter_reference=fully_qualified_column_values_nonnull_count_metric_parameter_builder_name,
            expected_return_type=None,
            variables=variables,
            parameters=parameters,
        )

        fully_qualified_column_value_counts_metric_single_batch_parameter_builder_name: str = f"{RAW_PARAMETER_KEY}{self._column_value_counts_metric_single_batch_parameter_builder_config.name}"  # noqa: E501 # FIXME CoP
        # Obtain "column.value_counts" from "rule state" (i.e., variables and parameters); from instance variable otherwise.  # noqa: E501 # FIXME CoP
        column_value_counts_parameter_node: ParameterNode = get_parameter_value_and_validate_return_type(  # noqa: E501 # FIXME CoP
            domain=domain,
            parameter_reference=fully_qualified_column_value_counts_metric_single_batch_parameter_builder_name,
            expected_return_type=None,
            variables=variables,
            parameters=parameters,
        )

        values: list = list(
            column_value_counts_parameter_node[FULLY_QUALIFIED_PARAMETER_NAME_VALUE_KEY].index
        )
        weights: np.ndarray = np.asarray(
            column_value_counts_parameter_node[FULLY_QUALIFIED_PARAMETER_NAME_VALUE_KEY]
        ) / (
            column_values_nonnull_count_parameter_node[FULLY_QUALIFIED_PARAMETER_NAME_VALUE_KEY]
            + NP_EPSILON
        )

        partition_object: dict = {
            "values": values,
            "weights": weights.tolist(),
        }
        details: dict = column_value_counts_parameter_node[
            FULLY_QUALIFIED_PARAMETER_NAME_METADATA_KEY
        ]

        return Attributes(
            {
                FULLY_QUALIFIED_PARAMETER_NAME_VALUE_KEY: partition_object,
                FULLY_QUALIFIED_PARAMETER_NAME_METADATA_KEY: details,
            }
        )

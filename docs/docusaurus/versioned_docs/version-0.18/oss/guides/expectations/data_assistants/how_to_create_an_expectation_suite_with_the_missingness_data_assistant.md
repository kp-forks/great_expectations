---
title: Create an Expectation Suite with the Missingness Data Assistant
---

import Prerequisites from '../../../../components/_prerequisites.jsx'
import TechnicalTag from '../../../../reference/learn/term_tags/_tag.mdx';

:::caution Caution

Missingness Data Assistant functionality is [Experimental](/oss/contributing/contributing_maturity.md).

:::

Use the information provided here to learn how you can use the Missingness Data Assistant to profile your data and automate the creation of an Expectation Suite.

All the code used in the examples is available in GitHub at this location: [how_to_create_an_expectation_suite_with_the_missingness_data_assistant.py](https://github.com/great-expectations/great_expectations/blob/develop/docs/docusaurus/docs/oss/guides/expectations/data_assistants/how_to_create_an_expectation_suite_with_the_missingness_data_assistant.py).

## Prerequisites

<Prerequisites>

- A [configured Data Context](/oss/guides/setup/configuring_data_contexts/instantiating_data_contexts/instantiate_data_context.md).
- An understanding of how to [configure a Data Source](../../connecting_to_your_data/connect_to_data_lp.md).
- An understanding of how to [configure a Batch Request](/oss/guides/connecting_to_your_data/fluent/batch_requests/how_to_request_data_from_a_data_asset.md).

</Prerequisites>

## Prepare your Data Source and Validator

In the following examples, you'll be using existing New York taxi trip data to create a Validator.

This is the `Data Source` configuration:
 
```python title="Python" name="docs/docusaurus/docs/oss/guides/expectations/data_assistants/how_to_create_an_expectation_suite_with_the_missingness_data_assistant.py datasource_config"
```

This is the `Validator` configuration:

```python title="Python" name="docs/docusaurus/docs/oss/guides/expectations/data_assistants/how_to_create_an_expectation_suite_with_the_missingness_data_assistant.py validator"
```

:::caution Caution
The Missingness Data Assistant runs multiple queries against your `Data Source`. Data Assistant performance can vary significantly depending on the number of Batches, the number of records per Batch, and network latency. If Data Assistant runtimes are too long, use a subset of your data when defining your `Data Source` and `Validator`.
:::

## Run the Missingness Data Assistant

To run a Data Assistant, you can call the `run(...)` method for the assistant. There are numerous parameters available for the `run(...)` method of the Missingness Data Assistant. For instance, the `exclude_column_names` parameter allows you to define the columns that should not be Profiled.

1. Run the following code to define the columns to exclude:

  ```python title="Python" name="docs/docusaurus/docs/oss/guides/expectations/data_assistants/how_to_create_an_expectation_suite_with_the_missingness_data_assistant.py exclude_column_names"
  ```

2. Run the following code to run the Missingness Data Assistant:

  ```python title="Python" name="docs/docusaurus/docs/oss/guides/expectations/data_assistants/how_to_create_an_expectation_suite_with_the_missingness_data_assistant.py data_assistant_result"
  ```

  In this example, `context` is your Data Context instance.

  :::note Note
  The example code uses the default `estimation` parameter (`"exact"`).

  If you consider your data to be valid, and want to produce Expectations with ranges that are identical to the data in the `Validator`, you don't need to alter the example code. 
  
  To identify potential outliers in your `BatchRequest` data, pass `estimation="flag_outliers"` to the `run(...)` method.
  :::

  :::note Note
  The Missingness Data Assistant `run(...)` method can accept other parameters in addition to `exclude_column_names` such as `include_column_names`, `include_column_name_suffixes`, and `cardinality_limit_mode`. To view the available parameters, see [this information](https://github.com/great-expectations/great_expectations/blob/develop/great_expectations/rule_based_profiler/data_assistant/column_value_missing_data_assistant.py#L44).
  :::

## Save your Expectation Suite

After executing the Missingness Data Assistant's `run(...)` method and generating Expectations for your data, run the following code to generate an Expectation Suite and save it to your Validator:

  ```python title="Python" name="docs/docusaurus/docs/oss/guides/expectations/data_assistants/how_to_create_an_expectation_suite_with_the_missingness_data_assistant.py save_validator"
  ```
## Test your Expectation Suite

Run the following code to use a Checkpoint to operate with the Expectation Suite and Validator that you defined:

  ```python title="Python" name="docs/docusaurus/docs/oss/guides/expectations/data_assistants/how_to_create_an_expectation_suite_with_the_missingness_data_assistant.py checkpoint"
  ```

You can check the `"success"` key of the Checkpoint's results to verify that your Expectation Suite worked.

## Plot and inspect Metrics and Expectations

1. Run the following code to view Batch-level visualizations of the Metrics computed by the Missingness Data Assistant:

  ```python title="Python" name="docs/docusaurus/docs/oss/guides/expectations/data_assistants/how_to_create_an_expectation_suite_with_the_missingness_data_assistant.py plot_metrics"
  ```

  ![Plot Metrics](/docs/oss/images/data_assistant_plot_metrics.png)

  :::note Note
  Hover over a data point to view more information about the Batch and its calculated Metric value.
  :::

2. Run the following command to view the Expectations produced and grouped by Expectation type:

  ```python title="Python" name="docs/docusaurus/docs/oss/guides/expectations/data_assistants/how_to_create_an_expectation_suite_with_the_missingness_data_assistant.py show_expectations_by_expectation_type"
  ```

## Edit your Expectation Suite (Optional)

The Missingness Data Assistant creates as many Expectations as it can for the permitted columns. Although this can help with data analysis, it might be unnecessary.  You might have some domain knowledge that is not reflected in the data that was sampled for the Profiling process. In these types of scenarios, you can edit your Expectation Suite to better align with your business requirements.

To edit your new Expectation Suite, see [Edit an existing Expectation Suite](/oss/guides/expectations/how_to_edit_an_existing_expectationsuite.md).
---
title: Validate multiple Batches from a Batch Request with a single Checkpoint
---

import Prerequisites from '../../../../components/_prerequisites.jsx';



By default, a Checkpoint only validates the last Batch included in a Batch Request. Use the information provided here to learn how you can use a Python loop and the Checkpoint `validations` parameter to validate multiple Batches identified by a single Batch Request. 

## Prerequisites

<Prerequisites>

- [A configured Data Context](/oss/guides/setup/configuring_data_contexts/instantiating_data_contexts/instantiate_data_context.md).
- [A Data Asset with multiple Batches](/oss/guides/connecting_to_your_data/connect_to_data_lp.md).
- [An Expectation Suite](/oss/guides/expectations/expectations_lp.md). 

</Prerequisites>

## Create a Batch Request with multiple Batches

The following Python code creates a Batch Request that includes every available Batch in a Data Asset named `asset`:

```python title="Python" name="docs/docusaurus/docs/oss/guides/validation/checkpoints/how_to_validate_multiple_batches_within_single_checkpoint.py build_a_batch_request_with_multiple_batches"
```

:::tip Tip
A Batch Request can only retrieve multiple Batches from a Data Asset that has been configured to include more than the default single Batch.

When working with a Filesystem Data Source and organizing Batches, the `batching_regex` argument determines the inclusion of multiple Batches into a single Data Asset, with each file that matches the `batching_regex` resulting in a single Batch.

SQL Data Assets include a single Batch by default. You can use splitters to split the single Batch into multiple Batches.

For more information on partitioning a Data Asset into Batches, see [Manage Data Assets](/oss/guides/connecting_to_your_data/manage_data_assets_lp.md).
:::

## Get a list of Batches from the Batch Request

Use the same Data Asset that your Batch Request was built from to retrieve a list of Batches with the following code:

```python title="Python" name="docs/docusaurus/docs/oss/guides/validation/checkpoints/how_to_validate_multiple_batches_within_single_checkpoint.py batch_list"
```

## Convert the list of Batches into a list of Batch Requests

A Checkpoint validates Batch Requests, but only validates the last Batch found in a Batch Request. You'll need to convert the list of Batches into a list of Batch Requests that return the corresponding individual Batch.

```python title="Python" name="docs/docusaurus/docs/oss/guides/validation/checkpoints/how_to_validate_multiple_batches_within_single_checkpoint.py batch_request_list"
```

## Build a validations list 

A Checkpoint class's `validations` parameter consists of a list of dictionaries.  Each dictionary pairs one Batch Request with the Expectation Suite it should be validated against.  The following code creates a valid `validations` list and associates each Batch Request with an Expectation Suite named `example_suite`.

```python title="Python" name="docs/docusaurus/docs/oss/guides/validation/checkpoints/how_to_validate_multiple_batches_within_single_checkpoint.py add_validations"
```

## Run Checkpoint

The `validations` list, containing the pairings of Batch Requests and Expectation Suites, can now be passed to a single Checkpoint instance which validates each Batch Request against its corresponding Expectation Suite. This effectively validates each Batch included in the original multiple-Batch Batch Request.

```python title="Python" name="docs/docusaurus/docs/oss/guides/validation/checkpoints/how_to_validate_multiple_batches_within_single_checkpoint.py add_checkpoint"
```

## Review the Validation Results

After the validations run, use the following code to build and view the Validation Results as Data Docs.

```python title="Python" name="docs/docusaurus/docs/oss/guides/validation/checkpoints/how_to_validate_multiple_batches_within_single_checkpoint.py review data_docs"
```
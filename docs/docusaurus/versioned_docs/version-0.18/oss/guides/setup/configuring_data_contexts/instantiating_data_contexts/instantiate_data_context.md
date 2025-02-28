---
sidebar_label: "Instantiate a Data Context"
title: "Instantiate a Data Context"
id: instantiate_data_context
description: Create and configure a Great Expectations Data Context.
hide_table_of_contents: true
---

import TechnicalTag from '../../../../../reference/learn/term_tags/_tag.mdx';
import Prerequisites from '../../../../../components/_prerequisites.jsx'
import GxImport from '../../../../../components/setup/python_environment/_gx_import.md'
import DataContextVerifyContents from '../../../../../components/setup/data_context/_data_context_verify_contents.md'
import AdmonitionConvertToFileContext from '../../../../../components/setup/data_context/_admonition_convert_to_file_context.md'
import ConnectingToDataFluently from '../../../../../components/connect_to_data/link_lists/_connecting_to_data_fluently.md';
import TabItem from '@theme/TabItem';
import Tabs from '@theme/Tabs';


A <TechnicalTag tag="data_context" text="Data Context" /> contains the configurations for <TechnicalTag tag="expectation" text="Expectations" />, <TechnicalTag tag="store" text="Metadata Stores" />, <TechnicalTag tag="data_docs" text="Data Docs" />, <TechnicalTag tag="checkpoint" text="Checkpoints" />, and all things related to working with Great Expectations (GX).  Use the information provided here to instantiate a Data Context so that you can continue working with previously defined GX configurations.

<Tabs
  groupId="install-gx"
  defaultValue='quick'
  values={[
  {label: 'Existing Filesystem', value:'quick'},
  {label: 'Filesystem with Python', value:'python'},
  {label: 'Specific Filesystem', value:'specific'},
  {label: 'Ephemeral', value:'ephemeral'},
  ]}>
<TabItem value="quick">

## Existing Filesystem

Instantiate an existing Filesystem Data Context so that you can continue working with previously defined GX configurations.

### Prerequisites

<Prerequisites requirePython = {false} requireInstallation = {true} requireDataContext = {false} requireSourceData = {null} requireDatasource = {false} requireExpectationSuite = {false}>

</Prerequisites>

### Import GX

<GxImport />

### Run the `get_context(...)` method

To quickly acquire a Data Context, use the `get_context(...)` method without any defined parameters:

```python title="Python code"
context = gx.get_context()
```

This functions as a convenience method for initializing, instantiating, and returning a Data Context.  In the absence of parameters defining its behavior, calling `get_context()` returns a Cloud Data Context, a Filesystem Data Context, or an Ephemeral Data Context depending on what type of Data Context has previously been initialized with your GX install.

If you have GX Cloud configured on your system, `get_context()` instantiates and returns a Cloud Data Context. Otherwise, `get_context()`  instantiates and returns the last accessed Filesystem Data Context. If a previously initialized Filesystem Data Context cannot be found, `get_context()` initializes, instantiates, and returns a temporary in-memory Ephemeral Data Context.


:::info Saving the contents of an Ephemeral Data Context for future use

<AdmonitionConvertToFileContext />

:::

### Verify Data Context content 

<DataContextVerifyContents />

</TabItem>
<TabItem value="python">

## Python

A <TechnicalTag tag="data_context" text="Data Context" /> is required in almost all Python scripts utilizing GX. Use Python code to initialize, instantiate, and verify the contents of a Filesystem Data Context.

### Prerequisites

<Prerequisites requirePython = {false} requireInstallation = {true} requireDataContext = {false} requireSourceData = {null} requireDatasource = {false} requireExpectationSuite = {false}>

</Prerequisites>

### Import GX

<GxImport />

### Determine the folder to initialize the Data Context in

Run the following command to initialize your Filesystem Data Context in an empty folder:

```python title="Python" name="docs/docusaurus/docs/oss/guides/setup/configuring_data_contexts/instantiating_data_contexts/how_to_initialize_a_filesystem_data_context_in_python.py path_to_empty_folder"
```

### Create a context

You provide the path for your empty folder to the GX library's `FileDataContext.create(...)` method as the `project_root_dir` parameter.  Because you are providing a path to an empty folder, `FileDataContext.create(...)` initializes a Filesystem Data Context in that location.

For convenience, the `FileDataContext.create(...)` method instantiates and returns the newly initialized Data Context, which you can keep in a Python variable.

```python title="Python" name="docs/docusaurus/docs/oss/guides/setup/configuring_data_contexts/instantiating_data_contexts/how_to_initialize_a_filesystem_data_context_in_python.py initialize_filesystem_data_context"
```

:::info What if the folder is not empty?
If the `project_root_dir` provided to the `FileDataContext.create(...)` method points to a folder that does not already have a Data Context present, the `FileDataContext.create(...)` method initializes a Filesystem Data Context in that location even if other files and folders are present.  This allows you to initialize a Filesystem Data Context in a folder that contains your Data Assets or other project related contents.

If a Data Context already exists in `project_root_dir`, the `FileDataContext.create(...)` method will not re-initialize it.  Instead, `FileDataContext.create(...)` instantiates and returns the existing Data Context.
:::

### Verify the Data Context content 

<DataContextVerifyContents />

</TabItem>
<TabItem value="specific">

## Specific

If you're using GX for multiple projects, you might want to use a different Data Context for each project. Instantiate a specific Filesystem Data Context so that you can switch between sets of previously defined GX configurations.

### Prerequisites

<Prerequisites requirePython = {false} requireInstallation = {true} requireDataContext = {false} requireSourceData = {null} requireDatasource = {false} requireExpectationSuite = {false}>

- A previously initialized Filesystem Data Context.

</Prerequisites>

### Import GX

<GxImport />

### Specify a folder containing a previously initialized Filesystem Data Context

Each Filesystem Data Context has a root folder in which it was initialized.  This root folder identifies the specific Filesystem Data Context to instantiate.

```python title="Python" name="docs/docusaurus/docs/oss/guides/setup/configuring_data_contexts/instantiating_data_contexts/how_to_instantiate_a_specific_filesystem_data_context.py path_to_project_root"
```

### Run the `get_context(...)` method

You provide the path for your empty folder to the GX library's `get_context(...)` method as the `project_root_dir` parameter. Because you are providing a path to an empty folder, the `get_context(...)` method instantiates and return the Data Context at that location.

```python title="Python" name="docs/docusaurus/docs/oss/guides/setup/configuring_data_contexts/instantiating_data_contexts/how_to_instantiate_a_specific_filesystem_data_context.py get_filesystem_data_context"
```

:::info Project root vs context root
Note that there is a subtle distinction between the `project_root_dir` and `context_root_dir` arguments accepted by `get_context(...)`.

Your context root is the directory that contains all your GX config while your project root refers to your actual working directory (and therefore contains the context root).

```bash
# The overall directory is your project root
data/
gx/ # The GX folder with your config is your context root
  great_expectations.yml
  ...
...
```

Both are functionally equivalent for purposes of working with a file-backed project. 
:::

:::info What if the folder does not contain a Data Context?
If the root directory provided to the `get_context(...)` method points to a folder that does not already have a Data Context, the `get_context(...)` method initializes a new Filesystem Data Context in that location.

The `get_context(...)` method instantiates and returns the newly initialized Data Context.
:::

### Verify the Data Context content 

<DataContextVerifyContents />

</TabItem>
<TabItem value="ephemeral">

## Ephemeral

An Ephemeral Data Context is a temporary, in-memory Data Context.  They are ideal for doing data exploration and initial analysis when you do not want to save anything to an existing project, or for when you need to work in a hosted environment such as an EMR Spark Cluster.

An Ephemeral Data Context does not persist beyond the current Python session. To keep the contents of your Ephemeral Data Context for future use, see [How to convert an Ephemeral Data Context to a Filesystem Data Context](/oss/guides/setup/configuring_data_contexts/how_to_convert_an_ephemeral_data_context_to_a_filesystem_data_context.md).

### Prerequisites

<Prerequisites>

- A Great Expectations instance. See [Setup: Overview](../../setup_overview.md).

</Prerequisites> 

### Import classes

To create your Data Context, you'll create a configuration that uses in-memory Metadata Stores. 

1. Run the following command to import the `DataContextConfig` and the `InMemoryStoreBackendDefaults` classes:

    ```python title="Python" name="docs/docusaurus/docs/snippets/how_to_explicitly_instantiate_an_ephemeral_data_context.py import_data_context_config_with_in_memory_store_backend"
    ```

2. Run the following command to import the `EphemeralDataContext` class:

    ```python title="Python" name="docs/docusaurus/docs/snippets/how_to_explicitly_instantiate_an_ephemeral_data_context.py import_ephemeral_data_context"
    ```

### Create the Data Context configuration

Run the following command to create a Data Context configuration that specifies the use of in-memory Metadata Stores and pass in an instance of the `InMemoryStoreBackendDefaults` class as a parameter when initializing an instance of the `DataContextConfig` class:

```python title="Python" name="docs/docusaurus/docs/snippets/how_to_explicitly_instantiate_an_ephemeral_data_context.py instantiate_data_context_config_with_in_memory_store_backend"
```

### Instantiate an Ephemeral Data Context

Run the following command to initialize the `EphemeralDataContext` class while passing in the `DataContextConfig` instance you created as the value of the `project_config` parameter.

```python title="Python" name="docs/docusaurus/docs/snippets/how_to_explicitly_instantiate_an_ephemeral_data_context.py instantiate_ephemeral_data_context"
```

:::info Saving the contents of an Ephemeral Data Context for future use

<AdmonitionConvertToFileContext />

:::

### Connect to a Data Source

Now that you have an Ephemeral Data Context you can connect GX to your Data Source. See the following topics:

<ConnectingToDataFluently />

</TabItem>
</Tabs>

## Next steps

- [Customize the Data Context configuration for Metadata Stores](/oss/guides/setup/setup_overview_lp.md#install-and-configure)
- [Customize the Data Context configuration for hosting and sharing Data Docs](/oss/guides/setup/configuring_data_docs/host_and_share_data_docs.md)
- [Connect GX to a Data Source](/oss/guides/connecting_to_your_data/connect_to_data_lp.md)



---
sidebar_label: "Install GX with Data Source dependencies"
title: "Install Great Expectations with Data Source dependencies"
id: install_gx
description: Install Great Expectations locally, or in a hosted environment.
hide_table_of_contents: true
---

import Preface from './components_local/_preface.mdx'
import CheckPythonVersion from './components_local/_check_python_version.mdx'
import ChooseInstallationMethod from './components_local/_choose_installation_method.mdx'
import InstallGreatExpectations from './components_local/_install_great_expectations.mdx'
import VerifyGeInstallSucceeded from './components_local/_verify_ge_install_succeeded.mdx'
import TechnicalTag from '../../../../reference/learn/term_tags/_tag.mdx';
import Prerequisites from '../../../../components/_prerequisites.jsx'
import PrereqInstalledAwsCli from '../../../../components/prerequisites/_aws_installed_the_aws_cli.mdx'
import PrereqAwsConfiguredCredentials from '../../../../components/prerequisites/_aws_configured_your_credentials.mdx'
import AwsVerifyInstallation from '../../../../components/setup/dependencies/_aws_verify_installation.md'
import AwsVerifyCredentialsConfiguration from '../../../../components/setup/dependencies/_aws_verify_installation.md'
import PythonCheckVersion from '../../../../components/setup/python_environment/_python_check_version.mdx'
import PythonCreateVenv from '../../../../components/setup/python_environment/_python_create_venv.md'
import TipPythonOrPython3Executable from '../../../../components/setup/python_environment/_tip_python_or_python3_executable.md'
import S3InstallDependencies from '../../../../components/setup/dependencies/_s3_install_dependencies.md'
import GxVerifyInstallation from '../../../../components/setup/_gx_verify_installation.md'
import LinksAfterInstallingGx from '../../../../components/setup/next_steps/_links_after_installing_gx.md'
import PrereqGcpServiceAccount from '../../../../components/prerequisites/_gcp_service_account.md'
import GcpVerifyCredentials from '../../../../components/setup/dependencies/_gcp_verify_credentials_configuration.md'
import GcpInstallDependencies from '../../../../components/setup/dependencies/_gcp_install_dependencies.md'
import PrereqAbsConfiguredAnAbsAccount from '../../../../components/prerequisites/_abs_configured_an_azure_storage_account_and_kept_connection_string.md'
import AbsInstallDependencies from '../../../../components/setup/dependencies/_abs_install_dependencies.md'
import AbsConfigureCredentialsInDataContext from '../../../../components/setup/dependencies/_abs_configure_credentials_in_data_context.md'
import AbsFurtherConfiguration from '../../../../components/setup/next_steps/_links_for_adding_azure_blob_storage_configurations_to_data_context.md'
import InstallDependencies from '../../../../components/setup/dependencies/_sql_install_dependencies.mdx'
import TabItem from '@theme/TabItem';
import Tabs from '@theme/Tabs';


You can install Great Expectations (GX) locally, or in hosted environments such as Databricks, Amazon EMR, or Google Cloud Composer. Installing GX locally lets you test features and functionality to determine if it's suitable for your use case. 

:::info Windows Support

Windows support for the open source Python version of GX is currently unavailable. If you’re using GX in a Windows environment, you might experience errors or performance issues.

:::

<Tabs
  groupId="install-gx"
  defaultValue='local'
  values={[
  {label: 'Local', value:'local'},
  {label: 'Hosted', value:'hosted'},
  {label: 'Amazon S3', value:'amazon'},
  {label: 'Microsoft Azure Blob Storage', value:'azure'},
  {label: 'Google Cloud Storage', value:'gcs'},
  {label: 'SQL databases', value:'sql'},
  ]}>
  <TabItem value="local">

## Local

Install Great Expectations (GX) locally.

<Preface />

### Check Python version
<CheckPythonVersion />

### Choose installation method
<ChooseInstallationMethod />

### Install GX
<InstallGreatExpectations />

### Confirm GX installation
<VerifyGeInstallSucceeded />

</TabItem>

<TabItem value="hosted">

## Hosted

Great Expectations can be deployed in environments such as Databricks, Amazon EMR, or Google Cloud Composer. These environments do not always have a file system that allows a Great Expectations installation. To install Great Expectations in a hosted environment, see one of the following guides:

- [How to Use Great Expectations in Databricks](https://docs.greatexpectations.io/docs/oss/tutorials/getting_started/how_to_use_great_expectations_in_databricks/)
- [How to instantiate a Data Context on an EMR Spark cluster](https://docs.greatexpectations.io/docs/oss/deployment_patterns/how_to_instantiate_a_data_context_on_an_emr_spark_cluster)

</TabItem>

<TabItem value="amazon">

## Amazon S3

Create your GX Python environment, install Great Expectations locally, and then configure the necessary dependencies to access data stored on Amazon S3.

### Prerequisites

<Prerequisites requirePython = {true} requireInstallation = {false} requireDataContext = {false} requireSourceData = {null} requireDatasource = {false} requireExpectationSuite = {false}>

- The ability to install Python modules with pip
- <PrereqInstalledAwsCli />
- <PrereqAwsConfiguredCredentials />

</Prerequisites>

### Ensure your AWS CLI version is the most recent

<AwsVerifyInstallation />

### Ensure your AWS credentials are correctly configured

<AwsVerifyCredentialsConfiguration />

### Check your Python version

<PythonCheckVersion />

<TipPythonOrPython3Executable />

### Create a Python virtual environment

<PythonCreateVenv />

### Install GX with optional dependencies for S3

<S3InstallDependencies />

### Verify the GX has been installed correctly

<GxVerifyInstallation />

### Next steps

Now that you have installed GX with the necessary dependencies for working with S3, you are ready to initialize your <TechnicalTag tag="data_context" text="Data Context" />.  The Data Context will contain your configurations for GX components, as well as provide you with access to GX's Python API.

<LinksAfterInstallingGx />

</TabItem>
<TabItem value="azure">

## Microsoft Azure Blob Storage

Create your GX Python environment, install Great Expectations locally, and then configure the necessary dependencies to access data stored on Microsoft Azure Blob Storage.

### Prerequisites

<Prerequisites requirePython = {true} requireInstallation = {false} requireDataContext = {false} requireSourceData = {null} requireDatasource = {false} requireExpectationSuite = {false}>

- The ability to install Python modules with pip
- <PrereqAbsConfiguredAnAbsAccount />

</Prerequisites>

### Check your Python version

<PythonCheckVersion />

<TipPythonOrPython3Executable />

### Create a Python virtual environment

<PythonCreateVenv />

### Install GX with optional dependencies for Azure Blob Storage

<AbsInstallDependencies />

### Verify that GX has been installed correctly

<GxVerifyInstallation />

### Configure the `config_variables.yml` file with your Azure Storage credentials

<AbsConfigureCredentialsInDataContext />

### Next steps

<AbsFurtherConfiguration />

</TabItem>
<TabItem value="gcs">

## GCS

Create your GX Python environment, install Great Expectations locally, and then configure the necessary dependencies to access data stored on GCS.

### Prerequisites

<Prerequisites requirePython = {true} requireInstallation = {false} requireDataContext = {false} requireSourceData = {null} requireDatasource = {false} requireExpectationSuite = {false}>

- The ability to install Python modules with pip
- <PrereqGcpServiceAccount />

</Prerequisites>

### Ensure your GCP credentials are correctly configured

<GcpVerifyCredentials />

### Check your Python version

<PythonCheckVersion />

<TipPythonOrPython3Executable />

### Create a Python virtual environment

<PythonCreateVenv />

### Install optional dependencies

<GcpInstallDependencies />

### Verify that GX has been installed correctly

<GxVerifyInstallation />

### Next steps

Now that you have installed GX with the necessary dependencies for working with GCS, you are ready to initialize your <TechnicalTag tag="data_context" text="Data Context" />.  The Data Context will contain your configurations for GX components, as well as provide you with access to GX's Python API.

<LinksAfterInstallingGx />

</TabItem>
<TabItem value="sql">

## SQL databases

Create your GX Python environment, install Great Expectations locally, and then configure the necessary dependencies to access data stored on SQL databases.

### Prerequisites

<Prerequisites requirePython = {true} requireInstallation = {false} requireDataContext = {false} requireSourceData = {null} requireDatasource = {false} requireExpectationSuite = {false}>

- The ability to install Python modules with pip

</Prerequisites>

### Check your Python version

<PythonCheckVersion />

<TipPythonOrPython3Executable />

### Create a Python virtual environment

<PythonCreateVenv />

### Install GX with optional dependencies for SQL databases

<InstallDependencies install_key="sqlalchemy" database_name="SQL databases"/>

:::caution Additional dependencies for some SQL dialects

The above pip instruction will install GX with basic SQL support through SqlAlchemy.  However, certain SQL dialects require additional dependencies.  Depending on the SQL database type you will be working with, you may wish to use one of the following installation commands, instead:

- AWS Athena: `pip install 'great_expectations[athena]'`
- BigQuery: `pip install 'great_expectations[bigquery]'`
- MSSQL: `pip install 'great_expectations[mssql]'`
- PostgreSQL: `pip install 'great_expectations[postgresql]'`
- Redshift: `pip install 'great_expectations[redshift]'`
- Snowflake: `pip install 'great_expectations[snowflake]'`
- Trino: `pip install 'great_expectations[trino]'`

:::

### Verify that GX has been installed correctly

<GxVerifyInstallation />

### Set up credentials

Different SQL dialects have different requirements for connection strings and methods of configuring credentials.  By default, GX allows you to define credentials as environment variables or as values in your Data Context. See [Instantiate a Data Context](../configuring_data_contexts/instantiating_data_contexts/instantiate_data_context.md).

There may also be third party utilities for setting up credentials of a given SQL database type.  For more information on setting up credentials for a given source database, please reference the official documentation for that SQL dialect as well as our guide on [how to set up credentials](/oss/guides/setup/configuring_data_contexts/how_to_configure_credentials.md).

### Next steps

Now that you have installed GX with the necessary dependencies for working with SQL databases, you are ready to initialize your <TechnicalTag tag="data_context" text="Data Context" />.  The Data Context will contain your configurations for GX components, as well as provide you with access to GX's Python API.

<LinksAfterInstallingGx />

</TabItem>
</Tabs>

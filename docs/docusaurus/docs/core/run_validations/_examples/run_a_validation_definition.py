"""
This is an example script for how to run a Validation Definition.

To test, run:

"""


def set_up_context_for_example(context):
    # Create a Batch Definition
    batch_definition = (
        context.data_sources.add_pandas_filesystem(
            name="my_data_source", base_directory="./data/folder_with_data"
        )
        .add_csv_asset(name="my_data_asset")
        .add_batch_definition_yearly(
            name="my_batch_definition",
            regex=r"yellow_tripdata_sample_(?P<year>\d{4})-01.csv",
        )
    )

    # Create an Expectation Suite
    expectation_suite = context.suites.add(
        gx.ExpectationSuite(name="my_expectation_suite")
    )
    # Add some Expectations
    expectation_suite.add_expectation(
        gx.expectations.ExpectColumnValuesToNotBeNull(column="pickup_datetime")
    )
    expectation_suite.add_expectation(
        gx.expectations.ExpectColumnValuesToNotBeNull(column="passenger_count")
    )
    # Create a Validation Definition
    context.validation_definitions.add(
        gx.ValidationDefinition(
            data=batch_definition,
            suite=expectation_suite,
            name="my_validation_definition",
        )
    )


df = "fake_data_frame"

# EXAMPLE SCRIPT STARTS HERE:
# <snippet name="docs/docusaurus/docs/core/run_validations/_examples/run_a_validation_definition.py - full code example">
import great_expectations as gx

context = gx.get_context()
# Hide this
set_up_context_for_example(context)

# Retrieve the Validation Definition
# <snippet name="docs/docusaurus/docs/core/run_validations/_examples/run_a_validation_definition.py - retrieve a Validation Definition">
validation_definition_name = "my_validation_definition"
validation_definition = context.validation_definitions.get(validation_definition_name)
# </snippet>

# Define Batch parameters
# Accepted keys are determined by the BatchDefinition used to instantiate this ValidationDefinition.
# <snippet name="docs/docusaurus/docs/core/run_validations/_examples/run_a_validation_definition.py - define batch parameters">
batch_parameters_dataframe = {"dataframe": df}
batch_parameters_daily = {"year": "2020", "month": "1", "day": "17"}
batch_parameters_yearly = {"year": "2019"}
# </snippet>

# Run the Validation Definition
# <snippet name="docs/docusaurus/docs/core/run_validations/_examples/run_a_validation_definition.py - run a Validation Definition">
validation_results = validation_definition.run(batch_parameters=batch_parameters_yearly)
# </snippet>

# Review the Validation Results
# <snippet name="docs/docusaurus/docs/core/run_validations/_examples/run_a_validation_definition.py - review Validation Results">
print(validation_results)
# </snippet>
# </snippet>


# TODO: Set up the example script to use a GX Cloud Data Context and then
# add this portion back in.
# # Get the URL for Validation Results in GX Cloud
# # <snippet name="docs/docusaurus/docs/core/run_validations/_examples/run_a_validation_definition.py - get GX Cloud Validation Result URL">
# print(validation_results.results_url)
# # </snippet>

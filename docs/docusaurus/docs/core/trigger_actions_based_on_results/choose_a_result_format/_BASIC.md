When the `result_format` is set to `"BASIC"` the Validation Results of each Expectation includes a `result` dictionary with information providing a basic explanation for why it failed or succeeded. The format is intended for quick feedback and it works well in Jupyter Notebooks.

You can check the [Validation Results reference tables](#validation-results-reference-tables) to see what information is provided in the `result` dictionary.

To create a `"BASIC"` result format configuration use the following code:

```python title="Python" name="docs/docusaurus/docs/core/trigger_actions_based_on_results/_examples/choose_result_format.py - basic Result Format"
```
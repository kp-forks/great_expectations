import TechnicalTag from '../../../../reference/learn/term_tags/_tag.mdx';

The Checkpoint contains `UpdateDataDocsAction` which renders the <TechnicalTag tag="data_docs" text="Data Docs"/> from the generated Validation Results. The Data Docs store contains a new entry for the rendered Validation Result.

:::tip Tip

For more information on Actions that Checkpoints can perform and how to add them, see [Configure Actions](/oss/guides/validation/validation_actions/actions_lp.md).

:::

Run the following code to view the new entry for the rendered Validation Result:

```python title="Python"
context.open_data_docs()
```
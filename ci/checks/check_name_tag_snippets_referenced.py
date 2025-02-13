"""
Purpose: To ensure that all named snippets are referenced in the docs.

Python code snippets refers to the Python module, containing the test, as follows:

```python name="tests/integration/docusaurus/general_directory/specific_directory/how_to_do_my_operation.py get_context"
```

whereby "tests/integration/docusaurus/general_directory/specific_directory/how_to_do_my_operation.py get_context", which
is the Python module, containing the integration test in the present example, would contain the following tagged code:

# Python
# <snippet name="tests/integration/docusaurus/general_directory/specific_directory/how_to_do_my_operation.py get_context">
import great_expectations as gx

context = gx.get_context()
# </snippet>

Find all named snippets and ensure that they are referenced in the docs using the above syntax.
"""  # noqa: E501

import pathlib
import shutil
import subprocess
import sys
from typing import List

UNREFERENCED_SNIPPETS: list[str] = [
    # Snippets can be added here if we want them but they are not yet referenced in docs.
    # We should work to keep this as empty as we can.
]


def check_dependencies(*deps: str) -> None:
    for dep in deps:
        if not shutil.which(dep):
            raise Exception(f"Must have `{dep}` installed in PATH to run {__file__}")  # noqa: TRY002, TRY003


def get_snippet_definitions(target_dir: pathlib.Path) -> List[str]:
    try:
        res_snippets = subprocess.run(  # noqa: PLW1510
            [
                "grep",
                "--recursive",
                "--binary-files=without-match",
                "--no-filename",
                "--ignore-case",
                "--word-regexp",
                "--regexp",
                r"^# <snippet .*name=.*>",
                str(target_dir),
            ],
            text=True,
            capture_output=True,
        )
        res_snippet_names = subprocess.run(  # noqa: PLW1510
            ["sed", 's/.*name="//; s/">//; s/version-[0-9\\.]* //'],
            text=True,
            input=res_snippets.stdout,
            capture_output=True,
        )
        return res_snippet_names.stdout.splitlines()
    except subprocess.CalledProcessError as e:
        raise RuntimeError(  # noqa: TRY003
            f"Command {e.cmd} returned with error (code {e.returncode}): {e.output}"
        ) from e


def get_snippets_used(target_dir: pathlib.Path) -> List[str]:
    try:
        res_snippet_usages = subprocess.run(  # noqa: PLW1510
            [
                "grep",
                "--recursive",
                "--binary-files=without-match",
                "--no-filename",
                "--exclude-dir=versioned_code",
                "--exclude-dir=versioned_docs",
                "--ignore-case",
                "-E",
                "--regexp",
                r"```(python|yaml).*name=",
                str(target_dir),
            ],
            text=True,
            capture_output=True,
        )
        res_snippet_used_names = subprocess.run(  # noqa: PLW1510
            ["sed", 's/.*="//; s/".*//; s/version-[0-9\\.]* //'],
            text=True,
            input=res_snippet_usages.stdout,
            capture_output=True,
        )
        return res_snippet_used_names.stdout.splitlines()
    except subprocess.CalledProcessError as e:
        raise RuntimeError(  # noqa: TRY003
            f"Command {e.cmd} returned with error (code {e.returncode}): {e.output}"
        ) from e


def main() -> None:
    check_dependencies("grep", "sed")
    project_root = pathlib.Path(__file__).parent.parent.parent
    docs_dir = project_root / "docs"
    assert docs_dir.exists()
    tests_dir = project_root / "tests"
    assert tests_dir.exists()
    new_violations = sorted(
        set(get_snippet_definitions(tests_dir))
        .difference(set(get_snippets_used(docs_dir)))
        .difference(set(UNREFERENCED_SNIPPETS))
    )
    if new_violations:
        print(f"[ERROR] Found {len(new_violations)} snippets which are not used within a doc file.")
        for line in new_violations:
            print(line)
        sys.exit(1)
    else:
        print("No unexpected unused snippets found")


if __name__ == "__main__":
    main()

# Enterprise Test Framework

A Python test-automation project built with [Playwright](https://playwright.dev/python/) and `pytest`.

The project follows a page-object structure. Browser interactions for Amazon are grouped in an `Amazon` page object, while automated checks are kept under the `tests/` directory.

## Project structure

```text
.
├── pages/          # Page objects and browser interaction helpers
├── tests/          # Automated tests
├── conftest.py     # Shared pytest fixtures and configuration
├── pytest.ini      # Pytest settings
├── requirement.txt # Python dependencies
└── .gitignore      # Local and generated files excluded from Git
```

## Requirements

- Python 3.10 or newer
- Google Chrome or another browser supported by Playwright

## Installation

Create and activate a virtual environment, then install the project dependencies:

```bash
python -m venv venv
```

Windows:

```powershell
venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
source venv/bin/activate
```

Install the Python packages:

```bash
pip install -r requirement.txt
```

Install the Playwright browser binaries:

```bash
playwright install
```

## Running the tests

Run the complete test suite from the project root:

```bash
pytest
```

For more detailed output:

```bash
pytest -v
```

Select the target environment at runtime:

```bash
pytest --env dev
pytest --env stage
```

Environment URLs are maintained in `data/environments.json`. Replace the stage placeholder URLs with your actual staging URLs before running stage tests.

Choose the browser at runtime as well:

```bash
pytest --env dev --browser chromium
pytest --env dev --browser firefox
pytest --env stage --browser webkit
```

Supported browsers are `chromium`, `firefox`, and `webkit`. Install their Playwright binaries before running them:

```bash
playwright install
```

By default, tests run with a visible browser window. Use `--headless` for CI or background execution:

```bash
pytest --env dev --browser chromium --headless
```

When a browser test fails, a full-page screenshot is saved under `test-results/screenshots/`.

Generate an HTML test report with:

```bash
pytest --html=test-results/report.html --self-contained-html
```

To run one test module or one test case:

```bash
pytest tests/test_amazon.py
pytest tests/test_amazon.py -k search
```

## Page-object example

The Amazon page object provides actions for loading the page, searching for an item, submitting the search, and counting search results. Tests should use these page-object methods instead of placing selectors directly in test cases.

## Development notes

- Run commands from the repository root.
- Keep browser selectors and page interactions in `pages/`.
- Keep assertions and test scenarios in `tests/`.
- Do not commit the virtual environment, Python cache files, or pytest cache; these are excluded by `.gitignore`.

## Troubleshooting

If Playwright reports that a browser executable is missing, run:

```bash
playwright install
```

If dependencies are missing, activate the virtual environment and reinstall them with `pip install -r requirement.txt`.

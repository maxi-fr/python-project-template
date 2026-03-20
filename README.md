# Simple Python Project Template

A simple Python project template using [uv](https://github.com/astral-sh/uv) and [ruff](https://github.com/astral-sh/ruff), designed for modern Python development.

## Features

-   **Dependency Management:** Powered by `uv`.
-   **Linting & Formatting:** Fast and consistent code style with `ruff`.
-   **Testing:** Pre-configured `pytest` setup.
-   **Code Quality:** Robust pre-commit hooks configured for formatting, linting, and type checking.
-   **Python Version:** Targets Python 3.13 by default (configurable).

## Usage

You need to have `cookiecutter` installed:

```bash
uv tool install cookiecutter
```

Generate a new project:

```bash
cookiecutter https://github.com/yourusername/simple-python-template
# or if you have cloned this repo locally:
cookiecutter .
```

Follow the prompts to configure your project.

## After Generation

1.  Navigate to your new project directory:
    ```bash
    cd my_awesome_project
    ```

2.  Initialize a git repository:
    ```bash
    git init
    git add .
    git commit -m "Initial commit"
    ```

3.  Install dependencies:
    ```bash
    uv sync
    ```

4.  Set up pre-commit hooks (automatically generates `requirements.txt`, lints, and runs tests):
    ```bash
    uv run pre-commit install
    ```

5.  Run tests manually (optional, since pre-commit does it too):
    ```bash
    uv run pytest
    ```

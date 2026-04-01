# Simple Python Project Template

A simple Python project template using [uv](https://github.com/astral-sh/uv) and [ruff](https://github.com/astral-sh/ruff), designed for modern Python development.

## Features

-   **Dependency Management:** Powered by `uv`.
-   **Linting & Formatting:** Fast and consistent code style with `ruff`.
-   **Testing:** Pre-configured `pytest` setup.
-   **Code Quality:** Robust pre-commit hooks configured for formatting, linting, and type checking.
-   **Python Version:** Targets Python 3.13 by default (configurable).

## Usage

You need to have cookiecutter installed (preferably via uv):
```console
uv tool install cookiecutter
```

Generate a new project:

```console
cookiecutter https://github.com/yourusername/simple-python-template
# or if you have cloned this repo locally:
cookiecutter .
```

Follow the prompts to configure your project.

## After Generation

1.  Navigate to your new project directory
    ```console
    cd my_awesome_project
    ```

2.  Initialize a git repository \
    *Crucial*: Do this before installing hooks.
    ```console
    git init
    ```

3.  Install dependencies
    ```console
    uv sync
    ```

4.  Set up pre-commit hooks (automatically generates `requirements.txt`, lints, and runs tests)
    ```console
    uv run pre-commit install
    ```
5.  Initial commit:   
    ```console
    git add .
    git commit -m "Initial commit"
    ```

6.  Run tests manually (optional, since pre-commit does it too)
    ```console
    uv run pytest
    ```

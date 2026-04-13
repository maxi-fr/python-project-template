# Simple Python Project Template

A simple Python project template using [uv](https://docs.astral.sh/uv/) and [ruff](https://github.com/astral-sh/ruff), designed for modern Python development.

## Features

-   **Dependency Management:** Powered by `uv`.
-   **Linting & Formatting:** Fast and consistent code style with `ruff`.
-   **Testing:** Pre-configured `pytest` setup.
-   **Type Checking:** Integrated with `mypy`.
-   **Code Quality:** Robust pre-commit hooks configured for formatting, linting, type checking, automatically generating `requirements.txt`.


# Usage

Install [uv](https://docs.astral.sh/uv/) following [these instructions](https://docs.astral.sh/uv/getting-started/installation/).  


Install [cookiecutter](https://www.cookiecutter.io/) installed (preferably via uv):
```console
uv tool install cookiecutter
```

## Generation

Generate a new project:

```console
cookiecutter https://github.com/maxi-fr/python-project-template
```
or if you have cloned this repo locally:
```console
cookiecutter .
```

Follow the prompts to configure your project.

## Initialization

1.  Navigate to your new project directory
    ```console
    cd my_new_project
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

4.  Set up pre-commit hooks
    ```console
    uv run pre-commit install
    ```
5.  Initial commit:   
    ```console
    git add -a
    git commit -m "Initial commit"
    ```
## After Initialization
Once initialized, you can use the following commands to manage your project:


| Task                | Command            |
|---------------------|--------------------|
| Adding dependencies | uv add <dependency>|
| Sync Dependencies   | uv sync            |
| Linting (Manual)    | uv run ruff check  |
| Formatting (Manual) | uv run ruff format |
| Run Tests           | uv run pytest      |
| Type Checking       | uv run mypy .      |
| Pre-commit Hooks    | uv run pre-commit --all-files  |





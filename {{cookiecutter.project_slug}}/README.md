# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

## Development

This project uses [uv](https://github.com/astral-sh/uv) for dependency management and [ruff](https://github.com/astral-sh/ruff) for linting and formatting.

### Setup

1.  Install `uv`:
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

2.  Sync dependencies:
    ```bash
    uv sync
    ```

3.  Set up pre-commit hooks:
    ```bash
    uv run pre-commit install
    ```

### Running Tests

To run tests using `pytest`:

```bash
uv run pytest
```

### Linting and Formatting

To check for linting errors:

```bash
uv run ruff check .
```

To format code:

```bash
uv run ruff format .
```

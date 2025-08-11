## Local MCP Repository Setup with `uv`

This guide will help you set up the repository using [`uv`](https://github.com/astral-sh/uv), a fast Python package manager and virtual environment tool.

### Prerequisites

- Python 3.8 or newer installed
- [`uv`](https://github.com/astral-sh/uv) installed (see below)

### Install `uv`

You can install `uv` via Homebrew:

```sh
brew install uv
```

Or with pipx:

```sh
pipx install uv
```

### Create and Activate Environment

```sh
uv venv
source .venv/bin/activate
```

### Install Dependencies

If you have a `requirements.txt` or `pyproject.toml`, install dependencies with:

```sh
uv pip install -r requirements.txt
# or
uv pip install .
```

### Run the Server

```sh
python fastmcp_server.py
```

---

For more details on `uv`, see the [uv documentation](https://github.com/astral-sh/uv).
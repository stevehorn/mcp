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

```sh
uv pip install -r requirements.txt
```

### Run the Server

```sh
python main.py
```

## Connect via MCP inspector

1. Launch the inspector.

```
npx @modelcontextprotocol/inspector
```

2. Configure the inspector

```
Transport Type: STDIO
Command: {Path to the python executable in your venv}
Arguments: {Path to ./main.py (fully qualified)}
```

## Connecting VS Code to Your Local MCP Server

To connect VS Code to your local MCP server, follow these steps:

1. **Create the configuration file:**

   - In your project root, create a new file at `.vscode/mcp.json`.

2. **Add the following configuration:**

   ```json
   {
     "servers": {
       "livefront": {
         "type": "stdio",
         "command": "/absolute/path/to/mcp/.venv/bin/python",
         "args": ["/absolute/path/to/mcp/main.py"]
       }
     },
     "inputs": []
   }
   ```

   - Replace `/absolute/path/to/mcp` with the full path to your local repository.
   - Ensure the Python executable and `main.py` paths are correct for your environment.

This configuration enables VS Code to communicate with your MCP server using STDIO transport.

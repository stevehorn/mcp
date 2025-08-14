# Contributing Guidelines

Welcome to the Livefront MCP repository! Our goal is to standardize and refine prompts that can be shared across Livefront.

## Project Structure

```text
mcp/
├── core/                # Core utilities and shared logic
│   └── utils.py
├── livefront_mcp/       # MCP server implementation and main modules
│   ├── code_review.py
│   └── mcp_instance.py
├── prompts/             # Prompt templates organized by topic
│   ├── code_review/
│   │   ├── csharp/
│   │   │   └── csharp.md
│   │   └── shared/
│   │       ├── diff_review.md
│   │       └── shared.md
│   └── product_management/
│       └── new_ticket.md
├── main.py              # Entry point for MCP server
├── requirements.txt     # Python dependencies
├── README.md            # Project overview and setup
└── CONTRIBUTING.md      # Guidelines for contributors
```

## Recommended Directory Structure

- **core/**: Shared utilities and helper functions.
- **livefront_mcp/**: Main MCP server code and modules. Generally this is where prompts are surfaced.
- **prompts/**: All prompt templates, organized by topic (e.g., `code_review/`, `product_management.md`, etc.).
- **main.py**: Main entry point for running the MCP server.
- **requirements.txt**: List of required Python packages.
- **README.md**: Project overview, setup instructions, and usage.
- **CONTRIBUTING.md**: This guide for contributors.

## Workflow for Making Changes to MCP

1. **Work in the production repository as usual.**
   - Continue your client work and use this MCP server for code review and prompt refinement.
2. **Connect to the MCP server and refine prompts.**
   - Test, iterate, and improve prompts in your workflow.
3. **When improvements are discovered:**
   - Make changes to the relevant prompt files in the MCP repository.
   - Open a pull request to this repository describing the improvement and its impact.
   - Work with reviewers to ensure clarity and consistency.

## Guidelines for Contributors

- Focus on adding, refining, and organizing prompts that you feel are helpful to share with the broader team.
- Ensure prompt templates are clear and reusable.
- Follow the recommended directory structure for new files and modules.
- Use descriptive commit messages and pull request titles.
- Engage in code reviews and discussions to build shared understanding.

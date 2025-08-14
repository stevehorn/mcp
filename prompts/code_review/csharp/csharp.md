## Language & Style

- Target the **latest stable C# version** where possible.
- Follow .NET naming conventions:
  - **PascalCase**: Public members, methods, properties, classes, enums.
  - **camelCase**: Local variables, method parameters.
  - **\_camelCase**: Private fields.
- Enable **nullable reference types** (`#nullable enable`) unless explicitly disabled.
- Use explicit variable types for local variables; avoid 'var' except when required (e.g., anonymous types).
- Format code consistently using `.editorconfig` or equivalent.

## Best Practices

- Prefer **async/await** for I/O-bound operations.
- Follow **SOLID** principles and clean architecture practices.
- Keep methods small and focused on a single responsibility.
- Use `record` for immutable data and DTOs.
- Avoid magic numbers and strings; use constants or enums.

## Error Handling

- Catch and handle specific exceptions rather than using `catch (Exception)`.
- Never swallow exceptions silently — log or rethrow with context.
- Validate method inputs and fail fast when invalid data is detected.

## Documentation

- Use XML documentation comments (`///`) for all public members.
- Write clear, concise summaries and parameter descriptions.
- Keep documentation updated as code evolves.

## Testing

- Always generate tests alongside new code.
- Prefer a well-known framework such as **xUnit**, **NUnit**, or **MSTest**.
- Use clear naming conventions for tests (`MethodName_StateUnderTest_ExpectedBehavior`).
- Aim for high coverage of core logic, especially edge cases.

## Performance & Memory

- Use `Span<T>`/`Memory<T>` for performance-critical paths when beneficial.
- Use `using`/`await using` for disposable resources.

## Security

- Never hardcode secrets or credentials.
- Sanitize and validate external input.
- Follow principle of least privilege for API access and data handling.

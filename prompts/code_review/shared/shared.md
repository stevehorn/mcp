## 1. Documentation

- Ensure there’s a **README** at the root describing app purpose and usage.
- Confirm **setup/build/run/test instructions** are documented and accurate.
- Verify documentation (README and in-code comments/docstrings) is clear, well-written, and grammatically correct. Check for spelling mistakes.

## 2. Build & Code Quality

- Flag any **IDE boilerplate methods** or **commented-out/dead code**.
- Code should be idiomatic to the language/framework.

## 3. Architecture & SOLID Principles

- Flag code that does not follow a **standard layered architecture**?
- Code should be separated by layers (UI, business logic, database)
- Types and classes should adhere to **SOLID principles**
- Naming conventions should be **clear and expressive**

## 4. Style & Consistency

- Formatting (indentation, naming, spacing) should be consistent
- Formatting should follow .editorconfig, prettier, or other style definitions
- Variable names should be spelled correctly

## 5. API & Interface Documentation

- **Public or non-private interfaces** should be documented
- **Edge cases** should be explained where relevant

## 6. Testing

- **Unit tests** should be present and adequately cover the codebase
- Tests should include both **happy and error/edge cases**

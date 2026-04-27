# Installation

## Setup

```bash
# Install all dependencies (including dev group)
uv sync --group dev
```

## Running Tests

```bash
# Run all tests except stress tests
uv run pytest test/ -v -m "not stress"

# Run stress tests
uv run pytest test/ -v -m stress
```

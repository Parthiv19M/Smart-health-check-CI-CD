# AGENTS.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

A Python Flask application ("Smart Health Check") demonstrating CI/CD practices. It exposes two API endpoints (`/` and `/health`) and serves static HTML pages. Python 3.9+ is required.

## Architecture

There are two Flask entry points:

- **`app.py`** — The main application. Uses the factory pattern (`create_app()`) and is what tests, CI, and Heroku use. A module-level `app = create_app()` instance is exported for convenience. When `TESTING` config is set, the `/` route returns JSON instead of static HTML.
- **`server.py`** — A standalone dev server that serves `static/landing.html` on port 8000. Not used by tests or CI.

The `Procfile` runs the app via gunicorn: `gunicorn app:create_app()`.

Static frontend files live in `static/` (`index.html`, `landing.html`). Vercel deployment serves only the static files (configured in `vercel.json`).

## Build & Run Commands

```bash
# Create and activate virtualenv
python3 -m venv venv && source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Run the app locally (port 5001)
python app.py
```

## Testing

Tests are in `tests/test_app.py` and use pytest with the Flask test client.

```bash
# Run all tests
pytest

# Run a single test
pytest tests/test_app.py::test_health_endpoint

# Run tests with coverage (CI enforces 80% minimum)
pytest --cov=. --cov-report=xml
```

## Linting & Formatting

The project uses pre-commit hooks. Install them with `pre-commit install`. Configuration is in `pyproject.toml` and `.pre-commit-config.yaml`.

```bash
# Format code
black .

# Sort imports
isort .

# Lint
flake8 . --max-complexity=10 --max-line-length=88

# Security scan (skips assert warnings)
bandit -r . --skip B101

# Type checking
mypy --ignore-missing-imports .

# Docstring style
pydocstyle .

# Run all pre-commit hooks at once
pre-commit run --all-files
```

## CI/CD

GitHub Actions workflow at `.github/workflows/ci.yml` runs on pushes and PRs to `main`. It runs black, flake8, pytest with coverage, and a live endpoint smoke test against `localhost:5001/health`. All lint/test steps use `continue-on-error: true`, so the pipeline does not hard-fail on lint issues.

Heroku deployment job exists in CI but is currently commented out. It requires `HEROKU_API_KEY` and `HEROKU_APP_NAME` secrets.

Dependabot is configured (`.github/dependabot.yml`) for weekly updates to GitHub Actions and pip dependencies, ignoring semver-major bumps.

## Code Style

- Line length: 88 (Black default)
- Target Python version: 3.9
- Import sorting: isort with Black-compatible profile (multi_line_output=3, trailing comma)
- All public functions and modules require docstrings (enforced by pydocstyle)

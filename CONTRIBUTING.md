# Contributing

Thank you for helping improve the companion repository for *From Noodles to Neural Networks*.

## Before proposing a change

1. Search existing issues to avoid duplicate work.
2. Keep examples beginner-friendly and deterministic.
3. Use synthetic or openly licensed data only. Never commit confidential, personal, or proprietary data.
4. Do not commit credentials, local configuration, generated build output, or KDP upload files.

## Development setup

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install -e .
pytest
```

On Windows PowerShell, activate the environment with `.venv\Scripts\Activate.ps1`.

## Pull requests

- Make one focused change per pull request.
- Add or update tests for reusable Python code.
- Re-run affected data generators and verify deterministic output.
- Clear notebook execution errors and remove private paths or machine-specific metadata.
- Explain any change to generated data, figures, or documented results.

By contributing, you agree that your contribution may be distributed under the repository's applicable licences.


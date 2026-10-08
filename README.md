# Hello App

A simple Python app that asks for your name and greets you.

## Requirements

- Python 3.10 or newer
- Git

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/hello-app.git
cd hello-app
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

- Windows (PowerShell): `.venv\Scripts\Activate.ps1`
- Mac/Linux: `source .venv/bin/activate`

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run

```bash
python app.py
```

Example:

```
Enter your name: Deepthi
Hello Deepthi
```

If you press Enter without typing a name, the app asks again.

## Test

```bash
pytest
```as

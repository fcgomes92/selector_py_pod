# Selector Py Pod

## Install

Clone this repository

Create venv if not exists

```bash
python3 -m venv venv
```

Load the new venv

```bash
source venv/bin/activate
```

Install dependencies

```
python -m pip install -r requirements.txt .
```

Populate your env file based on `.env.example`
## Running

```bash
python -m selector_py_pod --show_id='spt:spotify:show:6IAVb4s0xkX9l9Ym9hZjM5' --name='Nigel Goodman' --description='Vâmo dormir!' --outputs twitter
```
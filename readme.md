## Create virtualenv and install dependency (for linux and mac)

```
python3 -m venv .venv
source .venv/bin/activate
```

```
pip3 install -r requirements.txt
```

## Run app

```
uvicorn app.main:app --reload
```

## Run test

```
pytest tests/
```

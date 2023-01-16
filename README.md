# FastAPI Introduction

This repository contains an example API, build using the FastAPI framework.

The code within this repository is written using 3.6/7/8/9 syntax - the syntax can change slightly for FastAPI from Python 3.10 onwards.

## Getting started

You can run the API yourself by:

###  Installing all requirements
```bash
python3 -m venv venv
source ./venv/bin/activate
pip3 install -r requirements.txt
```

### Running the application
```bash
uvicorn main:app --reload
```

The API docs can then be accessed at:

```
http://127.0.0.1:8000/docs
```

or...

```
http://127.0.0.1:8000/redoc
```

## Benefits of FastAPI

Aside from performance benefits, a major benefit of using FastAPI for your APIs is a lot of the 'grunt work' is handled automatically.

API endpoints are automatically documented, with both swagger and redoc specs being available.

By supplying type hints into your code, it is also possible to automatically parse user input, returning 422 errors for invalid input.
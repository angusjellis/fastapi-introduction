# FastAPI Introduction

This repository contains an example API, build using the FastAPI framework.

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

## Benefits of FastAPI

Aside from performance benefits, a major benefit of using FastAPI for your APIs is a lot of the 'grunt work' is handled automatically.

API endpoints are automatically documented, with both swagger and redoc specs being available.

By supplying type hints into your code, it is also possible to automatically parse user input, returning 422 errors for invalid input.
#!/bin/bash

# if using pyenv activate the virtual-env
#pyenv activate WebAPI

#pyenv activate WEBAPI2

# start uvicorn server serving the main app
python -m uvicorn brapi_v2.main:app --host 0.0.0.0 --port 9000 --reload

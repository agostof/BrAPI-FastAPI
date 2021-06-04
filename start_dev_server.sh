#!/bin/bash

# if using pyenv activate the virtual-env
# pyenv activate WebAPI

#pyenv activate WEBAPI2

# start uvicorn server serving the main app
# bind to localhost:9000
# check  --> http://127.0.0.1:9000/brapi/v2/serverinfo
python -m uvicorn brapi_v2.main:app  --port 9000 --reload

# use this version if you want to listen in all network devices
# python -m uvicorn brapi_v2.main:app --host 0.0.0.0 --port 9000 --reload



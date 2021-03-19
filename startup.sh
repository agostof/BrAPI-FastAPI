# pyenv activate WebAPI

pyenv activate WEBAPI2

python -m uvicorn brapi_v2.views:app --host 0.0.0.0 --port 9000 --reload

## Overview

## BrAPI-FastAPI: Python-based BrAPI server stubs

Implementation of the [BrAPI v2.0](https://brapi.org/) specification for Python using the [FastAPI](https://fastapi.tiangolo.com/) framework.
* includes models and server stubs (views.py) for [Core](brapi_v2/core), [Genotyping](brapi_v2/genotyping), [Germplasm](brapi_v2/germplasm), and [Phenotyping](brapi_v2/phenotyping).
* use as a template to create your Python-based [BrAPI server](brapi_v2/main.py)
* use models to create a [BrAPI client](client/brapi_client.py) (a.k.a BrAPP) or to create a client library

## Quick start
1. Installation using pyenv, skip this step if you don't want to use pyenv.
``` sh
pyenv virtualenv 3.9.1 WebAPI
pyenv activate WebAPI
```
2. Install module dependencies
``` sh
python -m pip install -r requirements.txt
```
3. Then start server
``` sh
cd server
./start_dev_server.sh
```
The local server should be running at `port 9000`, to see available enpoints visit your serverinfo endpoint: http://127.0.0.1:9000/brapi/v2/serverinfo. Available end-points are also listed in the [server's README](server/README.md).

### Auto-generated documentation
The default FastAPI server will generate and display documentation for your running instance using *Swagger UI* and *ReDoc*. This documentation will be available at `{server_url}/docs` or `{server_url}/redocs`. Check the [server's README](server/README.md) for details.


## Using as a BrAPI server template

If you want to use these stubs as a template you can add them in your project by running:

```sh
git submodule add https://github.com/agostof/BrAPI-FastAPI [optional local_name]
```
Then use (by copying or modifying) the appropriate BrAPI module(s) views (controllers) and models as needed.

## Using for building BrAPI clients

Simple clients could be built using the Pydantic models to parse the responses returned by the server.
For example, to parse the serverInfo call response we could import the following **ServerInfoResponse** model:
```python
from brapi_v2.core.models import ServerInfoResponse
```
then use the module to contruct an object that could be used by the client.

This is demonstrated by a simple [brapi_client](client/brapi_client.py) that parses the demo endpoints already defined by this server, see [client's documentation](client/README.md) for details.

## Notes

The auto-generated models still need cleaning up. ~~Also some models names are *repeated* across modules e.g. **Metadata**, **AdditionalInfo**.~~ These *repeated* models were consolidated and they are uniquely imported from core.models e.g. **core.models.Metadata**,  **core.models.AdditionalInfo**, etc.

These redundant Pydantic models occur because the BrAPI OpenAPI spec files were processed independently.
Ideally, they should be consolidated as part of the Core module or in a *commons* package. Check the [modelgen_utils](modelgen_utils) directory for additional details.

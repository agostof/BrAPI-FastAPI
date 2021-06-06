# Overview

## BrAPI-FastAPI: Python-based BrAPI server stubs

Implementation of the [BrAPI v2.0](https://brapi.org/) specification for Python using the [FastAPI](https://fastapi.tiangolo.com/) framework.
* includes models and server stubs (views.py) for [Core](brapi_v2/core), [Genotyping](brapi_v2/genotyping), [Germplasm](brapi_v2/germplasm), and [Phenotyping](brapi_v2/phenotyping).
* use as a template to create your Python-based [BrAPI server](server/brapi_v2/main.py)
* use models to create a [BrAPI client](client/brapi_client.py) (a.k.a BrAPP) or to create a client library

## Quick start
1. Installation using pyenv (Python $version could be 3.8.3 and above). If not using pyenv just skip to the next step.
``` sh
pyenv virtualenv 3.9.1 WebAPI
pyenv activate WebAPI
```
2. Install module dependencies
``` sh
python -m pip install -r requirements.txt
```
3. Then start server (do check the script in case you want to modify how the server starts)
``` sh
cd server
./start_dev_server.sh
```

4. Now check the API server at: http://127.0.0.1:9000/brapi/v2/serverinfo
5. Self-generated documentation can be seen in the following endpoints:
    1. http://127.0.0.1:9000/docs or
    2. here http://127.0.0.1:9000/redoc

A few test(dummy) endpoints have been provided from each BrAPI module: Core, Genotyping, Germplasm, Phenotyping.
* These are the example endpoints:
    * brapi/v2/serverinfo
    * brapi/v2/samples
    * brapi/v2/attributes
    * brapi/v2/events

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

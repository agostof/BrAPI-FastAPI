## BrAPI-FastAPI: Server Stubs

Implementation of the [BrAPI v2.0](https://brapi.org/) specification for Python using the [FastAPI](https://fastapi.tiangolo.com/) framework.
* includes models and server stubs (views.py) for [Core](../brapi_v2/core), [Genotyping](../brapi_v2/genotyping), [Germplasm](../brapi_v2/germplasm), and [Phenotyping](../brapi_v2/phenotyping).
* use as a template to create your Python-based [BrAPI server](../brapi_v2/main.py)

## Run BrAPI server
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
./start_dev_server.sh
```

4. Now check the API server at: http://127.0.0.1:9000/brapi/v2/serverinfo
## Auto-generated documentation
The default FastAPI server will generate and display documentation for your running instance. This documentation will be available at `http://127.0.0.1:9000/docs` or `http://127.0.0.1:9000/redocs`.
To control *if* and *how* this documentation is display, see [FastAPI](https://fastapi.tiangolo.com/tutorial/metadata).
## Available endpoints
A few test(dummy) endpoints have been provided from each BrAPI module: Core, Genotyping, Germplasm, Phenotyping.
* These are the example endpoints available:
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

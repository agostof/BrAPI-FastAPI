## BrAPI-FastAPI: Server Stubs

Implementation of the [BrAPI v2.0](https://brapi.org/) specification for Python using the [FastAPI](https://fastapi.tiangolo.com/) framework.
* Includes models and server stubs (views.py) for [Core](../brapi_v2/core), [Genotyping](../brapi_v2/genotyping), [Germplasm](../brapi_v2/germplasm), and [Phenotyping](../brapi_v2/phenotyping).
* Use as a template to create your Python-based [BrAPI server](../brapi_v2/main.py).

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
The default **FastAPI** server will generate and display documentation for your running instance using **Swagger UI** and **ReDoc**. This documentation will be available at `http://127.0.0.1:9000/docs` or `http://127.0.0.1:9000/redocs` respectively.
To control **if** and **how** this documentation is displayed, see the [FastAPI](https://fastapi.tiangolo.com/tutorial/metadata) documentation.
## Available endpoints
A few test (dummy) endpoints have been provided from each BrAPI module (at least one per module): Core, Genotyping, Germplasm, and Phenotyping.
* These are the example endpoints available:
    * brapi/v2/serverinfo
    * brapi/v2/samples
    * brapi/v2/attributes
    * brapi/v2/events

## Using as a BrAPI server template

If you want to use these stubs as a template, you can add them into your project by running:
```sh
git submodule add https://github.com/agostof/BrAPI-FastAPI [optional local_name]
```
Then use (by copying or modifying) the appropriate BrAPI module(s) views (controllers) and models as needed.
## Implementing BrAPI endpoints
All the server stubs provided here have a stucture similar to this:
```python
@app.get('/endpoint_name', response_model_obj)
def httpmethod_endpoint_name(query_parameters) -> ResponseReturnType:
    #... empty body
    pass # <--- do nothing
```
When building a response our task is to turn them into something that generally looks like this:
```python
@app.get('/endpoint_name', response_model_obj)
def httpmethod_endpoint_name(query_parameters) -> ResponseReturnType:
    # setup code ... (e.g. function specific imports)
    # This should be filled with your implementation!
    # e.g. get data, build medatada, build response of ResponseReturnType
    # general steps:
    # 1. get some data, and its medatada
    # 2. format results (build some kind of Result object)
    # 3. build some kind of ResponseReturnType object
    # 4. done -> send response back to client
    return ResponseReturnType
```
To give a more concrete example, let's look at a very simple endpoint. The server stub for */brapi/v2/commoncropnames* might look like this (if you want to follow along check the code in [core.views.py](../brapi_v2/core/views.py#L66-L77)):
```python
@app.get('/commoncropnames', response_model=CommonCropNamesResponse)
def get_commoncropnames(
    page: Optional[int] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> CommonCropNamesResponse:
    """
    Get the Common Crop Names
    """
    # If your are new to Python the "pass" keyword below just means do nothing, which
    # results in empty function in this case! 
    # We will remove this and fill it with our "common crop names" implementation in just a bit...
    pass  # <-- do nothing!
    
 ```
The first pattern that you might notice is that the return response object name is a combination of the EndPointName + Response, e.g. `commoncropnames --> CommonCropNamesResponse`.

In general, the response structure of a BrAPI call has two components at the top level: a metadata object and a data results list. To create a response, we need *at least* the following objects: **Metadata**, **IndexPagination**, and a **Result**, and a **Response** objects of the endpoint's data type.

To illustrate how this process works, lets look at the **CommonCropNamesResponse**, defined in [core.models.py](../brapi_v2/core/models.py#L1477-L1480):
```python
# brapi_v2/core/models.py
class CommonCropNamesResponse(BaseModel):
    _context: Optional[Context] = Field(None, alias='@context')
    metadata: Metadata
    result: CommonCropNamesResponseResult # <-- we need this to hold our data
```
We see that the *ResponseResult* model needed to hold our data should be an instance of **CommonCropNamesResponseResult**, which is defined as follows:
```python
# brapi_v2/core/models.py
class CommonCropNamesResponseResult(BaseModel):
    data: List[str] = Field(
        ...,
        description='array of crop names available on the server',
        example=['Tomatillo', 'Paw Paw'],
    )
```
With these pieces of information, we are ready to build the **CommonCropNamesResponse** needed to implement the endpoint example for */brapi/v2/commoncropnames* (*well, sort of, just with dummy data!!*).

First, let's assume we have a database that tracks which crops are available, and that we can get the data in a list `available_crops`. Using this data, we will build a response with `available_crops` and the associated medatadata as follows: 
```python
    pagination = IndexPagination(
        currentPage=0,  # required
        pageSize=1000,  # required
        totalCount=total_items,  # optional
        totalPages=1,  # 1 in our case
    )
    metadata = Metadata(
        pagination=pagination,
        # datafiles=[],  # optional
        # status=[]  # optional
    )
```
Then we can combine the data and metadata to create **CommonCropNamesResponseResult** and **CommonCropNamesResponse** which is what we need our *server* to send back to any *client*. If we put it all together we have the following function:
```python
@app.get('/commoncropnames', response_model=CommonCropNamesResponse)
def get_commoncropnames(
    page: Optional[int] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> CommonCropNamesResponse:
    
    # import models needed
    from .models import CommonCropNamesResponseResult, CommonCropNamesResponse
    
    # simulated crop db, use your real database here
    available_crops = ['rice', 'maize', 'wheat', 'tomato', 'sorghum']
    total_items = len(available_crops)
    
    pagination = IndexPagination(
        currentPage=0,  # required
        pageSize=1000,  # required
        totalCount=total_items,  # optional
        totalPages=1,  # 1 in our case
    )
    
    metadata = Metadata(
        pagination=pagination,
        # datafiles=[],  # optional
        # status=[]  # optional
    )

    # build result object
    result = CommonCropNamesResponseResult(
        data=available_crops # it accepts a list of strings
    )

    # build a response!!
    response = CommonCropNamesResponse(
        metadata=metadata,
        result=result
    )

    # if all goes well we should have a response to send back to the client!!! \(^.^)/
    # check: http://{your_url}/brapi/v2/commoncropnames
    return response

```
If you are following along, fill free to replace the `get_commoncropnames` in your copy of [core.views.py](../brapi_v2/core/views.py) with the code above. After this, your server should refresh, and the endpoint should be available for querying. You will need to access the endpoint directly by calling *http://{your_url}/brapi/v2/commoncropnames*. *Note: We have to use direct access becasue we have not added this new endpoint yet to the /serverinfo call in [core.views.py](../brapi_v2/core/views.py#L600-668). We leave that as an excercise for the reader.*
The output of our newly constructed BrAPI call (i.e. *http://{your_url}/brapi/v2/commoncropnames*) should contain the following information:
```json
    {
        "metadata": {
            "datafiles": null,
            "status": null,
            "pagination": {
                "pageSize": 1000,
                "totalCount": 5,
                "totalPages": 1,
                "currentPage": 0
            }
        },
        "result": {
            "data": [
                "rice",
                "maize",
                "wheat",
                "tomato",
                "sorghum"
            ]
        }
    }
```
If you got the output above, you have successfully implemented a BrAPI endpoint!🎉
If you want to remove the `null` values from the response, add this parameter to the function decorator: `response_model_exclude_unset` as follows:
```python
# decorator
@app.get('/commoncropnames', response_model=CommonCropNamesResponse, response_model_exclude_unset=True)
```
With that change, your output should look like this:
```json
    {
        "metadata": {
            "pagination": {
                "pageSize": 1000,
                "totalCount": 5,
                "totalPages": 1,
                "currentPage": 0
            }
        },
        "result": {
            "data": [
                "rice",
                "maize",
                "wheat",
                "tomato",
                "sorghum"
            ]
        }
    }
```
## Why I did not see *"/brapi/v2"* on endpoint definitions?
You might have noticed that the */brapi/v2* prefix string is missing from endpoint definitions. This is because that prefix is already added when each view is mounted to the app using the [APIRouter](https://fastapi.tiangolo.com/tutorial/bigger-applications/#apirouter) feature. This is done in the applications [main.py](../brapi_v2/main.py), in detail:
```python
# brapi_v2/main.py
#...

app.include_router(core.views.router, prefix='/brapi/v2')
app.include_router(genotyping.views.router, prefix='/brapi/v2')
app.include_router(germplasm.views.router, prefix='/brapi/v2')
app.include_router(phenotyping.views.router, prefix='/brapi/v2')

#...
```

On that note, [main.py](../brapi_v2/main.py) has other settings worth checking like, [CORS](https://fastapi.tiangolo.com/tutorial/cors/)(Cross-Origin Resource Sharing), application root-level endpoints among others, please take a look. 
 
## What is left?
Now you have enough information to start filling any of the server stubs that you need. Things like security and databases connectivity (e.g. [SQLAlchemy](https://www.sqlalchemy.org/)) will be needed but are beyond the scope of this document. Consult the [FastAPI](https://fastapi.tiangolo.com/) documentation for details about which options are available to address these concerns.

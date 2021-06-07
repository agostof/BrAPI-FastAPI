# BrAPI-FastAPI: Python-based BrAPI clients
## Using for building BrAPI clients

The Pydantic models can be used to parse the responses returned by a BrAPI server. We can figure out what is the appropriate response object to use for a given call by looking at the server stubs, the API specification, or the auto-generated docs from your FastAPI:BrAPI server instance e.g. **{your_server_url}/docs**.

For instance, to parse the ServerInfo call we would use the **ServerInfoResponse** model, then we could parse the response by using the appropriate Pydantic method (e.g. *parse_obj*, *parse_raw*) as follows:
```python
# 
from brapi_v2.core.models import ServerInfoResponse
# ...
# use favorite library to get an response in JSON format
response_json_text = fav_lib(url)
# ...
# parse dictionary using pydantic model
server_info = ServerInfoResponse.parse_obj(json.loads(response_json_text))

# parse parse text using pydantic model
server_info = ServerInfoResponse.parse_raw(response_json_text)

# Since the responses are pydantic model instances
# we could use them as part of our tests e.g:
assert isinstance(server_info, ServerInfoResponse)

# work with your data here ...
# e.g. access the BrAPI responses metadata and results
# server_info.metadata, server_info.result
print("Server info metadata", server_info.metadata)
# ...
# please check the code in barebones_brapi_client.py for more details

```
In order to parse all the responses provided by the example **BrAPI server** we needed the following models:
```python
from brapi_v2.core.models import ServerInfoResponse
from brapi_v2.genotyping.models import SampleListResponse
from brapi_v2.germplasm.models import GermplasmAttributeListResponse
from brapi_v2.phenotyping.models import EventsResponse
```

Look at the [barebones_brapi_client](barebones_brapi_client.py) for a very basic working implementation of the concepts outline above.
To run the example:
```sh
python barebones_brapi_client.py
```
Here is an example of the output:
```
==================================
Supported BrAPI calls on: http://127.0.0.1:9000/brapi/v2
row_no	endpoint	full_url
1	/serverinfo	http://127.0.0.1:9000/brapi/v2/serverinfo
2	/events	http://127.0.0.1:9000/brapi/v2/events
3	/attributes	http://127.0.0.1:9000/brapi/v2/attributes
4	/samples	http://127.0.0.1:9000/brapi/v2/samples

==================================
Querying germplasm endpoint: /attributes
Germplasm Attributes results:
row_no	attributeName	attributeName
1	Plant Height Example	Plant Height Example
2	Dry Weight Example	Dry Weight Example
3	Leaf Weight Example	Leaf Weight Example

==================================
Querying genotyping endpoint: /samples
Genotyping Samples results:
row_no	sampleDbId	sampleName
1	1213234	dummy sample 1
2	981975	dummy sample 2
3	5361	dummy sample 3
4	7148	dummy sample 4
5	8935	dummy sample 5
6	10722	dummy sample 6
7	12509	dummy sample 7
8	14296	dummy sample 8

==================================
Querying phenotyping endpoint: /events
Phenotyping Events results:
row_no	eventDbId	eventType	eventDescription
1	123456789	JUST_AN_EXAMPLE	FIRST Testing event!!
2	912831282	JUST_AN_EXAMPLE	Testing event number two

==================================
```
Check the [Pydanic](https://pydantic-docs.helpmanual.io/) documentation for more details on how to parse, construct, and validate data with the data models provided.

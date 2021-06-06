# BrAPI-FastAPI: Python-based BrAPI clients
## Using for building BrAPI clients

We can use the Pydantic models to parse the responses returned by the server. By looking at the server stubs and the API specification we can figure out what is the approriate response object to use for a given call.

For instance, to parse the ServerInfo call we would use the **ServerInfoResponse** model, then we could parse the response by using the appropriate Pydantic method as follows:
```python
from brapi_v2.core.models import ServerInfoResponse
# parse dictionary
server_info = ServerInfoResponse.parse_obj(json.loads(response_json_text))

# parse parse text
server_info = ServerInfoResponse.parse_raw(response_json_text)

# work with your data here
# ...
```
In order to parse all the reponses provided in the example **BrAPI server** we needed the following models:
```python
from brapi_v2.core.models import ServerInfoResponse
from brapi_v2.genotyping.models import SampleListResponse
from brapi_v2.germplasm.models import GermplasmAttributeListResponse
from brapi_v2.phenotyping.models import EventsResponse
```

Look at the [brapi_client](brapi_client.py) for a very basic implementation of this concept.
To run the example:
```sh
python client/brapi_client.py
```
Here is an example of output:
```
==================================
Supported BrAPI calls on: http://127.0.0.1:9000/brapi/v2
row_no	end_point	full_url
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

==================================
Querying genotyping endpoint: /samples
Genotyping Samples results:
row_no	sampleDbId	sampleName
1	1213234	dummy sample 1
2	981975	dummy sample 2

==================================
Querying phenotyping endpoint: /events
Phenotyping Events results:
row_no	eventDbId	eventType	eventDescription
1	123456789	JUST_AN_EXAMPLE	FIRST Testing event!!
2	912831282	JUST_AN_EXAMPLE	Testing event number two

==================================
```
Check the [Pydanic](https://pydantic-docs.helpmanual.io/) documentation for more details.
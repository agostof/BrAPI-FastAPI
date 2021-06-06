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
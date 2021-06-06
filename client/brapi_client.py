import requests
import re
from brapi_v2.core.models import ServerInfoResponse, HttpMethod
from brapi_v2.genotyping.models import SampleListResponse
from brapi_v2.germplasm.models import GermplasmAttributeListResponse
from brapi_v2.phenotyping.models import EventsResponse


# run an HTTP request against a BrAPI server
# it will try to parse the response using the 
# provided pydantic datamodel
def run_brapi_request(url, method, datamodel, payload = {}, headers = {}):
    response = requests.request(method.name, url, headers=headers, data=payload)
    # if response.status_code == 200:
    result = datamodel.parse_raw(response.text)
    return response.status_code, result


api_url = "http://127.0.0.1:9000/brapi/v2"

server_info_url = api_url+"/serverinfo"
status_code, server_info = run_brapi_request(server_info_url, HttpMethod.GET, ServerInfoResponse)

regexp = re.compile('.*(?P<api_name>brapi/v2)(?P<end_point>.*)')
# access metadata
# print("Call metadata", server_info.metadata)

print("\n==================================")
print(f"Supported BrAPI calls on: {api_url}")
print("row_no\tend_point\tfull_url")
for count, call in enumerate(server_info.result.calls, 1):
    service_match = regexp.match(call.service)
    # extract the end-point from the call
    if service_match:
        service_detail = service_match.groupdict()
        end_point = service_detail['end_point']
    else:
        end_point = ''
    print(f"{count}\t{end_point}\t{call.service}")

print("\n==================================")


# run a query against germplasm attributes
print("Querying germplasm endpoint: /attributes")
germplasm_url = api_url + "/attributes"
status_code, germplasm_attributes = run_brapi_request(germplasm_url, HttpMethod.GET, GermplasmAttributeListResponse)
print("Germplasm Attributes results:")
print("row_no\tattributeName\tattributeName")
# for count,sample in enumerate(samples.result.data, 1):
#     print(f'{count}\t{sample.sampleDbId}\t{sample.sampleName}')
for count, attribute in enumerate(germplasm_attributes.result.data, 1):
    print(f'{count}\t{attribute.attributeName}\t{attribute.attributeName}')
print("\n==================================")

# run a query against genotyping
print("Querying genotyping endpoint: /samples")
genotyping_samples_url = api_url + "/samples"
status_code, samples = run_brapi_request(genotyping_samples_url, HttpMethod.GET, SampleListResponse)
print("Genotyping Samples results:")
print('row_no\tsampleDbId\tsampleName')
for count,sample in enumerate(samples.result.data, 1):
    print(f'{count}\t{sample.sampleDbId}\t{sample.sampleName}')
print("\n==================================")


# run a query against phenotyping
print("Querying phenotyping endpoint: /events")
phenotyping_events_url = api_url + "/events"
status_code, pheno_events = run_brapi_request(phenotyping_events_url, HttpMethod.GET, EventsResponse)
print("Phenotyping Events results:")
print('row_no\teventDbId\teventType\teventDescription')
for count,event in enumerate(pheno_events.result.data, 1):
    print(f'{count}\t{event.eventDbId}\t{event.eventType}\t{event.eventDescription}')
print("\n==================================")


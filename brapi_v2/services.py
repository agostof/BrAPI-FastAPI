from .models import *

ServerInfo.update_forward_refs()

'''
  Registers services
'''
def getServices():
    # Basic services to implement
    # http://{{ApiHost}}/brapi/v2/serverinfo
    # http://{{ApiHost}}/brapi/v2/studies
    # http://{{ApiHost}}/brapi/v2/variantsets/
    # http://{{ApiHost}}/brapi/v2/variantsets/{variantSetDbId}}/calls
    # http://{{ApiHost}}/brapi/v2/variantsets/{variantSetDbId}}/callsets
    # http://{{ApiHost}}/brapi/v2/variantsets/{variantSetDbId}}/variants

    services = []
    services.append(
        Service(service="token", 
                dataTypes=[ WSMIMEDataTypes.application_json],
                methods=[Method.POST],
                versions=[Version.v2_0])
    )
    services.append(
        # Lists Studies 
        Service(service="studies",
                dataTypes=[ WSMIMEDataTypes.application_json],
                methods=[Method.GET],
                versions=[Version.v2_0])
    )

    services.append(
        #  Lists VariantSets
        Service(service="variantsets", 
                dataTypes=[ WSMIMEDataTypes.application_json],
                methods=[Method.GET],
                versions=[Version.v2_0])
    )
    services.append(
        #  Lists genotypes present in a VariantSet
        Service(service="variantsets/{variantSetDbId}/calls", 
                dataTypes=[ WSMIMEDataTypes.application_json],
                methods=[Method.GET],
                versions=[Version.v2_0])
    )

    services.append(
        #  Lists Callsets present in a VariantSet
        Service(service="variantsets/{variantSetDbId}/callsets", 
                dataTypes=[ WSMIMEDataTypes.application_json],
                methods=[Method.GET],
                versions=[Version.v2_0])
    )

    services.append(
        #  Lists Variants present in a VariantSet
        Service(service="variantsets/{variantSetDbId}/variants", 
                dataTypes=[ WSMIMEDataTypes.application_json],
                methods=[Method.GET],
                versions=[Version.v2_0])
    )

    services.append(
        # Extract data from a specific VariantSet
        Service(service="variantsets/extract",
                dataTypes=[ WSMIMEDataTypes.application_json],
                methods=[Method.POST],
                versions=[Version.v2_0])
    )
    #service = Service(service="token", dataTypes='aplication.json', methods="POST", versions="2.0")
    
#    serverinfo = ServerInfo(serverName = 'hostapplication/json', text_csv = results)

    # dataTypes: Optional[List[WSMIMEDataTypes]] = Field(
    #     None,
    #     description='The possible data formats returned by the available call',
    #     example=['application/json'],
    # )
    # methods: List[Method] = Field(
    #     ...,
    #     description='The possible HTTP Methods to be used with the available call',
    #     example=['GET', 'POST'],
    # )
    # service: str = Field(
    #     ...,
    #     description='The name of the available call as recorded in the documentation',
    #     example='germplasm/{germplasmDbId}/pedigree',
    # )
    # versions: List[Version] = Field(
    #     ...,
    #     description='The supported versions of a particular call',
    #     example=['2.0', '2.1'],
    # )
    return services
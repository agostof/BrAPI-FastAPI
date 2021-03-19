def get_serverinfo(
    data_type: Optional[WSMIMEDataTypes] = Query(None, alias='dataType'),
    authorization: Optional[constr(regex='^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> ServerinfoGetResponse:
    """
    Get the list of implemented Calls
    """
    import subprocess
    

    results = subprocess.check_output(['bcftools', '--help'])
    from .models import Metadata, ServerInfo

    metadata = Metadata(datafiles=[], status=[])
    from .services import getServices
    services = getServices()
    serverinfo = ServerInfo(serverName='BrAPI<-->FASTAPI Test Server',
                    organization="Cornell University",
                    calls=services)


#    metadata: Metadata
#    result: ServerInfo

    #response = ServerinfoGetResponse(metadata=metadata, result=serverinfo)

#    X.result = Result([])

#    results = subprocess.check_output(['bcftools', '--help'])
    # import time
    # serverinfo.text_csv += 'MODIF HWHWH' + str(time.time())
    response = ServerinfoGetResponse(metadata=metadata, result=serverinfo)

    print(response)
    return response
# generated by fastapi-codegen:
#   filename:  PlantBreedingAPI-BrAPI-Genotyping-2.0-resolved.yaml
#   timestamp: 2021-03-24T21:00:43+00:00
# Note: The auto-generated code was edited to remove 
#   redundancies and errors, and add examples.
#   See modelgen_utils for details.

from __future__ import annotations

from typing import List, Optional, Union

from fastapi import FastAPI, Query
from pydantic import constr

# To keep each module independent we are going to use the router 
# as a replacement for the app
from fastapi import APIRouter
router = APIRouter(
    tags = ["genotyping"]
)
app = router

# from brapi_v2.core.models import (
from .. core.models import (
    AdditionalInfo, 
    Metadata,
    IndexPagination,
    Field202AcceptedSearchResponse,
    # Field202AcceptedSearchResponseResult,
    WSMIMEDataTypes,
)

from .models import (
    CallSetResponse,
    CallSetsListResponse,
    CallSetsSearchRequest,
    CallsListResponse,
    CallsSearchRequest,
    # Field202AcceptedSearchResponse,
    GenomeMapListResponse,
    GenomeMapSingleResponse,
    LinkageGroupListResponse,
    MarkerPositionListResponse,
    MarkerPositionSearchRequest,
    ReferenceBasesResponse,
    ReferenceSetsListResponse,
    ReferenceSetsSearchRequest,
    ReferenceSetsSingleResponse,
    ReferenceSingleResponse,
    ReferencesListResponse,
    ReferencesSearchRequest,
    SampleListResponse,
    SampleNewRequest,
    SampleSearchRequest,
    SampleSingleResponse,
    VariantSetResponse,
    VariantSetsExtractRequest,
    VariantSetsListResponse,
    VariantSetsSearchRequest,
    VariantSingleResponse,
    VariantsListResponse,
    VariantsSearchRequest,
    VendorOrderListResponse,
    VendorOrderStatusResponse,
    VendorOrderSubmissionRequest,
    VendorOrderSubmissionSingleResponse,
    VendorPlateListResponse,
    VendorPlateSubmissionIdSingleResponse,
    VendorPlateSubmissionRequest,
    VendorPlateSubmissionSingleResponse,
    VendorResultFileListResponse,
    VendorSpecificationSingleResponse,
)


@app.get('/calls', response_model=CallsListResponse)
def get_calls(
    call_set_db_id: Optional[str] = Query(None, alias='callSetDbId'),
    variant_db_id: Optional[str] = Query(None, alias='variantDbId'),
    variant_set_db_id: Optional[str] = Query(None, alias='variantSetDbId'),
    expand_homozygotes: Optional[bool] = Query(None, alias='expandHomozygotes'),
    unknown_string: Optional[str] = Query(None, alias='unknownString'),
    sep_phased: Optional[str] = Query(None, alias='sepPhased'),
    sep_unphased: Optional[str] = Query(None, alias='sepUnphased'),
    page_token: Optional[str] = Query(None, alias='pageToken'),
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> CallsListResponse:
    """
    Gets a filtered list of `Calls`
    """
    pass


@app.get('/callsets', response_model=CallSetsListResponse)
def get_callsets(
    call_set_db_id: Optional[str] = Query(None, alias='callSetDbId'),
    call_set_name: Optional[str] = Query(None, alias='callSetName'),
    variant_set_db_id: Optional[str] = Query(None, alias='variantSetDbId'),
    sample_db_id: Optional[str] = Query(None, alias='sampleDbId'),
    germplasm_db_id: Optional[str] = Query(None, alias='germplasmDbId'),
    page: Optional[int] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> CallSetsListResponse:
    """
    Gets a filtered list of `CallSet` JSON objects.
    """
    pass


@app.get('/callsets/{call_set_db_id}', response_model=CallSetResponse)
def get_callsets_call_set_db_id(
    call_set_db_id: str = Query(..., alias='callSetDbId'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> CallSetResponse:
    """
    Gets a `CallSet` by ID.
    """
    pass


@app.get('/callsets/{call_set_db_id}/calls', response_model=CallsListResponse)
def get_callsets_call_set_db_id_calls(
    call_set_db_id: str = Query(..., alias='callSetDbId'),
    expand_homozygotes: Optional[bool] = Query(None, alias='expandHomozygotes'),
    unknown_string: Optional[str] = Query(None, alias='unknownString'),
    sep_phased: Optional[str] = Query(None, alias='sepPhased'),
    sep_unphased: Optional[str] = Query(None, alias='sepUnphased'),
    page_token: Optional[str] = Query(None, alias='pageToken'),
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> CallsListResponse:
    """
    Gets a list of `Calls` associated with a `CallSet`.
    """
    pass


@app.get('/maps', response_model=GenomeMapListResponse)
def get_maps(
    common_crop_name: Optional[str] = Query(None, alias='commonCropName'),
    map_db_id: Optional[str] = Query(None, alias='mapDbId'),
    map_p_u_i: Optional[str] = Query(None, alias='mapPUI'),
    scientific_name: Optional[str] = Query(None, alias='scientificName'),
    type: Optional[str] = None,
    program_db_id: Optional[str] = Query(None, alias='programDbId'),
    trial_db_id: Optional[str] = Query(None, alias='trialDbId'),
    study_db_id: Optional[str] = Query(None, alias='studyDbId'),
    page: Optional[int] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> GenomeMapListResponse:
    """
    Get the Genomic Maps
    """
    pass


@app.get('/maps/{map_db_id}', response_model=GenomeMapSingleResponse)
def get_maps_map_db_id(
    map_db_id: str = Query(..., alias='mapDbId'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> GenomeMapSingleResponse:
    """
    Get the details of a specific Genomic Map
    """
    pass


@app.get('/maps/{map_db_id}/linkagegroups', response_model=LinkageGroupListResponse)
def get_maps_map_db_id_linkagegroups(
    map_db_id: str = Query(..., alias='mapDbId'),
    page: Optional[int] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> LinkageGroupListResponse:
    """
    Get the Linkage Groups of a specific Genomic Map
    """
    pass


@app.get('/markerpositions', response_model=MarkerPositionListResponse)
def get_markerpositions(
    map_db_id: Optional[str] = Query(None, alias='mapDbId'),
    linkage_group_name: Optional[str] = Query(None, alias='linkageGroupName'),
    variant_db_id: Optional[str] = Query(None, alias='variantDbId'),
    min_position: Optional[int] = Query(None, alias='minPosition'),
    max_position: Optional[int] = Query(None, alias='maxPosition'),
    page: Optional[int] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> MarkerPositionListResponse:
    """
    Get marker position info
    """
    pass


@app.get('/references', response_model=ReferencesListResponse)
def get_references(
    reference_db_id: Optional[str] = Query(None, alias='referenceDbId'),
    reference_set_db_id: Optional[str] = Query(None, alias='referenceSetDbId'),
    accession: Optional[str] = None,
    md5checksum: Optional[str] = None,
    is_derived: Optional[bool] = Query(None, alias='isDerived'),
    min_length: Optional[int] = Query(None, alias='minLength'),
    max_length: Optional[int] = Query(None, alias='maxLength'),
    page: Optional[int] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> ReferencesListResponse:
    """
    Gets a filtered list of `Reference` objects.
    """
    pass


@app.get('/references/{reference_db_id}', response_model=ReferenceSingleResponse)
def get_references_reference_db_id(
    reference_db_id: str = Query(..., alias='referenceDbId'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> ReferenceSingleResponse:
    """
    Gets a `Reference` by ID.
    """
    pass


@app.get('/references/{reference_db_id}/bases', response_model=ReferenceBasesResponse)
def get_references_reference_db_id_bases(
    reference_db_id: str = Query(..., alias='referenceDbId'),
    start: Optional[int] = None,
    end: Optional[int] = None,
    page_token: Optional[str] = Query(None, alias='pageToken'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> ReferenceBasesResponse:
    """
    Lists `Reference` bases by ID and optional range.
    """
    pass


@app.get('/referencesets', response_model=ReferenceSetsListResponse)
def get_referencesets(
    reference_set_db_id: Optional[str] = Query(None, alias='referenceSetDbId'),
    accession: Optional[str] = None,
    assembly_p_u_i: Optional[str] = Query(None, alias='assemblyPUI'),
    md5checksum: Optional[str] = None,
    page: Optional[int] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> ReferenceSetsListResponse:
    """
    Gets a list of `ReferenceSets`.
    """
    pass


@app.get(
    '/referencesets/{reference_set_db_id}', response_model=ReferenceSetsSingleResponse
)
def get_referencesets_reference_set_db_id(
    reference_set_db_id: str = Query(..., alias='referenceSetDbId'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> ReferenceSetsSingleResponse:
    """
    Gets a `ReferenceSet` by ID.
    """
    pass


@app.get('/samples', response_model=SampleListResponse)
def get_samples(
    sample_db_id: Optional[str] = Query(None, alias='sampleDbId'),
    observation_unit_db_id: Optional[str] = Query(None, alias='observationUnitDbId'),
    plate_db_id: Optional[str] = Query(None, alias='plateDbId'),
    germplasm_db_id: Optional[str] = Query(None, alias='germplasmDbId'),
    study_db_id: Optional[str] = Query(None, alias='studyDbId'),
    external_reference_i_d: Optional[str] = Query(None, alias='externalReferenceID'),
    external_reference_source: Optional[str] = Query(
        None, alias='externalReferenceSource'
    ),
    page: Optional[int] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> SampleListResponse:
    """
    Get the Samples
    """

    from .models import SampleListResponseResult, Sample

    # create some additional information to be add to each sample entry
    # as you can see the field is flexible and it can be anything
    additional_info_test = {}
    # additional_info_test["info_tag_1"] = AdditionalInfo(location="Jupiter!",importance="Its dummy, so not much!")
    # additional_info_test["info_tag_2"] = AdditionalInfo(color="blue_green", arbitrary_info="this can be anything")
    additional_info_test["a_planet"] = AdditionalInfo(__root__="Jupiter!")
    additional_info_test["info_tag_1"] = AdditionalInfo(__root__="this can be any string")

    samples = []
    samples.append(Sample(sampleName="dummy sample 1", 
                          sampleDbId="1213234", 
                          additionalInfo=additional_info_test))

    samples.append(Sample(sampleName="dummy sample 2", 
                          sampleDbId="981975", 
                          additionalInfo=additional_info_test))
    # create extra content just for demo...
    for sample_no in range(3, 9):
        sample_id = 1787 * sample_no
        samples.append(Sample(sampleName=f"dummy sample {sample_no}", 
                          sampleDbId=f"{sample_id}", 
                          additionalInfo=additional_info_test))
    
    result = SampleListResponseResult(data=samples)
    # build pagination and metadata objects
    total_count = len(samples)
    pagination = IndexPagination(currentPage = 0, pageSize=1000, 
                                totalCount=total_count, totalPages=1)
    metadata = Metadata(datafiles=[], status=[], pagination=pagination)
    response = SampleListResponse(metadata=metadata, result=result)
    
    return response

@app.post('/samples', response_model=SampleListResponse)
def post_samples(
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: List[SampleNewRequest] = None,
) -> SampleListResponse:
    """
    Add new Samples
    """
    pass


@app.get('/samples/{sample_db_id}', response_model=SampleSingleResponse)
def get_samples_sample_db_id(
    sample_db_id: str = Query(..., alias='sampleDbId'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> SampleSingleResponse:
    """
    Get the details of a specific Sample
    """
    pass


@app.put('/samples/{sample_db_id}', response_model=SampleSingleResponse)
def put_samples_sample_db_id(
    sample_db_id: str = Query(..., alias='sampleDbId'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: SampleNewRequest = None,
) -> SampleSingleResponse:
    """
    Update the details of an existing Sample
    """
    pass


@app.post(
    '/search/calls',
    response_model=Union[CallsListResponse, Field202AcceptedSearchResponse],
)
def post_search_calls(
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: CallsSearchRequest = None,
) -> Union[CallsListResponse, Field202AcceptedSearchResponse]:
    """
    Submit a search request for `Calls`
    """
    pass


@app.get(
    '/search/calls/{search_results_db_id}',
    response_model=Union[CallsListResponse, Field202AcceptedSearchResponse],
)
def get_search_calls_search_results_db_id(
    search_results_db_id: str = Query(..., alias='searchResultsDbId'),
    page_token: Optional[str] = Query(None, alias='pageToken'),
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> Union[CallsListResponse, Field202AcceptedSearchResponse]:
    """
    Returns a filtered list of `Call` JSON objects.
    """
    pass


@app.post(
    '/search/callsets',
    response_model=Union[CallSetsListResponse, Field202AcceptedSearchResponse],
)
def post_search_callsets(
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: CallSetsSearchRequest = None,
) -> Union[CallSetsListResponse, Field202AcceptedSearchResponse]:
    """
    Gets a list of call sets matching the search criteria.
    """
    pass


@app.get(
    '/search/callsets/{search_results_db_id}',
    response_model=Union[CallSetsListResponse, Field202AcceptedSearchResponse],
)
def get_search_callsets_search_results_db_id(
    search_results_db_id: str = Query(..., alias='searchResultsDbId'),
    page: Optional[int] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> Union[CallSetsListResponse, Field202AcceptedSearchResponse]:
    """
    Gets a list of call sets matching the search criteria.
    """
    pass


@app.post(
    '/search/markerpositions',
    response_model=Union[MarkerPositionListResponse, Field202AcceptedSearchResponse],
)
def post_search_markerpositions(
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: MarkerPositionSearchRequest = None,
) -> Union[MarkerPositionListResponse, Field202AcceptedSearchResponse]:
    """
    Get marker position info
    """
    pass


@app.get(
    '/search/markerpositions/{search_results_db_id}',
    response_model=Union[MarkerPositionListResponse, Field202AcceptedSearchResponse],
)
def get_search_markerpositions_search_results_db_id(
    search_results_db_id: str = Query(..., alias='searchResultsDbId'),
    page: Optional[int] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> Union[MarkerPositionListResponse, Field202AcceptedSearchResponse]:
    """
    Get marker position info
    """
    pass


@app.post(
    '/search/references',
    response_model=Union[ReferencesListResponse, Field202AcceptedSearchResponse],
)
def post_search_references(
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: ReferencesSearchRequest = None,
) -> Union[ReferencesListResponse, Field202AcceptedSearchResponse]:
    """
    Gets a list of `Reference` matching the search criteria.
    """
    pass


@app.get(
    '/search/references/{search_results_db_id}',
    response_model=Union[ReferencesListResponse, Field202AcceptedSearchResponse],
)
def get_search_references_search_results_db_id(
    search_results_db_id: str = Query(..., alias='searchResultsDbId'),
    page: Optional[int] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> Union[ReferencesListResponse, Field202AcceptedSearchResponse]:
    """
    Gets a list of `Reference` matching the search criteria.
    """
    pass


@app.post(
    '/search/referencesets',
    response_model=Union[ReferenceSetsListResponse, Field202AcceptedSearchResponse],
)
def post_search_referencesets(
    body: ReferenceSetsSearchRequest,
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> Union[ReferenceSetsListResponse, Field202AcceptedSearchResponse]:
    """
    Gets a list of `ReferenceSet` matching the search criteria.
    """
    pass


@app.get(
    '/search/referencesets/{search_results_db_id}',
    response_model=Union[ReferenceSetsListResponse, Field202AcceptedSearchResponse],
)
def get_search_referencesets_search_results_db_id(
    search_results_db_id: str = Query(..., alias='searchResultsDbId'),
    page: Optional[int] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> Union[ReferenceSetsListResponse, Field202AcceptedSearchResponse]:
    """
    Gets a list of `ReferenceSet` matching the search criteria.
    """
    pass


@app.post(
    '/search/samples',
    response_model=Union[SampleListResponse, Field202AcceptedSearchResponse],
)
def post_search_samples(
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: SampleSearchRequest = None,
) -> Union[SampleListResponse, Field202AcceptedSearchResponse]:
    """
    Submit a search request for Samples
    """
    pass


@app.get(
    '/search/samples/{search_results_db_id}',
    response_model=Union[SampleListResponse, Field202AcceptedSearchResponse],
)
def get_search_samples_search_results_db_id(
    search_results_db_id: str = Query(..., alias='searchResultsDbId'),
    page: Optional[int] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> Union[SampleListResponse, Field202AcceptedSearchResponse]:
    """
    Get the results of a Samples search request
    """
    pass


@app.post(
    '/search/variants',
    response_model=Union[VariantsListResponse, Field202AcceptedSearchResponse],
)
def post_search_variants(
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: VariantsSearchRequest = None,
) -> Union[VariantsListResponse, Field202AcceptedSearchResponse]:
    """
    Gets a list of `Variant` matching the search criteria.
    """
    pass


@app.get(
    '/search/variants/{search_results_db_id}',
    response_model=Union[VariantsListResponse, Field202AcceptedSearchResponse],
)
def get_search_variants_search_results_db_id(
    search_results_db_id: str = Query(..., alias='searchResultsDbId'),
    page_token: Optional[str] = Query(None, alias='pageToken'),
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> Union[VariantsListResponse, Field202AcceptedSearchResponse]:
    """
    Gets a list of `Variant` matching the search criteria.
    """
    pass


@app.post(
    '/search/variantsets',
    response_model=Union[VariantSetsListResponse, Field202AcceptedSearchResponse],
)
def post_search_variantsets(
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: VariantSetsSearchRequest = None,
) -> Union[VariantSetsListResponse, Field202AcceptedSearchResponse]:
    """
    Gets a list of `VariantSet` matching the search criteria.
    """
    pass


@app.get(
    '/search/variantsets/{search_results_db_id}',
    response_model=Union[VariantSetsListResponse, Field202AcceptedSearchResponse],
)
def get_search_variantsets_search_results_db_id(
    search_results_db_id: str = Query(..., alias='searchResultsDbId'),
    page: Optional[int] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> Union[VariantSetsListResponse, Field202AcceptedSearchResponse]:
    """
    Gets a list of `VariantSet` matching the search criteria.
    """
    pass


@app.get('/variants', response_model=VariantsListResponse)
def get_variants(
    variant_db_id: Optional[str] = Query(None, alias='variantDbId'),
    variant_set_db_id: Optional[str] = Query(None, alias='variantSetDbId'),
    page_token: Optional[str] = Query(None, alias='pageToken'),
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> VariantsListResponse:
    """
    Gets a filtered list of `Variants`.
    """
    pass


@app.get('/variants/{variant_db_id}', response_model=VariantSingleResponse)
def get_variants_variant_db_id(
    variant_db_id: str = Query(..., alias='variantDbId'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> VariantSingleResponse:
    """
    Gets a `Variant` by ID.
    """
    pass


@app.get('/variants/{variant_db_id}/calls', response_model=CallsListResponse)
def get_variants_variant_db_id_calls(
    variant_db_id: str = Query(..., alias='variantDbId'),
    expand_homozygotes: Optional[bool] = Query(None, alias='expandHomozygotes'),
    unknown_string: Optional[str] = Query(None, alias='unknownString'),
    sep_phased: Optional[str] = Query(None, alias='sepPhased'),
    sep_unphased: Optional[str] = Query(None, alias='sepUnphased'),
    page_token: Optional[str] = Query(None, alias='pageToken'),
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> CallsListResponse:
    """
    Gets a list of `Calls` associated with a `Variant`.
    """
    pass


@app.get('/variantsets', response_model=VariantSetsListResponse)
def get_variantsets(
    variant_set_db_id: Optional[str] = Query(None, alias='variantSetDbId'),
    variant_db_id: Optional[str] = Query(None, alias='variantDbId'),
    call_set_db_id: Optional[str] = Query(None, alias='callSetDbId'),
    study_db_id: Optional[str] = Query(None, alias='studyDbId'),
    study_name: Optional[str] = Query(None, alias='studyName'),
    page: Optional[int] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> VariantSetsListResponse:
    """
    Gets a filtered list of `VariantSets`.
    """
    pass


@app.post('/variantsets/extract', response_model=VariantSetResponse)
def post_variantsets_extract(
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: VariantSetsExtractRequest = None,
) -> VariantSetResponse:
    """
    Create new `VariantSet` based on search results
    """
    pass


@app.get('/variantsets/{variant_set_db_id}', response_model=VariantSetResponse)
def get_variantsets_variant_set_db_id(
    variant_set_db_id: str = Query(..., alias='variantSetDbId'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> VariantSetResponse:
    """
    Gets a `VariantSet` by ID.
    """
    pass


@app.get('/variantsets/{variant_set_db_id}/calls', response_model=CallsListResponse)
def get_variantsets_variant_set_db_id_calls(
    variant_set_db_id: str = Query(..., alias='variantSetDbId'),
    expand_homozygotes: Optional[bool] = Query(None, alias='expandHomozygotes'),
    unknown_string: Optional[str] = Query(None, alias='unknownString'),
    sep_phased: Optional[str] = Query(None, alias='sepPhased'),
    sep_unphased: Optional[str] = Query(None, alias='sepUnphased'),
    page_token: Optional[str] = Query(None, alias='pageToken'),
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> CallsListResponse:
    """
    Gets a list of `Calls` associated with a `VariantSet`.
    """
    pass


@app.get(
    '/variantsets/{variant_set_db_id}/callsets', response_model=CallSetsListResponse
)
def get_variantsets_variant_set_db_id_callsets(
    call_set_db_id: Optional[str] = Query(None, alias='callSetDbId'),
    call_set_name: Optional[str] = Query(None, alias='callSetName'),
    variant_set_db_id: str = Query(..., alias='variantSetDbId'),
    page: Optional[int] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> CallSetsListResponse:
    """
    Gets a list of `CallSets` associated with a `VariantSet`.
    """
    pass


@app.get(
    '/variantsets/{variant_set_db_id}/variants', response_model=VariantsListResponse
)
def get_variantsets_variant_set_db_id_variants(
    variant_db_id: Optional[str] = Query(None, alias='variantDbId'),
    variant_set_db_id: str = Query(..., alias='variantSetDbId'),
    page_token: Optional[str] = Query(None, alias='pageToken'),
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> VariantsListResponse:
    """
    Gets a `Variants` for a given `VariantSet`.
    """
    pass


@app.get('/vendor/orders', response_model=VendorOrderListResponse)
def get_vendor_orders(
    order_id: Optional[str] = Query(None, alias='orderId'),
    submission_id: Optional[str] = Query(None, alias='submissionId'),
    page: Optional[int] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> VendorOrderListResponse:
    """
    List current available orders
    """
    pass


@app.post('/vendor/orders', response_model=VendorOrderSubmissionSingleResponse)
def post_vendor_orders(
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: VendorOrderSubmissionRequest = None,
) -> VendorOrderSubmissionSingleResponse:
    """
    Submit New Order
    """
    pass


@app.get('/vendor/orders/{order_id}/plates', response_model=VendorPlateListResponse)
def get_vendor_orders_order_id_plates(
    order_id: str = Query(..., alias='orderId'),
    page: Optional[int] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> VendorPlateListResponse:
    """
    Get the Plates for a specific Order
    """
    pass


@app.get(
    '/vendor/orders/{order_id}/results', response_model=VendorResultFileListResponse
)
def get_vendor_orders_order_id_results(
    order_id: str = Query(..., alias='orderId'),
    page: Optional[int] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> VendorResultFileListResponse:
    """
    Get the results of a specific Order
    """
    pass


@app.get('/vendor/orders/{order_id}/status', response_model=VendorOrderStatusResponse)
def get_vendor_orders_order_id_status(
    order_id: str = Query(..., alias='orderId'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> VendorOrderStatusResponse:
    """
    Get the status of a specific Order
    """
    pass


@app.post('/vendor/plates', response_model=VendorPlateSubmissionIdSingleResponse)
def post_vendor_plates(
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: VendorPlateSubmissionRequest = None,
) -> VendorPlateSubmissionIdSingleResponse:
    """
    Submit a new set of Sample data
    """
    pass


@app.get(
    '/vendor/plates/{submission_id}', response_model=VendorPlateSubmissionSingleResponse
)
def get_vendor_plates_submission_id(
    submission_id: str = Query(..., alias='submissionId'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> VendorPlateSubmissionSingleResponse:
    """
    Get the data for a submitted set of plates
    """
    pass


@app.get('/vendor/specifications', response_model=VendorSpecificationSingleResponse)
def get_vendor_specifications(
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    )
) -> VendorSpecificationSingleResponse:
    """
    Get the Vendor Specifications
    """
    pass

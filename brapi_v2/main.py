from fastapi import FastAPI

app = FastAPI(
    #root_path="/brapi/v2",
    description='The Breeding API (BrAPI) is a Standardized REST ful Web Service API Specification for communicating Plant Breeding Data. BrAPI allows for easy data sharing between databases and tools involved in plant breeding.\n<div class="brapi-section">\n<h2 class="brapi-section-title">General Reference Documentation</h2>\n<div class="gen-info-link"><a href="https://github.com/plantbreeding/API/blob/master/Specification/GeneralInfo/URL_Structure.md">URL Structure</a></div>\n<div class="gen-info-link"><a href="https://github.com/plantbreeding/API/blob/master/Specification/GeneralInfo/Response_Structure.md">Response Structure</a></div>\n<div class="gen-info-link"><a href="https://github.com/plantbreeding/API/blob/master/Specification/GeneralInfo/Date_Time_Encoding.md">Date/Time Encoding</a></div>\n<div class="gen-info-link"><a href="https://github.com/plantbreeding/API/blob/master/Specification/GeneralInfo/Location_Encoding.md">Location Encoding</a></div>\n<div class="gen-info-link"><a href="https://github.com/plantbreeding/API/blob/master/Specification/GeneralInfo/Error_Handling.md">Error Handling</a></div>\n<div class="gen-info-link"><a href="https://github.com/plantbreeding/API/blob/master/Specification/GeneralInfo/Search_Services.md">Search Services</a></div>\n</div>\n\n<div class="current-brapi-section brapi-section">\n<h2 class="brapi-section-title">BrAPI Core</h2>\n<div class="brapi-section-description">The BrAPI Core module contains high level entities used for organization and management. This includes Programs, Trials, Studies, Locations, People, and Lists</div>\n<div class="version-number">V2.0</div>\n<div class="link-btn"><a href="https://github.com/plantbreeding/API/tree/master/Specification/BrAPI-Core">GitHub</a></div>\n<div class="link-btn"><a href="https://app.swaggerhub.com/apis/PlantBreedingAPI/BrAPI-Core">SwaggerHub</a></div>\n<div class="link-btn"><a href="https://brapicore.docs.apiary.io">Apiary</a></div>\n<div class="stop-float"></div>\n</div>\n\n<div class="brapi-section">\n<h2 class="brapi-section-title">BrAPI Phenotyping</h2>\n<div class="brapi-section-description">The BrAPI Phenotyping module contains entities related to phenotypic observations. This includes Observation Units, Observations, Observation Variables, Traits, Scales, Methods, and Images</div>\n<div class="version-number">V2.0</div>\n<div class="link-btn"><a href="https://github.com/plantbreeding/API/tree/master/Specification/BrAPI-Phenotyping">GitHub</a></div>\n<div class="link-btn"><a href="https://app.swaggerhub.com/apis/PlantBreedingAPI/BrAPI-Phenotyping">SwaggerHub</a></div>\n<div class="link-btn"><a href="https://brapiphenotyping.docs.apiary.io">Apiary</a></div>\n<div class="stop-float"></div>\n</div>\n\n<div class="brapi-section">\n<h2 class="brapi-section-title">BrAPI Genotyping</h2>\n<div class="brapi-section-description">The BrAPI Genotyping module contains entities related to genotyping analysis. This includes Samples, Markers, Variant Sets, Variants, Call Sets, Calls, References, Reads, and Vendor Orders</div>\n<div class="version-number">V2.0</div>\n<div class="link-btn"><a href="https://github.com/plantbreeding/API/tree/master/Specification/BrAPI-Genotyping">GitHub</a></div>\n<div class="link-btn"><a href="https://app.swaggerhub.com/apis/PlantBreedingAPI/BrAPI-Genotyping">SwaggerHub</a></div>\n<div class="link-btn"><a href="https://brapigenotyping.docs.apiary.io">Apiary</a></div>\n<div class="stop-float"></div>\n</div>\n\n<div class="brapi-section">\n<h2 class="brapi-section-title">BrAPI Germplasm</h2>\n<div class="brapi-section-description">The BrAPI Germplasm module contains entities related to germplasm management. This includes Germplasm, Germplasm Attributes, Seed Lots, Crosses, Pedigree, and Progeny</div>\n<div class="version-number">V2.0</div>\n<div class="link-btn"><a href="https://github.com/plantbreeding/API/tree/master/Specification/BrAPI-Germplasm">GitHub</a></div>\n<div class="link-btn"><a href="https://app.swaggerhub.com/apis/PlantBreedingAPI/BrAPI-Germplasm">SwaggerHub</a></div>\n<div class="link-btn"><a href="https://brapigermplasm.docs.apiary.io">Apiary</a></div>\n<div class="stop-float"></div>\n</div>\n\n<style>\n.link-btn{\nfloat: left; \nmargin: 2px 10px 0 0; \npadding: 0 5px; \nborder-radius: 5px; \nbackground-color: #ddd;\n}\n.stop-float{\n  clear: both;\n}\n.version-number{\n  float: left; \n  margin: 5px 10px 0 5px;\n}\n.brapi-section-title{\n  margin: 0 10px 0 0;\n  font-size: 20px;\n}\n.current-brapi-section{\n  font-weight: bolder;\n  border-radius: 5px; \n  background-color: #ddd;\n}\n.brapi-section{\n  padding: 5px 5px; \n}\n.brapi-section-description{\n  margin: 5px 0 0 5px;\n}\n</style>',
    title='BrAPI-Core',
    version='2.0',
)

# See FastAPI doc's on how enable CORS (Cross-Origin Resource Sharing) 
# https://fastapi.tiangolo.com/tutorial/cors

# from fastapi.middleware.cors import CORSMiddleware
# origins = [
#     "http://localhost",
#     "http://localhost:8080",
#     "http://localhost:9000",
# ]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


#from . import views as core#, users
from . import core
from . import genotyping
from . import germplasm
from . import phenotyping


app.include_router(core.views.router, prefix='/brapi/v2')
app.include_router(genotyping.views.router, prefix='/brapi/v2')
app.include_router(germplasm.views.router, prefix='/brapi/v2')
app.include_router(phenotyping.views.router, prefix='/brapi/v2')

@app.get("/", tags=["main_root"])
async def root():
    return {"BrAPI": "V2.0"}


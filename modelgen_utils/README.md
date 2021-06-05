# FastAPI Model generation

The resolved openapi models in `brapi_openapi_models` were used to generate the Python Pydanic models (for more details check the documentation in `brapi_openapi_models`). The resulting models are in the `resolved` directory.

The models from `resolved` are the basis for what was used to build the models and views present in `brapi_v2`.
In the event of a new release of BrAPI this process has to be runned again.

# Important

The code here is provided as a way of documenting how the models were generated and what needs to be done in a new BrAPI release. Do *NOT* use these models to overwrite `brapi_v2`, specially if you don't know what you are doing.

# Note on Model duplicates

The FastAPI-code-generator created some duplicated classes definitions across each module. They can be found by looking for "class" instance definitions. The [find_duplicate_classes] script(find_duplicate_classes.sh) will help in finding these duplicates so they can be edited.
Example usage:
```sh
modelgen_utils/find_duplicate_classes.sh brapi_v2
```
Output content
instance_count | class_name
------------ | -------------
   4 | AdditionalInfo(BaseModel):
   4 | BasePagination(BaseModel):
   ... | ... omitted ...
   2 | Season(BaseModel):
   1 | AcquisitionSourceCode(Enum):
   1 | Analysis(BaseModel):

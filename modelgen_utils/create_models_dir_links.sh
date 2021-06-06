#!/bin/bash

# Use to link only the BrAPI models. 
# You might not need to run this, since already a models directory is provided.
# This is useful when 
#   1. a new model set is created
#   2. a shallow copy/link of the models is needed in a new path
# modify $MODELS_ROOT if needed

MODELS_ROOT=models

# This assumes that brapi_v2 is in the path were the script is running
if [[ ! -d "brapi_v2" ]]
then
   echo "The [brapi_v2] directory is NOT present!"
   echo "This script assumes that [brapi_v2] is in the current dir."
   exit 0
else
   echo "brapi_v2 found will link models to $MODELS_ROOT"
fi


mkdir -pv ${MODELS_ROOT}/brapi_v2
cd ${MODELS_ROOT}/brapi_v2

ls -la
cp -v ../../brapi_v2/__init__.py ./
for module in core genotyping germplasm phenotyping;
do
   mkdir -v ${module}
   cd ${module}
   ln -sv ../../../brapi_v2/${module}/models.py ./
   echo "from . import models" >> __init__.py
   cd ..
done

#for x in *;do pushd $x; ln -s ../../../brapi_v2/${x}/models.py ./;popd;done


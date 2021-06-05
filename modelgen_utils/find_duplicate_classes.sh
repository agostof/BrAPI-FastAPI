#!/bin/bash

# Utility script to find and enumerate which classes are defined more than once across modules. It will produce class def counts and names as follows:
#   4  AdditionalInfo(BaseModel):
#   2  Season(BaseModel):

#  usage example:
# ./find_duplicate_classes.sh ../brapi_v2

BRAPIDIR=$1
cd $BRAPIDIR
grep -nr "^class"  ./ | cut -d " " -f2 | sort | uniq -c | sort -k1,1nr


# BrAPI-Models

# Pydantic models

The resolved openapi models here were used to generate the Python Pydantic models.
In some instances the OpenApi models were modified due to parsing errors with the fastapi-code-generator (and datamodel-code-generator its dependency).

Those will have a "_MOD.yaml" suffix to indiate this.

Models were generated as follows:
fastapi-code-generator --input ${RESOLVED_MODEL} --output api_models/

## Note
Note: FastAPI and datamodel-code-generator's might have change, this conversion could break with newer releases of these tools. 

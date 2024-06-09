# Use bash (needed, for example, for the process substitutions)
SHELL := /bin/bash

# Options:
# --additional-imports "datetime.datetime": Default was `AwareDatetime`, but input should have timezone info (e.g., `VaccinationData.referencedate` field)
# For Pydantic v1, --use-annotated: To avoid error "TypeError: Forward references must evaluate to types."
generate-datamodels:
	datamodel-codegen --input ../../docs/openapi-data-gov-gr.yaml --input-file-type openapi --disable-timestamp --use-double-quotes --use-annotated --additional-imports "datetime.datetime" --output-model-type pydantic.BaseModel --output ./datagovgr_datamodels/pydantic_v1/models.py
	datamodel-codegen --input ../../docs/openapi-data-gov-gr.yaml --input-file-type openapi --disable-timestamp --use-double-quotes --use-annotated --additional-imports "datetime.datetime" --output-model-type pydantic_v2.BaseModel --output ./datagovgr_datamodels/pydantic_v2/models.py

check-models: generate-datamodels
	git diff --exit-code || { echo "Update the datamodels by running 'make -C datamodels/python generate-datamodels' from the base directory."; exit 1; }

check-api-version:
	diff <(cat ./datagovgr_datamodels/API-DOC-VERSION | xargs echo) <(cat ../../API-DOC-VERSION | xargs echo) || { echo "API-DOC-VERSION files do not match."; exit 1; }

check-ci: check-models check-api-version

update-reqs:
	poetry update

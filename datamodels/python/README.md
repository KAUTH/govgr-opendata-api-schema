# datagovgr-datamodels
Datamodels created for handling the data from the https://data.gov.gr API.

The models are automatically generated from the [unofficial API documentation](https://github.com/KAUTH/govgr-opendata-api-schema/blob/main/docs/openapi-data-gov-gr.yaml),
using the [`datamodel-code-generator`](https://github.com/koxudaxi/datamodel-code-generator).

For more information regarding the related project, see https://github.com/KAUTH/govgr-opendata-api-schema.

## Supported datamodels
- [pydantic_v1](https://docs.pydantic.dev/1.10/).BaseModel
- [pydantic_v2](https://docs.pydantic.dev/2.0/).BaseModel

_Note: At this moment, the package focuses on the datamodels of the responses._

## Quick Installation
To install `datagovgr-datamodels`:

- For `pydantic` models:
```bash
$ pip install datagovgr-datamodels[pydantic]
```

## Example Usage

- `$ python3 examples/pydantic_v1_models.py`

## Changelog
Changes to the datamodels are accompanied by a version update, documented in
https://github.com/KAUTH/govgr-opendata-api-schema/blob/main/datamodels/python/CHANGELOG.md.

## License
[MIT License](https://github.com/KAUTH/govgr-opendata-api-schema/blob/main/datamodels/python/LICENSE)

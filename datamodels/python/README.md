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

### Pydantic models
- To test querying the API and using the `pydantic` data models, provide a valid token and run:  
`$ python3 examples/pydantic_v1_models.py`

- Example directly using `pydantic` v1 models:
```python
from datagovgr_datamodels.pydantic_v1 import VaccinationData


data = {
    'area': 'ΑΝΑΤΟΛΙΚΗΣ ΑΤΤΙΚΗΣ',
    'areaid': 901,
    'dailydose1': 45,
    'dailydose2': 0,
    'dailydose3': 0,
    'daydiff': 0,
    'daytotal': 45,
    'referencedate': '2021-01-01T00:00:00',
    'totaldistinctpersons': 276,
    'totaldose1': 276,
    'totaldose2': 0,
    'totaldose3': 0,
    'totalvaccinations': 276
}

vaccination = VaccinationData.parse_obj(data)
print(
    f"Total vaccinations in '{vaccination.area}' "
    f"for {vaccination.referencedate.date()}: "
    f"{vaccination.totalvaccinations}."
)
```

- Example directly using `pydantic` v2 models:
```python
from datagovgr_datamodels.pydantic_v2 import VaccinationData


data = {
    'area': 'ΑΝΑΤΟΛΙΚΗΣ ΑΤΤΙΚΗΣ',
    'areaid': 901,
    'dailydose1': 45,
    'dailydose2': 0,
    'dailydose3': 0,
    'daydiff': 0,
    'daytotal': 45,
    'referencedate': '2021-01-01T00:00:00',
    'totaldistinctpersons': 276,
    'totaldose1': 276,
    'totaldose2': 0,
    'totaldose3': 0,
    'totalvaccinations': 276
}

vaccination = VaccinationData.model_validate(data)
print(
    f"Total vaccinations in '{vaccination.area}' "
    f"for {vaccination.referencedate.date()}: "
    f"{vaccination.totalvaccinations}."
)
```

## Changelog
Changes to the datamodels are accompanied by a version update, documented in
https://github.com/KAUTH/govgr-opendata-api-schema/blob/main/datamodels/python/CHANGELOG.md.

## License
[MIT License](https://github.com/KAUTH/govgr-opendata-api-schema/blob/main/datamodels/python/LICENSE)

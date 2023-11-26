# govgr-opendata-api-schema
This repository is an unofficial API documentation for the https://data.gov.gr API.

## What is data.gov.gr?
According to https://repository.data.gov.gr/about:

> data.gov.gr is the central catalog of public data that provides access to databases of Greek government agencies. The purpose of data.gov.gr is to increase access to high-value, machine-readable datasets by providing unified services for cataloging, indexing, storage, search, and availability of public sector data and information, as well as online services to citizens and third-party information systems.

## API Documentation
The API documentation was created based on the [OpenAPI Specification](https://swagger.io/specification/) and the OpenAPI Document can be found [here](https://github.com/KAUTH/govgr-opendata-api-schema/blob/main/openapi-data-gov-gr.yaml).

The open data referenced are published by central government, local authorities, and public bodies to help build products and services, and you can find them at https://data.gov.gr.

## Known Limitations
- `date_from` and `date_to` parameters support up to a specific, currently unknown, date range before getting a relevant
error (status code 400, `"Date/Time window exceeded please select a shorter period or break your requests to multiple ones"`)
- `date_from` and `date_to` parameters should have values that adhere to the first date of collection of the data and the
the latest date collected accordingly, which is not part of the documentation
- Error responses not documented

## Changelog
https://github.com/KAUTH/govgr-opendata-api-schema/blob/main/API-DOC-CHANGELOG.md

## Contributing
You can always submit a PR if you want to suggest improvements or fix issues.

Check out the open issues at https://github.com/KAUTH/govgr-opendata-api-schema/issues.
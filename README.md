# Unofficial data.gov.gr API Schema
This repository is an unofficial API documentation for the https://data.gov.gr API.

## What is data.gov.gr?
According to [https://repository.data.gov.gr/about](https://repository.data.gov.gr/about):

> data.gov.gr is the central catalog of public data that provides access to databases of Greek government agencies. The purpose of data.gov.gr is to increase access to high-value, machine-readable datasets by providing unified services for cataloging, indexing, storage, search, and availability of public sector data and information, as well as online services to citizens and third-party information systems.

## API Documentation
The API documentation was created based on the [OpenAPI Specification](https://swagger.io/specification/) and the OpenAPI Document can be found [here](https://github.com/KAUTH/govgr-opendata-api-schema/blob/main/docs/openapi-data-gov-gr.yaml).

### Source of Data
The open data referenced are published by central government, local authorities, and public bodies to help build products and services, and you can find them at https://data.gov.gr.

### Language
The API documentation (tags, summaries, descriptions, etc.) is written in English to provide easy access to people outside of Greece. When possible, the texts have been translated directly from data.gov.gr, otherwise they have been written by
the repository contributors. In the future, it is possible to additionally support the documentation written in the Greek language.

Regarding the example values, they have remained in their original format (in most cases Greek), as the data is expected.

### Known Limitations
- `date_from` and `date_to` parameters support up to a specific, currently unknown, date range before getting a relevant
error (status code 400, `"Date/Time window exceeded please select a shorter period or break your requests to multiple ones"`)
- `date_from` and `date_to` parameters should have values that adhere to the first date of collection of the data and the
the latest date collected accordingly, which is not part of the documentation
- Error responses are not documented
- The documentation is currently manually maintained. Feel free to open an [issue](https://github.com/KAUTH/govgr-opendata-api-schema/issues)
or submit a [PR](https://github.com/KAUTH/govgr-opendata-api-schema/pulls) if you notice discrepancies, missing items, or any other issues.

### Changelog
Changes to the [API documentation](https://github.com/KAUTH/govgr-opendata-api-schema/blob/main/docs/openapi-data-gov-gr.yaml)
are accompanied by a version update, documented in
https://github.com/KAUTH/govgr-opendata-api-schema/blob/main/API-DOC-CHANGELOG.md.

## Why?
Providing API documentation that follows a popular specification, such as OpenAPI, helps developers and systems learn the
capabilities of the data.gov.gr API service, without needing extensive discovery interactions with it, since currently there
is no official documentation.

As mentioned in https://swagger.io/specification/:
> An OpenAPI definition can then be used by documentation generation tools to display the API, code generation tools to generate servers and clients in various programming languages, testing tools, and many other use cases.

## Projects
Below is a list of projects that are using our API documentation:
- [OpenData Explorer GPT](https://chat.openai.com/g/g-1ZBK8qUZ1-opendata-explorer): Access and understand data published by the central government, local authorities, and public bodies.

If you want to add your project, open a PR [here](https://github.com/KAUTH/govgr-opendata-api-schema/pulls)!

## License
[MIT License](https://github.com/KAUTH/govgr-opendata-api-schema/blob/main/LICENSE)

## Contributing
You can always submit a PR if you want to suggest improvements or fix issues.

Check out the open issues at https://github.com/KAUTH/govgr-opendata-api-schema/issues.
# ai-core-api-client
This API gives you the ability to interact with AISF's neural networks

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0
- Package version: 1.0.0
- Generator version: 7.7.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/AiSaleForce/ai-core-api-client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/AiSaleForce/ai-core-api-client.git`)

Then import the package:
```python
import ai_core_api_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import ai_core_api_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import ai_core_api_client
from ai_core_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ai_core_api_client.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerAuth
configuration.api_key['BearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerAuth'] = 'Bearer'


# Enter a context with an instance of the API client
with ai_core_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ai_core_api_client.AiApi(api_client)
    request = ai_core_api_client.DomainConversationRequest() # DomainConversationRequest | Conversation Request

    try:
        # Generate response from AI model
        api_response = api_instance.conversation_post(request)
        print("The response of AiApi->conversation_post:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AiApi->conversation_post: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to */api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AiApi* | [**conversation_post**](docs/AiApi.md#conversation_post) | **POST** /conversation | Generate response from AI model
*CompanyApi* | [**company_get**](docs/CompanyApi.md#company_get) | **GET** /company | Returns a list of companies
*CompanyApi* | [**company_id_delete**](docs/CompanyApi.md#company_id_delete) | **DELETE** /company/{id} | Delete company from the database
*CompanyApi* | [**company_id_get**](docs/CompanyApi.md#company_id_get) | **GET** /company/{id} | Get company details
*CompanyApi* | [**company_post**](docs/CompanyApi.md#company_post) | **POST** /company | Adds a company to the database


## Documentation For Models

 - [DomainAIFunction](docs/DomainAIFunction.md)
 - [DomainAIFunctionCall](docs/DomainAIFunctionCall.md)
 - [DomainAIFunctionParameterProperty](docs/DomainAIFunctionParameterProperty.md)
 - [DomainAIFunctionParameters](docs/DomainAIFunctionParameters.md)
 - [DomainAIMessage](docs/DomainAIMessage.md)
 - [DomainAITool](docs/DomainAITool.md)
 - [DomainCompany](docs/DomainCompany.md)
 - [DomainCompanyRequest](docs/DomainCompanyRequest.md)
 - [DomainConversationRequest](docs/DomainConversationRequest.md)
 - [DomainConversationResponse](docs/DomainConversationResponse.md)
 - [DomainErrorResponse](docs/DomainErrorResponse.md)
 - [DomainSuccessResponse](docs/DomainSuccessResponse.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="BearerAuth"></a>
### BearerAuth

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

n.tolstov tolnikita556@gmail.com

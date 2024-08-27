# openapi_client.CompanyApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**company_get**](CompanyApi.md#company_get) | **GET** /company | Returns a list of companies
[**company_id_delete**](CompanyApi.md#company_id_delete) | **DELETE** /company/{id} | Delete company from the database
[**company_id_get**](CompanyApi.md#company_id_get) | **GET** /company/{id} | Get company details
[**company_patch**](CompanyApi.md#company_patch) | **PATCH** /company | Update a company in the database
[**company_post**](CompanyApi.md#company_post) | **POST** /company | Adds a company to the database


# **company_get**
> List[DomainCompany] company_get()

Returns a list of companies

This endpoint returns a list of all companies in the database

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.domain_company import DomainCompany
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CompanyApi(api_client)

    try:
        # Returns a list of companies
        api_response = api_instance.company_get()
        print("The response of CompanyApi->company_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyApi->company_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[DomainCompany]**](DomainCompany.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **company_id_delete**
> DomainSuccessResponse company_id_delete(id)

Delete company from the database

This endpoint removes the company from the database.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.domain_success_response import DomainSuccessResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CompanyApi(api_client)
    id = 'id_example' # str | Company ID

    try:
        # Delete company from the database
        api_response = api_instance.company_id_delete(id)
        print("The response of CompanyApi->company_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyApi->company_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Company ID | 

### Return type

[**DomainSuccessResponse**](DomainSuccessResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **company_id_get**
> DomainCompany company_id_get(id)

Get company details

This endpoint returns details of a specific company by its ID in the database.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.domain_company import DomainCompany
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CompanyApi(api_client)
    id = 'id_example' # str | Company ID

    try:
        # Get company details
        api_response = api_instance.company_id_get(id)
        print("The response of CompanyApi->company_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyApi->company_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Company ID | 

### Return type

[**DomainCompany**](DomainCompany.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **company_patch**
> DomainSuccessResponse company_patch(request)

Update a company in the database

This endpoint update a company record in the database.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.domain_company_update_request import DomainCompanyUpdateRequest
from openapi_client.models.domain_success_response import DomainSuccessResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CompanyApi(api_client)
    request = openapi_client.DomainCompanyUpdateRequest() # DomainCompanyUpdateRequest | Company Update Request

    try:
        # Update a company in the database
        api_response = api_instance.company_patch(request)
        print("The response of CompanyApi->company_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyApi->company_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**DomainCompanyUpdateRequest**](DomainCompanyUpdateRequest.md)| Company Update Request | 

### Return type

[**DomainSuccessResponse**](DomainSuccessResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **company_post**
> DomainSuccessResponse company_post(request)

Adds a company to the database

This endpoint creates a new company record in the database.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.domain_company_create_request import DomainCompanyCreateRequest
from openapi_client.models.domain_success_response import DomainSuccessResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CompanyApi(api_client)
    request = openapi_client.DomainCompanyCreateRequest() # DomainCompanyCreateRequest | Company Create Request

    try:
        # Adds a company to the database
        api_response = api_instance.company_post(request)
        print("The response of CompanyApi->company_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyApi->company_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**DomainCompanyCreateRequest**](DomainCompanyCreateRequest.md)| Company Create Request | 

### Return type

[**DomainSuccessResponse**](DomainSuccessResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# openapi_client.GetMeApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_me_get**](GetMeApi.md#get_me_get) | **GET** /get-me | Get company details


# **get_me_get**
> DomainGetMeResponse get_me_get()

Get company details

This endpoint returns details of a specific company by its tokeb in the database.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.domain_get_me_response import DomainGetMeResponse
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
    api_instance = openapi_client.GetMeApi(api_client)

    try:
        # Get company details
        api_response = api_instance.get_me_get()
        print("The response of GetMeApi->get_me_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GetMeApi->get_me_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DomainGetMeResponse**](DomainGetMeResponse.md)

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


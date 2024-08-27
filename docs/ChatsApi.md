# openapi_client.ChatsApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chats_get**](ChatsApi.md#chats_get) | **GET** /chats | Get all client chats of company


# **chats_get**
> DomainGetChatsResponse chats_get(page=page, limit=limit)

Get all client chats of company

This endpoint returns all client chats of company.

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.domain_get_chats_response import DomainGetChatsResponse
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
    api_instance = openapi_client.ChatsApi(api_client)
    page = 56 # int | Page number (optional)
    limit = 56 # int | Limit of chats per page (optional)

    try:
        # Get all client chats of company
        api_response = api_instance.chats_get(page=page, limit=limit)
        print("The response of ChatsApi->chats_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->chats_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] 
 **limit** | **int**| Limit of chats per page | [optional] 

### Return type

[**DomainGetChatsResponse**](DomainGetChatsResponse.md)

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


# ai_core_api_client.AiApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**conversation_post**](AiApi.md#conversation_post) | **POST** /conversation | Generate response from AI model


# **conversation_post**
> DomainConversationResponse conversation_post(request)

Generate response from AI model

This endpoint generates a response from an AI model based on the provided conversation.

### Example

* Api Key Authentication (BearerAuth):

```python
import ai_core_api_client
from ai_core_api_client.models.domain_conversation_request import DomainConversationRequest
from ai_core_api_client.models.domain_conversation_response import DomainConversationResponse
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
    except Exception as e:
        print("Exception when calling AiApi->conversation_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**DomainConversationRequest**](DomainConversationRequest.md)| Conversation Request | 

### Return type

[**DomainConversationResponse**](DomainConversationResponse.md)

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


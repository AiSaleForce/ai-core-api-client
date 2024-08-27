# DomainGetChatsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chats** | [**List[DomainClientChat]**](DomainClientChat.md) |  | [optional] 

## Example

```python
from openapi_client.models.domain_get_chats_response import DomainGetChatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DomainGetChatsResponse from a JSON string
domain_get_chats_response_instance = DomainGetChatsResponse.from_json(json)
# print the JSON string representation of the object
print(DomainGetChatsResponse.to_json())

# convert the object into a dict
domain_get_chats_response_dict = domain_get_chats_response_instance.to_dict()
# create an instance of DomainGetChatsResponse from a dict
domain_get_chats_response_from_dict = DomainGetChatsResponse.from_dict(domain_get_chats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



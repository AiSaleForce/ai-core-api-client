# DomainClientChat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **int** |  | [optional] 
**messages** | [**List[DomainClientMessage]**](DomainClientMessage.md) |  | [optional] 

## Example

```python
from openapi_client.models.domain_client_chat import DomainClientChat

# TODO update the JSON string below
json = "{}"
# create an instance of DomainClientChat from a JSON string
domain_client_chat_instance = DomainClientChat.from_json(json)
# print the JSON string representation of the object
print(DomainClientChat.to_json())

# convert the object into a dict
domain_client_chat_dict = domain_client_chat_instance.to_dict()
# create an instance of DomainClientChat from a dict
domain_client_chat_from_dict = DomainClientChat.from_dict(domain_client_chat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



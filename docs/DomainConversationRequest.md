# DomainConversationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**functions** | [**List[DomainAIFunction]**](DomainAIFunction.md) |  | [optional] 
**messages** | [**List[DomainAIMessage]**](DomainAIMessage.md) |  | 
**model** | **str** |  | 

## Example

```python
from ai_core_api_client.models.domain_conversation_request import DomainConversationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DomainConversationRequest from a JSON string
domain_conversation_request_instance = DomainConversationRequest.from_json(json)
# print the JSON string representation of the object
print(DomainConversationRequest.to_json())

# convert the object into a dict
domain_conversation_request_dict = domain_conversation_request_instance.to_dict()
# create an instance of DomainConversationRequest from a dict
domain_conversation_request_from_dict = DomainConversationRequest.from_dict(domain_conversation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



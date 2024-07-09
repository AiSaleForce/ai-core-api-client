# DomainConversationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | [optional] 
**tools** | [**List[DomainAITool]**](DomainAITool.md) |  | [optional] 

## Example

```python
from ai_core_api_client.models.domain_conversation_response import DomainConversationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DomainConversationResponse from a JSON string
domain_conversation_response_instance = DomainConversationResponse.from_json(json)
# print the JSON string representation of the object
print(DomainConversationResponse.to_json())

# convert the object into a dict
domain_conversation_response_dict = domain_conversation_response_instance.to_dict()
# create an instance of DomainConversationResponse from a dict
domain_conversation_response_from_dict = DomainConversationResponse.from_dict(domain_conversation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



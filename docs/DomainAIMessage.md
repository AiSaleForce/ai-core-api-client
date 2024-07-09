# DomainAIMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | [optional] 
**role** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.domain_ai_message import DomainAIMessage

# TODO update the JSON string below
json = "{}"
# create an instance of DomainAIMessage from a JSON string
domain_ai_message_instance = DomainAIMessage.from_json(json)
# print the JSON string representation of the object
print(DomainAIMessage.to_json())

# convert the object into a dict
domain_ai_message_dict = domain_ai_message_instance.to_dict()
# create an instance of DomainAIMessage from a dict
domain_ai_message_from_dict = DomainAIMessage.from_dict(domain_ai_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



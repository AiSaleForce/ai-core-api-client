# DomainAITool


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**function** | [**DomainAIFunctionCall**](DomainAIFunctionCall.md) |  | [optional] 
**id** | **str** |  | [optional] 
**index** | **int** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.domain_ai_tool import DomainAITool

# TODO update the JSON string below
json = "{}"
# create an instance of DomainAITool from a JSON string
domain_ai_tool_instance = DomainAITool.from_json(json)
# print the JSON string representation of the object
print(DomainAITool.to_json())

# convert the object into a dict
domain_ai_tool_dict = domain_ai_tool_instance.to_dict()
# create an instance of DomainAITool from a dict
domain_ai_tool_from_dict = DomainAITool.from_dict(domain_ai_tool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



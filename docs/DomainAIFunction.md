# DomainAIFunction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**parameters** | [**DomainAIFunctionParameters**](DomainAIFunctionParameters.md) |  | [optional] 

## Example

```python
from openapi_client.models.domain_ai_function import DomainAIFunction

# TODO update the JSON string below
json = "{}"
# create an instance of DomainAIFunction from a JSON string
domain_ai_function_instance = DomainAIFunction.from_json(json)
# print the JSON string representation of the object
print(DomainAIFunction.to_json())

# convert the object into a dict
domain_ai_function_dict = domain_ai_function_instance.to_dict()
# create an instance of DomainAIFunction from a dict
domain_ai_function_from_dict = DomainAIFunction.from_dict(domain_ai_function_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



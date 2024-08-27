# DomainAIFunctionCall


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arguments** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.domain_ai_function_call import DomainAIFunctionCall

# TODO update the JSON string below
json = "{}"
# create an instance of DomainAIFunctionCall from a JSON string
domain_ai_function_call_instance = DomainAIFunctionCall.from_json(json)
# print the JSON string representation of the object
print(DomainAIFunctionCall.to_json())

# convert the object into a dict
domain_ai_function_call_dict = domain_ai_function_call_instance.to_dict()
# create an instance of DomainAIFunctionCall from a dict
domain_ai_function_call_from_dict = DomainAIFunctionCall.from_dict(domain_ai_function_call_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# DomainAIFunctionParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**Dict[str, DomainAIFunctionParameterProperty]**](DomainAIFunctionParameterProperty.md) |  | [optional] 
**required** | **List[str]** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from ai_core_api_client.models.domain_ai_function_parameters import DomainAIFunctionParameters

# TODO update the JSON string below
json = "{}"
# create an instance of DomainAIFunctionParameters from a JSON string
domain_ai_function_parameters_instance = DomainAIFunctionParameters.from_json(json)
# print the JSON string representation of the object
print(DomainAIFunctionParameters.to_json())

# convert the object into a dict
domain_ai_function_parameters_dict = domain_ai_function_parameters_instance.to_dict()
# create an instance of DomainAIFunctionParameters from a dict
domain_ai_function_parameters_from_dict = DomainAIFunctionParameters.from_dict(domain_ai_function_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



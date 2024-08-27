# DomainGetMeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**functions** | [**List[DomainCompanyFunction]**](DomainCompanyFunction.md) |  | [optional] 
**id** | **str** |  | [optional] 
**level** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**prompt_blocks** | [**List[DomainPromptBlock]**](DomainPromptBlock.md) |  | [optional] 

## Example

```python
from openapi_client.models.domain_get_me_response import DomainGetMeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DomainGetMeResponse from a JSON string
domain_get_me_response_instance = DomainGetMeResponse.from_json(json)
# print the JSON string representation of the object
print(DomainGetMeResponse.to_json())

# convert the object into a dict
domain_get_me_response_dict = domain_get_me_response_instance.to_dict()
# create an instance of DomainGetMeResponse from a dict
domain_get_me_response_from_dict = DomainGetMeResponse.from_dict(domain_get_me_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



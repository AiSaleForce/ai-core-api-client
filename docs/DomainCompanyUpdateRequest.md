# DomainCompanyUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**functions** | [**List[DomainCompanyFunction]**](DomainCompanyFunction.md) |  | [optional] 
**id** | **str** |  | 
**integration_url** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**prompt_blocks** | [**List[DomainPromptBlock]**](DomainPromptBlock.md) |  | [optional] 
**token** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.domain_company_update_request import DomainCompanyUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DomainCompanyUpdateRequest from a JSON string
domain_company_update_request_instance = DomainCompanyUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(DomainCompanyUpdateRequest.to_json())

# convert the object into a dict
domain_company_update_request_dict = domain_company_update_request_instance.to_dict()
# create an instance of DomainCompanyUpdateRequest from a dict
domain_company_update_request_from_dict = DomainCompanyUpdateRequest.from_dict(domain_company_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



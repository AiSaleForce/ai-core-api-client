# DomainCompanyCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**functions** | [**List[DomainCompanyFunction]**](DomainCompanyFunction.md) |  | [optional] 
**integration_url** | **str** |  | 
**name** | **str** |  | 
**prompt_blocks** | [**List[DomainPromptBlock]**](DomainPromptBlock.md) |  | [optional] 
**token** | **str** |  | 

## Example

```python
from openapi_client.models.domain_company_create_request import DomainCompanyCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DomainCompanyCreateRequest from a JSON string
domain_company_create_request_instance = DomainCompanyCreateRequest.from_json(json)
# print the JSON string representation of the object
print(DomainCompanyCreateRequest.to_json())

# convert the object into a dict
domain_company_create_request_dict = domain_company_create_request_instance.to_dict()
# create an instance of DomainCompanyCreateRequest from a dict
domain_company_create_request_from_dict = DomainCompanyCreateRequest.from_dict(domain_company_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



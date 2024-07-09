# DomainCompanyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**token** | **str** |  | 

## Example

```python
from openapi_client.models.domain_company_request import DomainCompanyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DomainCompanyRequest from a JSON string
domain_company_request_instance = DomainCompanyRequest.from_json(json)
# print the JSON string representation of the object
print(DomainCompanyRequest.to_json())

# convert the object into a dict
domain_company_request_dict = domain_company_request_instance.to_dict()
# create an instance of DomainCompanyRequest from a dict
domain_company_request_from_dict = DomainCompanyRequest.from_dict(domain_company_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



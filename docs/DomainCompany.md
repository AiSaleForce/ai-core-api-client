# DomainCompany


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**token** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.domain_company import DomainCompany

# TODO update the JSON string below
json = "{}"
# create an instance of DomainCompany from a JSON string
domain_company_instance = DomainCompany.from_json(json)
# print the JSON string representation of the object
print(DomainCompany.to_json())

# convert the object into a dict
domain_company_dict = domain_company_instance.to_dict()
# create an instance of DomainCompany from a dict
domain_company_from_dict = DomainCompany.from_dict(domain_company_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



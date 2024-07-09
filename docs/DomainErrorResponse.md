# DomainErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.domain_error_response import DomainErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DomainErrorResponse from a JSON string
domain_error_response_instance = DomainErrorResponse.from_json(json)
# print the JSON string representation of the object
print(DomainErrorResponse.to_json())

# convert the object into a dict
domain_error_response_dict = domain_error_response_instance.to_dict()
# create an instance of DomainErrorResponse from a dict
domain_error_response_from_dict = DomainErrorResponse.from_dict(domain_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



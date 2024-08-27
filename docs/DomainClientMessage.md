# DomainClientMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **int** |  | [optional] 
**content** | **str** |  | [optional] 
**var_date** | **str** |  | [optional] 
**event_id** | **int** |  | [optional] 
**message_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.domain_client_message import DomainClientMessage

# TODO update the JSON string below
json = "{}"
# create an instance of DomainClientMessage from a JSON string
domain_client_message_instance = DomainClientMessage.from_json(json)
# print the JSON string representation of the object
print(DomainClientMessage.to_json())

# convert the object into a dict
domain_client_message_dict = domain_client_message_instance.to_dict()
# create an instance of DomainClientMessage from a dict
domain_client_message_from_dict = DomainClientMessage.from_dict(domain_client_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



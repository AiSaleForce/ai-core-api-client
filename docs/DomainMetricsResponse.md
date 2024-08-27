# DomainMetricsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dialog_count** | **int** |  | [optional] 
**message_count_per_day** | **int** |  | [optional] 
**messsage_count_per_month** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.domain_metrics_response import DomainMetricsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DomainMetricsResponse from a JSON string
domain_metrics_response_instance = DomainMetricsResponse.from_json(json)
# print the JSON string representation of the object
print(DomainMetricsResponse.to_json())

# convert the object into a dict
domain_metrics_response_dict = domain_metrics_response_instance.to_dict()
# create an instance of DomainMetricsResponse from a dict
domain_metrics_response_from_dict = DomainMetricsResponse.from_dict(domain_metrics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



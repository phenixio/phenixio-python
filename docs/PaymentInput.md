# PaymentInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Value of the payment at the time of creation. (Example: 3.14 USD) | 
**description** | **str** | Display the description of payment | 
**currency** | **str** | Choose the currency of value field (Default: USD) | [optional]  if omitted the server will use the default value of "usd"
**metadata** | [**MetadataInput**](MetadataInput.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# SubscriptionPlanOutput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **int** |  | 
**id** | **int** |  | [optional] [readonly] 
**created** | **datetime** |  | [optional] [readonly] 
**modified** | **datetime** |  | [optional] [readonly] 
**interval** | **str** | Set a subscription payment interval. | [optional]  if omitted the server will use the default value of "month"
**price** | **str** | Set a price for your subscription. | [optional] 
**currency** | **str** |  | [optional]  if omitted the server will use the default value of "usd"
**collection_method** | **str** | Collect payments by sending Lightning payment request to customer email. | [optional]  if omitted the server will use the default value of "send_invoice"
**webhook_url** | **str** | Set the webhook endpoint to get notified on your application backend. | [optional] 
**application_url** | **str** | Application associated with this subscription plan. Customers are redirected after successful payments. | [optional] 
**name** | **str** | The name of your subscription. It will appear in the email we send to your customers. | [optional] 
**description** | **str** | Short description of your subscription product/service. It will appear in the email we send to your customers. | [optional] 
**grace_period** | **int** | Set how many days a subscription gets canceled for over due payments. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



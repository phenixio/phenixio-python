# PaymentOutput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **int** | Receiver of this payment | 
**amount** | **int** | Bitcoin amount in Satoshi units | 
**value** | **str** | Value of the payment at the time of creation. (Example: 3.14 USD) | 
**description** | **str** | Display the description of payment | 
**payment_request** | **str** |  | 
**lninvoice** | [**LightningInvoiceOutput**](LightningInvoiceOutput.md) |  | 
**uuid** | **str** |  | [optional] [readonly] 
**object** | **str** |  | [optional]  if omitted the server will use the default value of "charge"
**amount_settled** | **int** |  | [optional] 
**settled** | **bool** |  | [optional]  if omitted the server will use the default value of False
**currency** | **str** | Choose the currency of value field (Default: USD) | [optional]  if omitted the server will use the default value of "usd"
**timestamp** | **datetime** | When this payment is created. (UTC Timestamp) | [optional] [readonly] 
**webpay_code** | **str** | Code for using web payment UI. Check webpay documentation for details. | [optional] 
**metadata** | [**MetadataInput**](MetadataInput.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



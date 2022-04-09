# LightningInvoiceOutput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_request** | **str** | A bare-bones invoice for a payment within the Lightning Network. With the details of the invoice, the sender has all the data necessary to send a payment to the recipient. | 
**expiry** | **int** | Payment request expiry time in seconds. | 
**r_hash** | **str** | Base64 encoded hash of the corresponding invoice preimage | 
**network** | **str** | Lightning Network version (testnet/mainnet) | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



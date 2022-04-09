# SettleEventOutput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settle_date** | **int** | When this invoice was settled (UTC Timestamp) | 
**amt_paid_sat** | **int** | The amount that was ultimately accepted for this invoice, in satoshis. | 
**settled** | **bool** | Whether this invoice has been fulfilled | 
**state** | **str** | The state the invoice is in. | 
**r_preimage** | **str** | Base64 encoded preimage (32 byte hex) which will allow settling an incoming HTLC payable to this preimage. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



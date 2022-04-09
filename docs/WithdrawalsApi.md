# phenixio.WithdrawalsApi

All URIs are relative to *https://testnet.phenixio.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**withdrawals_create**](WithdrawalsApi.md#withdrawals_create) | **POST** /withdrawals/ | On-Chain Withdrawals


# **withdrawals_create**
> WithdrawalRequest withdrawals_create(data)

On-Chain Withdrawals

Request for a withdrawal of your available balances to an onchain wallet address

### Example


```python
import time
import phenixio
from phenixio.api import withdrawals_api
from phenixio.model.withdrawal_request import WithdrawalRequest
from pprint import pprint
# Defining the host is optional and defaults to https://testnet.phenixio.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = phenixio.Configuration(
    host = "https://testnet.phenixio.com/api"
)


# Enter a context with an instance of the API client
with phenixio.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = withdrawals_api.WithdrawalsApi(api_client)
    data = WithdrawalRequest(
        amount=1E+4,
        addr="addr_example",
    ) # WithdrawalRequest | 

    # example passing only required values which don't have defaults set
    try:
        # On-Chain Withdrawals
        api_response = api_instance.withdrawals_create(data)
        pprint(api_response)
    except phenixio.ApiException as e:
        print("Exception when calling WithdrawalsApi->withdrawals_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WithdrawalRequest**](WithdrawalRequest.md)|  |

### Return type

[**WithdrawalRequest**](WithdrawalRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# phenixio.PaymentsApi

All URIs are relative to *https://local.sandbox.phenixio.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payments_create**](PaymentsApi.md#payments_create) | **POST** /payments/ | New Payment Request
[**payments_list**](PaymentsApi.md#payments_list) | **GET** /payments/ | Received Payments
[**payments_pending_list**](PaymentsApi.md#payments_pending_list) | **GET** /payments/pending/ | Pending Payments
[**payments_read**](PaymentsApi.md#payments_read) | **GET** /payments/{uuid}/ | Payment Info
[**payments_sum_read**](PaymentsApi.md#payments_sum_read) | **GET** /payments/sum/ | 


# **payments_create**
> PaymentOutput payments_create(data)

New Payment Request

Creates a new payment request on Lightning Network and returns details.

### Example


```python
import time
import phenixio
from phenixio.api import payments_api
from phenixio.model.payment_input import PaymentInput
from phenixio.model.payment_output import PaymentOutput
from pprint import pprint
# Defining the host is optional and defaults to https://local.sandbox.phenixio.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = phenixio.Configuration(
    host = "https://local.sandbox.phenixio.com/api"
)


# Enter a context with an instance of the API client
with phenixio.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payments_api.PaymentsApi(api_client)
    data = PaymentInput(
        amount=0,
        description="description_example",
        currency="currency_example",
        metadata=MetadataInput(
            customer_email="customer_email_example",
            customer_name="customer_name_example",
            order_id="order_id_example",
            callback_url="callback_url_example",
            success_url="success_url_example",
        ),
    ) # PaymentInput | 

    # example passing only required values which don't have defaults set
    try:
        # New Payment Request
        api_response = api_instance.payments_create(data)
        pprint(api_response)
    except phenixio.ApiException as e:
        print("Exception when calling PaymentsApi->payments_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**PaymentInput**](PaymentInput.md)|  |

### Return type

[**PaymentOutput**](PaymentOutput.md)

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

# **payments_list**
> [PaidChargesOutput] payments_list()

Received Payments

Returns a list of received payments that are already settled on Lightning Network.

### Example


```python
import time
import phenixio
from phenixio.api import payments_api
from phenixio.model.paid_charges_output import PaidChargesOutput
from pprint import pprint
# Defining the host is optional and defaults to https://local.sandbox.phenixio.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = phenixio.Configuration(
    host = "https://local.sandbox.phenixio.com/api"
)


# Enter a context with an instance of the API client
with phenixio.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payments_api.PaymentsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Received Payments
        api_response = api_instance.payments_list()
        pprint(api_response)
    except phenixio.ApiException as e:
        print("Exception when calling PaymentsApi->payments_list: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[PaidChargesOutput]**](PaidChargesOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payments_pending_list**
> [PaymentOutput] payments_pending_list()

Pending Payments

Returns a list of pending payments that your customers might still settle them.

### Example


```python
import time
import phenixio
from phenixio.api import payments_api
from phenixio.model.payment_output import PaymentOutput
from pprint import pprint
# Defining the host is optional and defaults to https://local.sandbox.phenixio.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = phenixio.Configuration(
    host = "https://local.sandbox.phenixio.com/api"
)


# Enter a context with an instance of the API client
with phenixio.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payments_api.PaymentsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Pending Payments
        api_response = api_instance.payments_pending_list()
        pprint(api_response)
    except phenixio.ApiException as e:
        print("Exception when calling PaymentsApi->payments_pending_list: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[PaymentOutput]**](PaymentOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payments_read**
> PaymentOutput payments_read(uuid)

Payment Info

Returns detailed information for a payment object.

### Example


```python
import time
import phenixio
from phenixio.api import payments_api
from phenixio.model.payment_output import PaymentOutput
from pprint import pprint
# Defining the host is optional and defaults to https://local.sandbox.phenixio.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = phenixio.Configuration(
    host = "https://local.sandbox.phenixio.com/api"
)


# Enter a context with an instance of the API client
with phenixio.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payments_api.PaymentsApi(api_client)
    uuid = "uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Payment Info
        api_response = api_instance.payments_read(uuid)
        pprint(api_response)
    except phenixio.ApiException as e:
        print("Exception when calling PaymentsApi->payments_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |

### Return type

[**PaymentOutput**](PaymentOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payments_sum_read**
> Output payments_sum_read()



Get Balance Sum

### Example


```python
import time
import phenixio
from phenixio.api import payments_api
from phenixio.model.output import Output
from pprint import pprint
# Defining the host is optional and defaults to https://local.sandbox.phenixio.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = phenixio.Configuration(
    host = "https://local.sandbox.phenixio.com/api"
)


# Enter a context with an instance of the API client
with phenixio.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payments_api.PaymentsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.payments_sum_read()
        pprint(api_response)
    except phenixio.ApiException as e:
        print("Exception when calling PaymentsApi->payments_sum_read: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Output**](Output.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


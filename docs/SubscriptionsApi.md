# phenixio.SubscriptionsApi

All URIs are relative to *https://testnet.phenixio.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subscriptions_create**](SubscriptionsApi.md#subscriptions_create) | **POST** /subscriptions/ | NewSubscription
[**subscriptions_list**](SubscriptionsApi.md#subscriptions_list) | **GET** /subscriptions/ | ListSubscriptions
[**subscriptions_plans_create**](SubscriptionsApi.md#subscriptions_plans_create) | **POST** /subscriptions/plans/ | NewSubscriptionPlan
[**subscriptions_plans_list**](SubscriptionsApi.md#subscriptions_plans_list) | **GET** /subscriptions/plans/ | ListSubscriptionPlans
[**subscriptions_plans_read**](SubscriptionsApi.md#subscriptions_plans_read) | **GET** /subscriptions/plans/{id}/ | SubscriptionPlanStatus
[**subscriptions_read**](SubscriptionsApi.md#subscriptions_read) | **GET** /subscriptions/{id} | SubscriptionStatus


# **subscriptions_create**
> SubscriptionInput subscriptions_create(data)

NewSubscription

Create a new subscription

### Example


```python
import time
import phenixio
from phenixio.api import subscriptions_api
from phenixio.model.subscription_input import SubscriptionInput
from pprint import pprint
# Defining the host is optional and defaults to https://testnet.phenixio.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = phenixio.Configuration(
    host = "https://testnet.phenixio.com/api"
)


# Enter a context with an instance of the API client
with phenixio.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = subscriptions_api.SubscriptionsApi(api_client)
    data = SubscriptionInput(
        subscription_plan=1,
        customer_email="customer_email_example",
    ) # SubscriptionInput | 

    # example passing only required values which don't have defaults set
    try:
        # NewSubscription
        api_response = api_instance.subscriptions_create(data)
        pprint(api_response)
    except phenixio.ApiException as e:
        print("Exception when calling SubscriptionsApi->subscriptions_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**SubscriptionInput**](SubscriptionInput.md)|  |

### Return type

[**SubscriptionInput**](SubscriptionInput.md)

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

# **subscriptions_list**
> [SubscriptionInput] subscriptions_list()

ListSubscriptions

List all subscriptions on your account.

### Example


```python
import time
import phenixio
from phenixio.api import subscriptions_api
from phenixio.model.subscription_input import SubscriptionInput
from pprint import pprint
# Defining the host is optional and defaults to https://testnet.phenixio.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = phenixio.Configuration(
    host = "https://testnet.phenixio.com/api"
)


# Enter a context with an instance of the API client
with phenixio.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = subscriptions_api.SubscriptionsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # ListSubscriptions
        api_response = api_instance.subscriptions_list()
        pprint(api_response)
    except phenixio.ApiException as e:
        print("Exception when calling SubscriptionsApi->subscriptions_list: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[SubscriptionInput]**](SubscriptionInput.md)

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

# **subscriptions_plans_create**
> SubscriptionPlanInput subscriptions_plans_create(data)

NewSubscriptionPlan

Create a new subscription plan

### Example


```python
import time
import phenixio
from phenixio.api import subscriptions_api
from phenixio.model.subscription_plan_input import SubscriptionPlanInput
from pprint import pprint
# Defining the host is optional and defaults to https://testnet.phenixio.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = phenixio.Configuration(
    host = "https://testnet.phenixio.com/api"
)


# Enter a context with an instance of the API client
with phenixio.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = subscriptions_api.SubscriptionsApi(api_client)
    data = SubscriptionPlanInput(
        interval="month",
        price="price_example",
        currency="usd",
        collection_method="send_invoice",
        webhook_url="webhook_url_example",
        application_url="application_url_example",
        name="name_example",
        description="description_example",
        grace_period=0,
    ) # SubscriptionPlanInput | 

    # example passing only required values which don't have defaults set
    try:
        # NewSubscriptionPlan
        api_response = api_instance.subscriptions_plans_create(data)
        pprint(api_response)
    except phenixio.ApiException as e:
        print("Exception when calling SubscriptionsApi->subscriptions_plans_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**SubscriptionPlanInput**](SubscriptionPlanInput.md)|  |

### Return type

[**SubscriptionPlanInput**](SubscriptionPlanInput.md)

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

# **subscriptions_plans_list**
> [SubscriptionPlanInput] subscriptions_plans_list()

ListSubscriptionPlans

List all subscription plans on your account.

### Example


```python
import time
import phenixio
from phenixio.api import subscriptions_api
from phenixio.model.subscription_plan_input import SubscriptionPlanInput
from pprint import pprint
# Defining the host is optional and defaults to https://testnet.phenixio.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = phenixio.Configuration(
    host = "https://testnet.phenixio.com/api"
)


# Enter a context with an instance of the API client
with phenixio.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = subscriptions_api.SubscriptionsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # ListSubscriptionPlans
        api_response = api_instance.subscriptions_plans_list()
        pprint(api_response)
    except phenixio.ApiException as e:
        print("Exception when calling SubscriptionsApi->subscriptions_plans_list: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[SubscriptionPlanInput]**](SubscriptionPlanInput.md)

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

# **subscriptions_plans_read**
> SubscriptionPlanOutput subscriptions_plans_read(id)

SubscriptionPlanStatus

Get a subscription plan status by id.

### Example


```python
import time
import phenixio
from phenixio.api import subscriptions_api
from phenixio.model.subscription_plan_output import SubscriptionPlanOutput
from pprint import pprint
# Defining the host is optional and defaults to https://testnet.phenixio.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = phenixio.Configuration(
    host = "https://testnet.phenixio.com/api"
)


# Enter a context with an instance of the API client
with phenixio.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = subscriptions_api.SubscriptionsApi(api_client)
    id = 1 # int | A unique integer value identifying this Subscription Plan.

    # example passing only required values which don't have defaults set
    try:
        # SubscriptionPlanStatus
        api_response = api_instance.subscriptions_plans_read(id)
        pprint(api_response)
    except phenixio.ApiException as e:
        print("Exception when calling SubscriptionsApi->subscriptions_plans_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Subscription Plan. |

### Return type

[**SubscriptionPlanOutput**](SubscriptionPlanOutput.md)

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

# **subscriptions_read**
> SubscriptionOutput subscriptions_read(id)

SubscriptionStatus

Get a subscription status by id.

### Example


```python
import time
import phenixio
from phenixio.api import subscriptions_api
from phenixio.model.subscription_output import SubscriptionOutput
from pprint import pprint
# Defining the host is optional and defaults to https://testnet.phenixio.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = phenixio.Configuration(
    host = "https://testnet.phenixio.com/api"
)


# Enter a context with an instance of the API client
with phenixio.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = subscriptions_api.SubscriptionsApi(api_client)
    id = 1 # int | A unique integer value identifying this subscriber.

    # example passing only required values which don't have defaults set
    try:
        # SubscriptionStatus
        api_response = api_instance.subscriptions_read(id)
        pprint(api_response)
    except phenixio.ApiException as e:
        print("Exception when calling SubscriptionsApi->subscriptions_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this subscriber. |

### Return type

[**SubscriptionOutput**](SubscriptionOutput.md)

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


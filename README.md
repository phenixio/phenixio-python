# phenixio

# Introduction

The Phenixio API allows you to integrate Lightning Network payments into your application.

## Just Getting Started?

Start developing your Phenixio integration with our client libraries. We will publish a guide soon: [Development Quickstart](https://github.com/phenixio/sdk)


## Generating Access Token

API endpoints require token based authentication. You can [Generate Access Token](#post-/token/) with your user credentials. You will recieve an access token in JWT format. Set your request header \"Authorization: Bearer `<YOUR-ACCESS-TOKEN>`\"


## Curl Example

Test your access token with Curl request. Replace `<YOUR-ACCESS-TOKEN>` with your actual token.


```bash
$ curl -I -X GET --http1.1 -H \"Content-Type: application/json\" -H \"Authorization: Bearer <YOUR-ACCESS-TOKEN>\"  https://sandbox.phenixio.com/api/charges/
```




This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v0.4.2-beta [testnet]
- Package version: 0.1.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import phenixio
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import phenixio
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import phenixio
from pprint import pprint
from phenixio.api import auth_tokens_api
from phenixio.model.token_obtain_pair import TokenObtainPair
from phenixio.model.token_pair import TokenPair
from phenixio.model.token_refresh import TokenRefresh
from phenixio.model.token_verify import TokenVerify
# Defining the host is optional and defaults to https://testnet.phenixio.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = phenixio.Configuration(
    host = "https://testnet.phenixio.com/api"
)



# Enter a context with an instance of the API client
with phenixio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_tokens_api.AuthTokensApi(api_client)
    data = TokenObtainPair(
        email="email_example",
        password="password_example",
    ) # TokenObtainPair | 

    try:
        # Access Token
        api_response = api_instance.auth_tokens_create(data)
        pprint(api_response)
    except phenixio.ApiException as e:
        print("Exception when calling AuthTokensApi->auth_tokens_create: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://testnet.phenixio.com/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthTokensApi* | [**auth_tokens_create**](docs/AuthTokensApi.md#auth_tokens_create) | **POST** /auth-tokens/ | Access Token
*AuthTokensApi* | [**auth_tokens_refresh_create**](docs/AuthTokensApi.md#auth_tokens_refresh_create) | **POST** /auth-tokens/refresh/ | Refresh Token
*AuthTokensApi* | [**auth_tokens_verify_create**](docs/AuthTokensApi.md#auth_tokens_verify_create) | **POST** /auth-tokens/verify/ | Verify Token
*PaymentsApi* | [**payments_create**](docs/PaymentsApi.md#payments_create) | **POST** /payments/ | New Payment Request
*PaymentsApi* | [**payments_list**](docs/PaymentsApi.md#payments_list) | **GET** /payments/ | Received Payments
*PaymentsApi* | [**payments_pending_list**](docs/PaymentsApi.md#payments_pending_list) | **GET** /payments/pending/ | Pending Payments
*PaymentsApi* | [**payments_read**](docs/PaymentsApi.md#payments_read) | **GET** /payments/{uuid}/ | Payment Info
*PaymentsApi* | [**payments_sum_read**](docs/PaymentsApi.md#payments_sum_read) | **GET** /payments/sum/ | 
*SubscriptionsApi* | [**subscriptions_create**](docs/SubscriptionsApi.md#subscriptions_create) | **POST** /subscriptions/ | NewSubscription
*SubscriptionsApi* | [**subscriptions_list**](docs/SubscriptionsApi.md#subscriptions_list) | **GET** /subscriptions/ | ListSubscriptions
*SubscriptionsApi* | [**subscriptions_plans_create**](docs/SubscriptionsApi.md#subscriptions_plans_create) | **POST** /subscriptions/plans/ | NewSubscriptionPlan
*SubscriptionsApi* | [**subscriptions_plans_list**](docs/SubscriptionsApi.md#subscriptions_plans_list) | **GET** /subscriptions/plans/ | ListSubscriptionPlans
*SubscriptionsApi* | [**subscriptions_plans_read**](docs/SubscriptionsApi.md#subscriptions_plans_read) | **GET** /subscriptions/plans/{id}/ | SubscriptionPlanStatus
*SubscriptionsApi* | [**subscriptions_read**](docs/SubscriptionsApi.md#subscriptions_read) | **GET** /subscriptions/{id} | SubscriptionStatus
*WithdrawalsApi* | [**withdrawals_create**](docs/WithdrawalsApi.md#withdrawals_create) | **POST** /withdrawals/ | On-Chain Withdrawals


## Documentation For Models

 - [LightningInvoiceOutput](docs/LightningInvoiceOutput.md)
 - [MetadataInput](docs/MetadataInput.md)
 - [Output](docs/Output.md)
 - [PaidChargesOutput](docs/PaidChargesOutput.md)
 - [PaymentInput](docs/PaymentInput.md)
 - [PaymentOutput](docs/PaymentOutput.md)
 - [SettleEventOutput](docs/SettleEventOutput.md)
 - [SubscriptionInput](docs/SubscriptionInput.md)
 - [SubscriptionOutput](docs/SubscriptionOutput.md)
 - [SubscriptionPlanInput](docs/SubscriptionPlanInput.md)
 - [SubscriptionPlanOutput](docs/SubscriptionPlanOutput.md)
 - [TokenObtainPair](docs/TokenObtainPair.md)
 - [TokenPair](docs/TokenPair.md)
 - [TokenRefresh](docs/TokenRefresh.md)
 - [TokenVerify](docs/TokenVerify.md)
 - [WithdrawalRequest](docs/WithdrawalRequest.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author

support@phenixio.com


## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in phenixio.apis and phenixio.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from phenixio.api.default_api import DefaultApi`
- `from phenixio.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import phenixio
from phenixio.apis import *
from phenixio.models import *
```


# phenixio.AuthTokensApi

All URIs are relative to *https://local.sandbox.phenixio.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_tokens_create**](AuthTokensApi.md#auth_tokens_create) | **POST** /auth-tokens/ | Access Token
[**auth_tokens_refresh_create**](AuthTokensApi.md#auth_tokens_refresh_create) | **POST** /auth-tokens/refresh/ | Refresh Token
[**auth_tokens_verify_create**](AuthTokensApi.md#auth_tokens_verify_create) | **POST** /auth-tokens/verify/ | Verify Token


# **auth_tokens_create**
> TokenPair auth_tokens_create(data)

Access Token

Takes a set of user credentials and returns an access and refresh JSON web token pair to prove the authentication of those credentials.

### Example


```python
import time
import phenixio
from phenixio.api import auth_tokens_api
from phenixio.model.token_pair import TokenPair
from phenixio.model.token_obtain_pair import TokenObtainPair
from pprint import pprint
# Defining the host is optional and defaults to https://local.sandbox.phenixio.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = phenixio.Configuration(
    host = "https://local.sandbox.phenixio.com/api"
)


# Enter a context with an instance of the API client
with phenixio.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_tokens_api.AuthTokensApi(api_client)
    data = TokenObtainPair(
        email="email_example",
        password="password_example",
    ) # TokenObtainPair | 

    # example passing only required values which don't have defaults set
    try:
        # Access Token
        api_response = api_instance.auth_tokens_create(data)
        pprint(api_response)
    except phenixio.ApiException as e:
        print("Exception when calling AuthTokensApi->auth_tokens_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**TokenObtainPair**](TokenObtainPair.md)|  |

### Return type

[**TokenPair**](TokenPair.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_tokens_refresh_create**
> TokenRefresh auth_tokens_refresh_create(data)

Refresh Token

Takes a refresh type JSON web token and returns an access type JSON web token if the refresh token is valid.

### Example


```python
import time
import phenixio
from phenixio.api import auth_tokens_api
from phenixio.model.token_refresh import TokenRefresh
from pprint import pprint
# Defining the host is optional and defaults to https://local.sandbox.phenixio.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = phenixio.Configuration(
    host = "https://local.sandbox.phenixio.com/api"
)


# Enter a context with an instance of the API client
with phenixio.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_tokens_api.AuthTokensApi(api_client)
    data = TokenRefresh(
        refresh="refresh_example",
    ) # TokenRefresh | 

    # example passing only required values which don't have defaults set
    try:
        # Refresh Token
        api_response = api_instance.auth_tokens_refresh_create(data)
        pprint(api_response)
    except phenixio.ApiException as e:
        print("Exception when calling AuthTokensApi->auth_tokens_refresh_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**TokenRefresh**](TokenRefresh.md)|  |

### Return type

[**TokenRefresh**](TokenRefresh.md)

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

# **auth_tokens_verify_create**
> TokenVerify auth_tokens_verify_create(data)

Verify Token

Takes a token and indicates if it is valid. This view provides no information about a token's fitness for a particular use.

### Example


```python
import time
import phenixio
from phenixio.api import auth_tokens_api
from phenixio.model.token_verify import TokenVerify
from pprint import pprint
# Defining the host is optional and defaults to https://local.sandbox.phenixio.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = phenixio.Configuration(
    host = "https://local.sandbox.phenixio.com/api"
)


# Enter a context with an instance of the API client
with phenixio.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_tokens_api.AuthTokensApi(api_client)
    data = TokenVerify(
        token="token_example",
    ) # TokenVerify | 

    # example passing only required values which don't have defaults set
    try:
        # Verify Token
        api_response = api_instance.auth_tokens_verify_create(data)
        pprint(api_response)
    except phenixio.ApiException as e:
        print("Exception when calling AuthTokensApi->auth_tokens_verify_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**TokenVerify**](TokenVerify.md)|  |

### Return type

[**TokenVerify**](TokenVerify.md)

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


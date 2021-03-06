# flake8: noqa

"""
    Phenixio API Reference

     # Introduction  The Phenixio API allows you to integrate Lightning Network payments into your application.  ## Just Getting Started?  Start developing your Phenixio integration with our client libraries. We will publish a guide soon: [Development Quickstart](https://github.com/phenixio/sdk)   ## Generating Access Token  API endpoints require token based authentication. You can [Generate Access Token](#post-/token/) with your user credentials. You will recieve an access token in JWT format. Set your request header \"Authorization: Bearer `<YOUR-ACCESS-TOKEN>`\"   ## Curl Example  Test your access token with Curl request. Replace `<YOUR-ACCESS-TOKEN>` with your actual token.   ```bash $ curl -I -X GET --http1.1 -H \"Content-Type: application/json\" -H \"Authorization: Bearer <YOUR-ACCESS-TOKEN>\"  https://sandbox.phenixio.com/api/charges/ ```     # noqa: E501

    The version of the OpenAPI document: v0.4.2-beta [testnet]
    Contact: support@phenixio.com
    Generated by: https://openapi-generator.tech
"""


__version__ = "0.1.0"

# import ApiClient
from phenixio.api_client import ApiClient

# import Configuration
from phenixio.configuration import Configuration

# import exceptions
from phenixio.exceptions import OpenApiException
from phenixio.exceptions import ApiAttributeError
from phenixio.exceptions import ApiTypeError
from phenixio.exceptions import ApiValueError
from phenixio.exceptions import ApiKeyError
from phenixio.exceptions import ApiException

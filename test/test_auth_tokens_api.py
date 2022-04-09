"""
    Phenixio API Reference

     # Introduction  The Phenixio API allows you to integrate Lightning Network payments into your application.  ## Just Getting Started?  Start developing your Phenixio integration with our client libraries. We will publish a guide soon: [Development Quickstart](https://github.com/phenixio/sdk)   ## Generating Access Token  API endpoints require token based authentication. You can [Generate Access Token](#post-/token/) with your user credentials. You will recieve an access token in JWT format. Set your request header \"Authorization: Bearer `<YOUR-ACCESS-TOKEN>`\"   ## Curl Example  Test your access token with Curl request. Replace `<YOUR-ACCESS-TOKEN>` with your actual token.   ```bash $ curl -I -X GET --http1.1 -H \"Content-Type: application/json\" -H \"Authorization: Bearer <YOUR-ACCESS-TOKEN>\"  https://sandbox.phenixio.com/api/charges/ ```     # noqa: E501

    The version of the OpenAPI document: v0.3.2-beta [testnet]
    Contact: support@phenixio.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import phenixio
from phenixio.api.auth_tokens_api import AuthTokensApi  # noqa: E501


class TestAuthTokensApi(unittest.TestCase):
    """AuthTokensApi unit test stubs"""

    def setUp(self):
        self.api = AuthTokensApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_auth_tokens_create(self):
        """Test case for auth_tokens_create

        Access Token  # noqa: E501
        """
        pass

    def test_auth_tokens_refresh_create(self):
        """Test case for auth_tokens_refresh_create

        Refresh Token  # noqa: E501
        """
        pass

    def test_auth_tokens_verify_create(self):
        """Test case for auth_tokens_verify_create

        Verify Token  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

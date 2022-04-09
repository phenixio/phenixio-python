"""
    Phenixio API Reference

     # Introduction  The Phenixio API allows you to integrate Lightning Network payments into your application.  ## Just Getting Started?  Start developing your Phenixio integration with our client libraries. We will publish a guide soon: [Development Quickstart](https://github.com/phenixio/sdk)   ## Generating Access Token  API endpoints require token based authentication. You can [Generate Access Token](#post-/token/) with your user credentials. You will recieve an access token in JWT format. Set your request header \"Authorization: Bearer `<YOUR-ACCESS-TOKEN>`\"   ## Curl Example  Test your access token with Curl request. Replace `<YOUR-ACCESS-TOKEN>` with your actual token.   ```bash $ curl -I -X GET --http1.1 -H \"Content-Type: application/json\" -H \"Authorization: Bearer <YOUR-ACCESS-TOKEN>\"  https://sandbox.phenixio.com/api/charges/ ```     # noqa: E501

    The version of the OpenAPI document: v0.3.2-beta [testnet]
    Contact: support@phenixio.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import phenixio
from phenixio.model.subscription_output import SubscriptionOutput


class TestSubscriptionOutput(unittest.TestCase):
    """SubscriptionOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSubscriptionOutput(self):
        """Test SubscriptionOutput"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SubscriptionOutput()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()

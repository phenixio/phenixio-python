
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.auth_tokens_api import AuthTokensApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from phenixio.api.auth_tokens_api import AuthTokensApi
from phenixio.api.payments_api import PaymentsApi
from phenixio.api.subscriptions_api import SubscriptionsApi
from phenixio.api.withdrawals_api import WithdrawalsApi

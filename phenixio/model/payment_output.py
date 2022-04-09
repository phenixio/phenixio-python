"""
    Phenixio API Reference

     # Introduction  The Phenixio API allows you to integrate Lightning Network payments into your application.  ## Just Getting Started?  Start developing your Phenixio integration with our client libraries. We will publish a guide soon: [Development Quickstart](https://github.com/phenixio/sdk)   ## Generating Access Token  API endpoints require token based authentication. You can [Generate Access Token](#post-/token/) with your user credentials. You will recieve an access token in JWT format. Set your request header \"Authorization: Bearer `<YOUR-ACCESS-TOKEN>`\"   ## Curl Example  Test your access token with Curl request. Replace `<YOUR-ACCESS-TOKEN>` with your actual token.   ```bash $ curl -I -X GET --http1.1 -H \"Content-Type: application/json\" -H \"Authorization: Bearer <YOUR-ACCESS-TOKEN>\"  https://sandbox.phenixio.com/api/charges/ ```     # noqa: E501

    The version of the OpenAPI document: v0.4.2-beta [testnet]
    Contact: support@phenixio.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from phenixio.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from phenixio.exceptions import ApiAttributeError


def lazy_import():
    from phenixio.model.lightning_invoice_output import LightningInvoiceOutput
    from phenixio.model.metadata_input import MetadataInput
    globals()['LightningInvoiceOutput'] = LightningInvoiceOutput
    globals()['MetadataInput'] = MetadataInput


class PaymentOutput(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('currency',): {
            'USD': "usd",
        },
    }

    validations = {
        ('amount',): {
            'inclusive_maximum': 2147483647,
            'inclusive_minimum': 0,
        },
        ('description',): {
            'max_length': 60,
            'min_length': 1,
        },
        ('payment_request',): {
            'min_length': 1,
        },
        ('object',): {
            'min_length': 1,
        },
        ('webpay_code',): {
            'max_length': 10,
            'min_length': 1,
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'account': (int,),  # noqa: E501
            'amount': (int,),  # noqa: E501
            'value': (str,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'payment_request': (str,),  # noqa: E501
            'lninvoice': (LightningInvoiceOutput,),  # noqa: E501
            'uuid': (str,),  # noqa: E501
            'object': (str,),  # noqa: E501
            'amount_settled': (int,),  # noqa: E501
            'settled': (bool,),  # noqa: E501
            'currency': (str,),  # noqa: E501
            'timestamp': (datetime,),  # noqa: E501
            'webpay_code': (str,),  # noqa: E501
            'metadata': (MetadataInput,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'account': 'account',  # noqa: E501
        'amount': 'amount',  # noqa: E501
        'value': 'value',  # noqa: E501
        'description': 'description',  # noqa: E501
        'payment_request': 'payment_request',  # noqa: E501
        'lninvoice': 'lninvoice',  # noqa: E501
        'uuid': 'uuid',  # noqa: E501
        'object': 'object',  # noqa: E501
        'amount_settled': 'amount_settled',  # noqa: E501
        'settled': 'settled',  # noqa: E501
        'currency': 'currency',  # noqa: E501
        'timestamp': 'timestamp',  # noqa: E501
        'webpay_code': 'webpay_code',  # noqa: E501
        'metadata': 'metadata',  # noqa: E501
    }

    read_only_vars = {
        'uuid',  # noqa: E501
        'timestamp',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, account, amount, value, description, payment_request, lninvoice, *args, **kwargs):  # noqa: E501
        """PaymentOutput - a model defined in OpenAPI

        Args:
            account (int): Receiver of this payment
            amount (int): Bitcoin amount in Satoshi units
            value (str): Value of the payment at the time of creation. (Example: 3.14 USD)
            description (str): Display the description of payment
            payment_request (str):
            lninvoice (LightningInvoiceOutput):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            uuid (str): [optional]  # noqa: E501
            object (str): [optional] if omitted the server will use the default value of "charge"  # noqa: E501
            amount_settled (int): [optional]  # noqa: E501
            settled (bool): [optional] if omitted the server will use the default value of False  # noqa: E501
            currency (str): Choose the currency of value field (Default: USD). [optional] if omitted the server will use the default value of "usd"  # noqa: E501
            timestamp (datetime): When this payment is created. (UTC Timestamp). [optional]  # noqa: E501
            webpay_code (str): Code for using web payment UI. Check webpay documentation for details.. [optional]  # noqa: E501
            metadata (MetadataInput): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.account = account
        self.amount = amount
        self.value = value
        self.description = description
        self.payment_request = payment_request
        self.lninvoice = lninvoice
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, account, amount, value, description, payment_request, lninvoice, *args, **kwargs):  # noqa: E501
        """PaymentOutput - a model defined in OpenAPI

        Args:
            account (int): Receiver of this payment
            amount (int): Bitcoin amount in Satoshi units
            value (str): Value of the payment at the time of creation. (Example: 3.14 USD)
            description (str): Display the description of payment
            payment_request (str):
            lninvoice (LightningInvoiceOutput):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            uuid (str): [optional]  # noqa: E501
            object (str): [optional] if omitted the server will use the default value of "charge"  # noqa: E501
            amount_settled (int): [optional]  # noqa: E501
            settled (bool): [optional] if omitted the server will use the default value of False  # noqa: E501
            currency (str): Choose the currency of value field (Default: USD). [optional] if omitted the server will use the default value of "usd"  # noqa: E501
            timestamp (datetime): When this payment is created. (UTC Timestamp). [optional]  # noqa: E501
            webpay_code (str): Code for using web payment UI. Check webpay documentation for details.. [optional]  # noqa: E501
            metadata (MetadataInput): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.account = account
        self.amount = amount
        self.value = value
        self.description = description
        self.payment_request = payment_request
        self.lninvoice = lninvoice
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")

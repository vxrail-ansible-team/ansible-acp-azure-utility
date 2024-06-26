# coding: utf-8

"""
    Dell APEX Cloud Platform for Microsoft Azure REST API

    Dell APEX Cloud Platform REST API provides a programmatic interface for performing administrative tasks on Dell APEX Cloud Platform for Microsoft Azure. The data is available in JSON format.  # noqa: E501

    OpenAPI spec version: 1.0.000
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class IntentSpec(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'traffic_type': 'list[str]',
        'adapter': 'list[str]',
        'override_virtual_switch_configuration': 'bool',
        'virtual_switch_configuration_overrides': 'IntentSpecVirtualSwitchConfigurationOverrides',
        'override_qos_policy': 'bool',
        'qos_policy_overrides': 'IntentSpecQosPolicyOverrides',
        'override_adapter_property': 'bool',
        'adapter_property_overrides': 'IntentSpecAdapterPropertyOverrides'
    }

    attribute_map = {
        'name': 'name',
        'traffic_type': 'traffic_type',
        'adapter': 'adapter',
        'override_virtual_switch_configuration': 'override_virtual_switch_configuration',
        'virtual_switch_configuration_overrides': 'virtual_switch_configuration_overrides',
        'override_qos_policy': 'override_qos_policy',
        'qos_policy_overrides': 'qos_policy_overrides',
        'override_adapter_property': 'override_adapter_property',
        'adapter_property_overrides': 'adapter_property_overrides'
    }

    def __init__(self, name=None, traffic_type=None, adapter=None, override_virtual_switch_configuration=None, virtual_switch_configuration_overrides=None, override_qos_policy=None, qos_policy_overrides=None, override_adapter_property=None, adapter_property_overrides=None):  # noqa: E501
        """IntentSpec - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._traffic_type = None
        self._adapter = None
        self._override_virtual_switch_configuration = None
        self._virtual_switch_configuration_overrides = None
        self._override_qos_policy = None
        self._qos_policy_overrides = None
        self._override_adapter_property = None
        self._adapter_property_overrides = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if traffic_type is not None:
            self.traffic_type = traffic_type
        if adapter is not None:
            self.adapter = adapter
        if override_virtual_switch_configuration is not None:
            self.override_virtual_switch_configuration = override_virtual_switch_configuration
        if virtual_switch_configuration_overrides is not None:
            self.virtual_switch_configuration_overrides = virtual_switch_configuration_overrides
        if override_qos_policy is not None:
            self.override_qos_policy = override_qos_policy
        if qos_policy_overrides is not None:
            self.qos_policy_overrides = qos_policy_overrides
        if override_adapter_property is not None:
            self.override_adapter_property = override_adapter_property
        if adapter_property_overrides is not None:
            self.adapter_property_overrides = adapter_property_overrides

    @property
    def name(self):
        """Gets the name of this IntentSpec.  # noqa: E501

        Enter the name of the network.  # noqa: E501

        :return: The name of this IntentSpec.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IntentSpec.

        Enter the name of the network.  # noqa: E501

        :param name: The name of this IntentSpec.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def traffic_type(self):
        """Gets the traffic_type of this IntentSpec.  # noqa: E501

        Traffic type. The supported values are COMPUTE, MANAGEMENT, and STORAGE.  # noqa: E501

        :return: The traffic_type of this IntentSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._traffic_type

    @traffic_type.setter
    def traffic_type(self, traffic_type):
        """Sets the traffic_type of this IntentSpec.

        Traffic type. The supported values are COMPUTE, MANAGEMENT, and STORAGE.  # noqa: E501

        :param traffic_type: The traffic_type of this IntentSpec.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["COMPUTE", "MANAGEMENT", "STORAGE"]  # noqa: E501
        if not set(traffic_type).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `traffic_type` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(traffic_type) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._traffic_type = traffic_type

    @property
    def adapter(self):
        """Gets the adapter of this IntentSpec.  # noqa: E501

        The array of network interfaces that will be used for the declared intent.  # noqa: E501

        :return: The adapter of this IntentSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._adapter

    @adapter.setter
    def adapter(self, adapter):
        """Sets the adapter of this IntentSpec.

        The array of network interfaces that will be used for the declared intent.  # noqa: E501

        :param adapter: The adapter of this IntentSpec.  # noqa: E501
        :type: list[str]
        """

        self._adapter = adapter

    @property
    def override_virtual_switch_configuration(self):
        """Gets the override_virtual_switch_configuration of this IntentSpec.  # noqa: E501

        Set the toggle parameter to true, to modify the default Virtual Switch settings.  # noqa: E501

        :return: The override_virtual_switch_configuration of this IntentSpec.  # noqa: E501
        :rtype: bool
        """
        return self._override_virtual_switch_configuration

    @override_virtual_switch_configuration.setter
    def override_virtual_switch_configuration(self, override_virtual_switch_configuration):
        """Sets the override_virtual_switch_configuration of this IntentSpec.

        Set the toggle parameter to true, to modify the default Virtual Switch settings.  # noqa: E501

        :param override_virtual_switch_configuration: The override_virtual_switch_configuration of this IntentSpec.  # noqa: E501
        :type: bool
        """

        self._override_virtual_switch_configuration = override_virtual_switch_configuration

    @property
    def virtual_switch_configuration_overrides(self):
        """Gets the virtual_switch_configuration_overrides of this IntentSpec.  # noqa: E501


        :return: The virtual_switch_configuration_overrides of this IntentSpec.  # noqa: E501
        :rtype: IntentSpecVirtualSwitchConfigurationOverrides
        """
        return self._virtual_switch_configuration_overrides

    @virtual_switch_configuration_overrides.setter
    def virtual_switch_configuration_overrides(self, virtual_switch_configuration_overrides):
        """Sets the virtual_switch_configuration_overrides of this IntentSpec.


        :param virtual_switch_configuration_overrides: The virtual_switch_configuration_overrides of this IntentSpec.  # noqa: E501
        :type: IntentSpecVirtualSwitchConfigurationOverrides
        """

        self._virtual_switch_configuration_overrides = virtual_switch_configuration_overrides

    @property
    def override_qos_policy(self):
        """Gets the override_qos_policy of this IntentSpec.  # noqa: E501

        Toggle parameter when the intention is to modify the default QoS policies.  # noqa: E501

        :return: The override_qos_policy of this IntentSpec.  # noqa: E501
        :rtype: bool
        """
        return self._override_qos_policy

    @override_qos_policy.setter
    def override_qos_policy(self, override_qos_policy):
        """Sets the override_qos_policy of this IntentSpec.

        Toggle parameter when the intention is to modify the default QoS policies.  # noqa: E501

        :param override_qos_policy: The override_qos_policy of this IntentSpec.  # noqa: E501
        :type: bool
        """

        self._override_qos_policy = override_qos_policy

    @property
    def qos_policy_overrides(self):
        """Gets the qos_policy_overrides of this IntentSpec.  # noqa: E501


        :return: The qos_policy_overrides of this IntentSpec.  # noqa: E501
        :rtype: IntentSpecQosPolicyOverrides
        """
        return self._qos_policy_overrides

    @qos_policy_overrides.setter
    def qos_policy_overrides(self, qos_policy_overrides):
        """Sets the qos_policy_overrides of this IntentSpec.


        :param qos_policy_overrides: The qos_policy_overrides of this IntentSpec.  # noqa: E501
        :type: IntentSpecQosPolicyOverrides
        """

        self._qos_policy_overrides = qos_policy_overrides

    @property
    def override_adapter_property(self):
        """Gets the override_adapter_property of this IntentSpec.  # noqa: E501

        Toggle parameter when the intention is to modify the default network adapter settings.  # noqa: E501

        :return: The override_adapter_property of this IntentSpec.  # noqa: E501
        :rtype: bool
        """
        return self._override_adapter_property

    @override_adapter_property.setter
    def override_adapter_property(self, override_adapter_property):
        """Sets the override_adapter_property of this IntentSpec.

        Toggle parameter when the intention is to modify the default network adapter settings.  # noqa: E501

        :param override_adapter_property: The override_adapter_property of this IntentSpec.  # noqa: E501
        :type: bool
        """

        self._override_adapter_property = override_adapter_property

    @property
    def adapter_property_overrides(self):
        """Gets the adapter_property_overrides of this IntentSpec.  # noqa: E501


        :return: The adapter_property_overrides of this IntentSpec.  # noqa: E501
        :rtype: IntentSpecAdapterPropertyOverrides
        """
        return self._adapter_property_overrides

    @adapter_property_overrides.setter
    def adapter_property_overrides(self, adapter_property_overrides):
        """Sets the adapter_property_overrides of this IntentSpec.


        :param adapter_property_overrides: The adapter_property_overrides of this IntentSpec.  # noqa: E501
        :type: IntentSpecAdapterPropertyOverrides
        """

        self._adapter_property_overrides = adapter_property_overrides

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(IntentSpec, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IntentSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

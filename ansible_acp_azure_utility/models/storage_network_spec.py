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

class StorageNetworkSpec(object):
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
        'network_adapter_name': 'str',
        'vlan_id': 'int'
    }

    attribute_map = {
        'network_adapter_name': 'network_adapter_name',
        'vlan_id': 'vlan_id'
    }

    def __init__(self, network_adapter_name=None, vlan_id=None):  # noqa: E501
        """StorageNetworkSpec - a model defined in Swagger"""  # noqa: E501
        self._network_adapter_name = None
        self._vlan_id = None
        self.discriminator = None
        if network_adapter_name is not None:
            self.network_adapter_name = network_adapter_name
        if vlan_id is not None:
            self.vlan_id = vlan_id

    @property
    def network_adapter_name(self):
        """Gets the network_adapter_name of this StorageNetworkSpec.  # noqa: E501

        Name of the network adapter for storage network.  # noqa: E501

        :return: The network_adapter_name of this StorageNetworkSpec.  # noqa: E501
        :rtype: str
        """
        return self._network_adapter_name

    @network_adapter_name.setter
    def network_adapter_name(self, network_adapter_name):
        """Sets the network_adapter_name of this StorageNetworkSpec.

        Name of the network adapter for storage network.  # noqa: E501

        :param network_adapter_name: The network_adapter_name of this StorageNetworkSpec.  # noqa: E501
        :type: str
        """

        self._network_adapter_name = network_adapter_name

    @property
    def vlan_id(self):
        """Gets the vlan_id of this StorageNetworkSpec.  # noqa: E501

        The Vlan ID is specified for the VLAN storage network. This setting is applied to the network interfaces that route the storage and VM migration traffic. Supported values are 1 to 4094.  # noqa: E501

        :return: The vlan_id of this StorageNetworkSpec.  # noqa: E501
        :rtype: int
        """
        return self._vlan_id

    @vlan_id.setter
    def vlan_id(self, vlan_id):
        """Sets the vlan_id of this StorageNetworkSpec.

        The Vlan ID is specified for the VLAN storage network. This setting is applied to the network interfaces that route the storage and VM migration traffic. Supported values are 1 to 4094.  # noqa: E501

        :param vlan_id: The vlan_id of this StorageNetworkSpec.  # noqa: E501
        :type: int
        """

        self._vlan_id = vlan_id

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
        if issubclass(StorageNetworkSpec, dict):
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
        if not isinstance(other, StorageNetworkSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

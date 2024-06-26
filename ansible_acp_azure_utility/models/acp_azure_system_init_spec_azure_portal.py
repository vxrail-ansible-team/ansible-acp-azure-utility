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

class ACPAzureSystemInitSpecAzurePortal(object):
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
        'subscription_id': 'str',
        'cloud': 'str',
        'region': 'str',
        'service_principal': 'ACPAzureSystemInitSpecAzurePortalServicePrincipal',
        'resource_group': 'str',
        'resource_name': 'str'
    }

    attribute_map = {
        'subscription_id': 'subscription_id',
        'cloud': 'cloud',
        'region': 'region',
        'service_principal': 'service_principal',
        'resource_group': 'resource_group',
        'resource_name': 'resource_name'
    }

    def __init__(self, subscription_id=None, cloud=None, region=None, service_principal=None, resource_group=None, resource_name=None):  # noqa: E501
        """ACPAzureSystemInitSpecAzurePortal - a model defined in Swagger"""  # noqa: E501
        self._subscription_id = None
        self._cloud = None
        self._region = None
        self._service_principal = None
        self._resource_group = None
        self._resource_name = None
        self.discriminator = None
        if subscription_id is not None:
            self.subscription_id = subscription_id
        if cloud is not None:
            self.cloud = cloud
        if region is not None:
            self.region = region
        if service_principal is not None:
            self.service_principal = service_principal
        if resource_group is not None:
            self.resource_group = resource_group
        if resource_name is not None:
            self.resource_name = resource_name

    @property
    def subscription_id(self):
        """Gets the subscription_id of this ACPAzureSystemInitSpecAzurePortal.  # noqa: E501

        Specifies the Azure subscription ID for the cluster deployment.  # noqa: E501

        :return: The subscription_id of this ACPAzureSystemInitSpecAzurePortal.  # noqa: E501
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this ACPAzureSystemInitSpecAzurePortal.

        Specifies the Azure subscription ID for the cluster deployment.  # noqa: E501

        :param subscription_id: The subscription_id of this ACPAzureSystemInitSpecAzurePortal.  # noqa: E501
        :type: str
        """

        self._subscription_id = subscription_id

    @property
    def cloud(self):
        """Gets the cloud of this ACPAzureSystemInitSpecAzurePortal.  # noqa: E501

        Specifies the Azure Environment.  # noqa: E501

        :return: The cloud of this ACPAzureSystemInitSpecAzurePortal.  # noqa: E501
        :rtype: str
        """
        return self._cloud

    @cloud.setter
    def cloud(self, cloud):
        """Sets the cloud of this ACPAzureSystemInitSpecAzurePortal.

        Specifies the Azure Environment.  # noqa: E501

        :param cloud: The cloud of this ACPAzureSystemInitSpecAzurePortal.  # noqa: E501
        :type: str
        """
        allowed_values = ["AZURE_CLOUD", "AZURE_CLOUD_CHINA", "AZURE_CLOUD_US_GOVERNMENT"]  # noqa: E501
        if cloud not in allowed_values:
            raise ValueError(
                "Invalid value for `cloud` ({0}), must be one of {1}"  # noqa: E501
                .format(cloud, allowed_values)
            )

        self._cloud = cloud

    @property
    def region(self):
        """Gets the region of this ACPAzureSystemInitSpecAzurePortal.  # noqa: E501

        Specifies the region to create the resource in Azure portal. The supported regions refer to https://learn.microsoft.com/en-us/azure-stack/hci/concepts/system-requirements?tabs=azure-public#azure-requirements  # noqa: E501

        :return: The region of this ACPAzureSystemInitSpecAzurePortal.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ACPAzureSystemInitSpecAzurePortal.

        Specifies the region to create the resource in Azure portal. The supported regions refer to https://learn.microsoft.com/en-us/azure-stack/hci/concepts/system-requirements?tabs=azure-public#azure-requirements  # noqa: E501

        :param region: The region of this ACPAzureSystemInitSpecAzurePortal.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def service_principal(self):
        """Gets the service_principal of this ACPAzureSystemInitSpecAzurePortal.  # noqa: E501


        :return: The service_principal of this ACPAzureSystemInitSpecAzurePortal.  # noqa: E501
        :rtype: ACPAzureSystemInitSpecAzurePortalServicePrincipal
        """
        return self._service_principal

    @service_principal.setter
    def service_principal(self, service_principal):
        """Sets the service_principal of this ACPAzureSystemInitSpecAzurePortal.


        :param service_principal: The service_principal of this ACPAzureSystemInitSpecAzurePortal.  # noqa: E501
        :type: ACPAzureSystemInitSpecAzurePortalServicePrincipal
        """

        self._service_principal = service_principal

    @property
    def resource_group(self):
        """Gets the resource_group of this ACPAzureSystemInitSpecAzurePortal.  # noqa: E501

        Specifies the Azure Resource Group name.  # noqa: E501

        :return: The resource_group of this ACPAzureSystemInitSpecAzurePortal.  # noqa: E501
        :rtype: str
        """
        return self._resource_group

    @resource_group.setter
    def resource_group(self, resource_group):
        """Sets the resource_group of this ACPAzureSystemInitSpecAzurePortal.

        Specifies the Azure Resource Group name.  # noqa: E501

        :param resource_group: The resource_group of this ACPAzureSystemInitSpecAzurePortal.  # noqa: E501
        :type: str
        """

        self._resource_group = resource_group

    @property
    def resource_name(self):
        """Gets the resource_name of this ACPAzureSystemInitSpecAzurePortal.  # noqa: E501

        Specifies the Azure Resource name.  # noqa: E501

        :return: The resource_name of this ACPAzureSystemInitSpecAzurePortal.  # noqa: E501
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this ACPAzureSystemInitSpecAzurePortal.

        Specifies the Azure Resource name.  # noqa: E501

        :param resource_name: The resource_name of this ACPAzureSystemInitSpecAzurePortal.  # noqa: E501
        :type: str
        """

        self._resource_name = resource_name

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
        if issubclass(ACPAzureSystemInitSpecAzurePortal, dict):
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
        if not isinstance(other, ACPAzureSystemInitSpecAzurePortal):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
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

class SystemInitStatusInfo(object):
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
        'id': 'str',
        'state': 'str',
        'step': 'str',
        'owner': 'str',
        'progress': 'int',
        'start_time': 'int',
        'detail': 'str',
        'error': 'str',
        'end_time': 'int',
        'extension': 'SystemInitStatusInfoExtension',
        'partial_pass': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'state': 'state',
        'step': 'step',
        'owner': 'owner',
        'progress': 'progress',
        'start_time': 'start_time',
        'detail': 'detail',
        'error': 'error',
        'end_time': 'end_time',
        'extension': 'extension',
        'partial_pass': 'partial_pass'
    }

    def __init__(self, id=None, state=None, step=None, owner=None, progress=None, start_time=None, detail=None, error=None, end_time=None, extension=None, partial_pass=None):  # noqa: E501
        """SystemInitStatusInfo - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._state = None
        self._step = None
        self._owner = None
        self._progress = None
        self._start_time = None
        self._detail = None
        self._error = None
        self._end_time = None
        self._extension = None
        self._partial_pass = None
        self.discriminator = None
        self.id = id
        if state is not None:
            self.state = state
        if step is not None:
            self.step = step
        if owner is not None:
            self.owner = owner
        self.progress = progress
        if start_time is not None:
            self.start_time = start_time
        if detail is not None:
            self.detail = detail
        if error is not None:
            self.error = error
        if end_time is not None:
            self.end_time = end_time
        if extension is not None:
            self.extension = extension
        if partial_pass is not None:
            self.partial_pass = partial_pass

    @property
    def id(self):
        """Gets the id of this SystemInitStatusInfo.  # noqa: E501

        The returned request_id from a running cluster configuration (POST /v1/system/initialize)  # noqa: E501

        :return: The id of this SystemInitStatusInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SystemInitStatusInfo.

        The returned request_id from a running cluster configuration (POST /v1/system/initialize)  # noqa: E501

        :param id: The id of this SystemInitStatusInfo.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def state(self):
        """Gets the state of this SystemInitStatusInfo.  # noqa: E501

        The current state of execution  # noqa: E501

        :return: The state of this SystemInitStatusInfo.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this SystemInitStatusInfo.

        The current state of execution  # noqa: E501

        :param state: The state of this SystemInitStatusInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["NOT_STARTED", "STARTED", "IN_PROGRESS", "FAILED", "COMPLETED", "SKIPPED"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def step(self):
        """Gets the step of this SystemInitStatusInfo.  # noqa: E501

        The current step being run  # noqa: E501

        :return: The step of this SystemInitStatusInfo.  # noqa: E501
        :rtype: str
        """
        return self._step

    @step.setter
    def step(self, step):
        """Sets the step of this SystemInitStatusInfo.

        The current step being run  # noqa: E501

        :param step: The step of this SystemInitStatusInfo.  # noqa: E501
        :type: str
        """

        self._step = step

    @property
    def owner(self):
        """Gets the owner of this SystemInitStatusInfo.  # noqa: E501

        The owner of the request  # noqa: E501

        :return: The owner of this SystemInitStatusInfo.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this SystemInitStatusInfo.

        The owner of the request  # noqa: E501

        :param owner: The owner of this SystemInitStatusInfo.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def progress(self):
        """Gets the progress of this SystemInitStatusInfo.  # noqa: E501

        The progress of the current execution (as a percentage)  # noqa: E501

        :return: The progress of this SystemInitStatusInfo.  # noqa: E501
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this SystemInitStatusInfo.

        The progress of the current execution (as a percentage)  # noqa: E501

        :param progress: The progress of this SystemInitStatusInfo.  # noqa: E501
        :type: int
        """
        if progress is None:
            raise ValueError("Invalid value for `progress`, must not be `None`")  # noqa: E501

        self._progress = progress

    @property
    def start_time(self):
        """Gets the start_time of this SystemInitStatusInfo.  # noqa: E501

        The start time of the current execution  # noqa: E501

        :return: The start_time of this SystemInitStatusInfo.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this SystemInitStatusInfo.

        The start time of the current execution  # noqa: E501

        :param start_time: The start_time of this SystemInitStatusInfo.  # noqa: E501
        :type: int
        """

        self._start_time = start_time

    @property
    def detail(self):
        """Gets the detail of this SystemInitStatusInfo.  # noqa: E501

        The detailed information after the step is executed  # noqa: E501

        :return: The detail of this SystemInitStatusInfo.  # noqa: E501
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this SystemInitStatusInfo.

        The detailed information after the step is executed  # noqa: E501

        :param detail: The detail of this SystemInitStatusInfo.  # noqa: E501
        :type: str
        """

        self._detail = detail

    @property
    def error(self):
        """Gets the error of this SystemInitStatusInfo.  # noqa: E501

        The error information of the current execution  # noqa: E501

        :return: The error of this SystemInitStatusInfo.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this SystemInitStatusInfo.

        The error information of the current execution  # noqa: E501

        :param error: The error of this SystemInitStatusInfo.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def end_time(self):
        """Gets the end_time of this SystemInitStatusInfo.  # noqa: E501

        The end time of the current execution  # noqa: E501

        :return: The end_time of this SystemInitStatusInfo.  # noqa: E501
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this SystemInitStatusInfo.

        The end time of the current execution  # noqa: E501

        :param end_time: The end_time of this SystemInitStatusInfo.  # noqa: E501
        :type: int
        """

        self._end_time = end_time

    @property
    def extension(self):
        """Gets the extension of this SystemInitStatusInfo.  # noqa: E501


        :return: The extension of this SystemInitStatusInfo.  # noqa: E501
        :rtype: SystemInitStatusInfoExtension
        """
        return self._extension

    @extension.setter
    def extension(self, extension):
        """Sets the extension of this SystemInitStatusInfo.


        :param extension: The extension of this SystemInitStatusInfo.  # noqa: E501
        :type: SystemInitStatusInfoExtension
        """

        self._extension = extension

    @property
    def partial_pass(self):
        """Gets the partial_pass of this SystemInitStatusInfo.  # noqa: E501

        Indicates that not all hosts are successfully OS provisioned or registered in Azure portal.  # noqa: E501

        :return: The partial_pass of this SystemInitStatusInfo.  # noqa: E501
        :rtype: bool
        """
        return self._partial_pass

    @partial_pass.setter
    def partial_pass(self, partial_pass):
        """Sets the partial_pass of this SystemInitStatusInfo.

        Indicates that not all hosts are successfully OS provisioned or registered in Azure portal.  # noqa: E501

        :param partial_pass: The partial_pass of this SystemInitStatusInfo.  # noqa: E501
        :type: bool
        """

        self._partial_pass = partial_pass

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
        if issubclass(SystemInitStatusInfo, dict):
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
        if not isinstance(other, SystemInitStatusInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

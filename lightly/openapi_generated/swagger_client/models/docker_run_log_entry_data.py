# coding: utf-8

"""
    Lightly API

    Lightly.ai enables you to do self-supervised learning in an easy and intuitive way. The lightly.ai OpenAPI spec defines how one can interact with our REST API to unleash the full potential of lightly.ai  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@lightly.ai
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from lightly.openapi_generated.swagger_client.configuration import Configuration


class DockerRunLogEntryData(object):
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
        'msg': 'str',
        'ts': 'Timestamp',
        'state': 'DockerRunState',
        'level': 'DockerRunLogLevel'
    }

    attribute_map = {
        'msg': 'msg',
        'ts': 'ts',
        'state': 'state',
        'level': 'level'
    }

    def __init__(self, msg=None, ts=None, state=None, level=None, _configuration=None):  # noqa: E501
        """DockerRunLogEntryData - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._msg = None
        self._ts = None
        self._state = None
        self._level = None
        self.discriminator = None

        self.msg = msg
        self.ts = ts
        self.state = state
        self.level = level

    @property
    def msg(self):
        """Gets the msg of this DockerRunLogEntryData.  # noqa: E501


        :return: The msg of this DockerRunLogEntryData.  # noqa: E501
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg):
        """Sets the msg of this DockerRunLogEntryData.


        :param msg: The msg of this DockerRunLogEntryData.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and msg is None:
            raise ValueError("Invalid value for `msg`, must not be `None`")  # noqa: E501

        self._msg = msg

    @property
    def ts(self):
        """Gets the ts of this DockerRunLogEntryData.  # noqa: E501


        :return: The ts of this DockerRunLogEntryData.  # noqa: E501
        :rtype: Timestamp
        """
        return self._ts

    @ts.setter
    def ts(self, ts):
        """Sets the ts of this DockerRunLogEntryData.


        :param ts: The ts of this DockerRunLogEntryData.  # noqa: E501
        :type: Timestamp
        """
        if self._configuration.client_side_validation and ts is None:
            raise ValueError("Invalid value for `ts`, must not be `None`")  # noqa: E501

        self._ts = ts

    @property
    def state(self):
        """Gets the state of this DockerRunLogEntryData.  # noqa: E501


        :return: The state of this DockerRunLogEntryData.  # noqa: E501
        :rtype: DockerRunState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this DockerRunLogEntryData.


        :param state: The state of this DockerRunLogEntryData.  # noqa: E501
        :type: DockerRunState
        """
        if self._configuration.client_side_validation and state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

    @property
    def level(self):
        """Gets the level of this DockerRunLogEntryData.  # noqa: E501


        :return: The level of this DockerRunLogEntryData.  # noqa: E501
        :rtype: DockerRunLogLevel
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this DockerRunLogEntryData.


        :param level: The level of this DockerRunLogEntryData.  # noqa: E501
        :type: DockerRunLogLevel
        """
        if self._configuration.client_side_validation and level is None:
            raise ValueError("Invalid value for `level`, must not be `None`")  # noqa: E501

        self._level = level

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
        if issubclass(DockerRunLogEntryData, dict):
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
        if not isinstance(other, DockerRunLogEntryData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DockerRunLogEntryData):
            return True

        return self.to_dict() != other.to_dict()
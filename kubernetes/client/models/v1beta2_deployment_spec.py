# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: release-1.16
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class V1beta2DeploymentSpec(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'min_ready_seconds': 'int',
        'paused': 'bool',
        'progress_deadline_seconds': 'int',
        'replicas': 'int',
        'revision_history_limit': 'int',
        'selector': 'V1LabelSelector',
        'strategy': 'V1beta2DeploymentStrategy',
        'template': 'V1PodTemplateSpec'
    }

    attribute_map = {
        'min_ready_seconds': 'minReadySeconds',
        'paused': 'paused',
        'progress_deadline_seconds': 'progressDeadlineSeconds',
        'replicas': 'replicas',
        'revision_history_limit': 'revisionHistoryLimit',
        'selector': 'selector',
        'strategy': 'strategy',
        'template': 'template'
    }

    def __init__(self, min_ready_seconds=None, paused=None, progress_deadline_seconds=None, replicas=None, revision_history_limit=None, selector=None, strategy=None, template=None):  # noqa: E501
        """V1beta2DeploymentSpec - a model defined in OpenAPI"""  # noqa: E501

        self._min_ready_seconds = None
        self._paused = None
        self._progress_deadline_seconds = None
        self._replicas = None
        self._revision_history_limit = None
        self._selector = None
        self._strategy = None
        self._template = None
        self.discriminator = None

        if min_ready_seconds is not None:
            self.min_ready_seconds = min_ready_seconds
        if paused is not None:
            self.paused = paused
        if progress_deadline_seconds is not None:
            self.progress_deadline_seconds = progress_deadline_seconds
        if replicas is not None:
            self.replicas = replicas
        if revision_history_limit is not None:
            self.revision_history_limit = revision_history_limit
        self.selector = selector
        if strategy is not None:
            self.strategy = strategy
        self.template = template

    @property
    def min_ready_seconds(self):
        """Gets the min_ready_seconds of this V1beta2DeploymentSpec.  # noqa: E501

        Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready)  # noqa: E501

        :return: The min_ready_seconds of this V1beta2DeploymentSpec.  # noqa: E501
        :rtype: int
        """
        return self._min_ready_seconds

    @min_ready_seconds.setter
    def min_ready_seconds(self, min_ready_seconds):
        """Sets the min_ready_seconds of this V1beta2DeploymentSpec.

        Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready)  # noqa: E501

        :param min_ready_seconds: The min_ready_seconds of this V1beta2DeploymentSpec.  # noqa: E501
        :type: int
        """

        self._min_ready_seconds = min_ready_seconds

    @property
    def paused(self):
        """Gets the paused of this V1beta2DeploymentSpec.  # noqa: E501

        Indicates that the deployment is paused.  # noqa: E501

        :return: The paused of this V1beta2DeploymentSpec.  # noqa: E501
        :rtype: bool
        """
        return self._paused

    @paused.setter
    def paused(self, paused):
        """Sets the paused of this V1beta2DeploymentSpec.

        Indicates that the deployment is paused.  # noqa: E501

        :param paused: The paused of this V1beta2DeploymentSpec.  # noqa: E501
        :type: bool
        """

        self._paused = paused

    @property
    def progress_deadline_seconds(self):
        """Gets the progress_deadline_seconds of this V1beta2DeploymentSpec.  # noqa: E501

        The maximum time in seconds for a deployment to make progress before it is considered to be failed. The deployment controller will continue to process failed deployments and a condition with a ProgressDeadlineExceeded reason will be surfaced in the deployment status. Note that progress will not be estimated during the time a deployment is paused. Defaults to 600s.  # noqa: E501

        :return: The progress_deadline_seconds of this V1beta2DeploymentSpec.  # noqa: E501
        :rtype: int
        """
        return self._progress_deadline_seconds

    @progress_deadline_seconds.setter
    def progress_deadline_seconds(self, progress_deadline_seconds):
        """Sets the progress_deadline_seconds of this V1beta2DeploymentSpec.

        The maximum time in seconds for a deployment to make progress before it is considered to be failed. The deployment controller will continue to process failed deployments and a condition with a ProgressDeadlineExceeded reason will be surfaced in the deployment status. Note that progress will not be estimated during the time a deployment is paused. Defaults to 600s.  # noqa: E501

        :param progress_deadline_seconds: The progress_deadline_seconds of this V1beta2DeploymentSpec.  # noqa: E501
        :type: int
        """

        self._progress_deadline_seconds = progress_deadline_seconds

    @property
    def replicas(self):
        """Gets the replicas of this V1beta2DeploymentSpec.  # noqa: E501

        Number of desired pods. This is a pointer to distinguish between explicit zero and not specified. Defaults to 1.  # noqa: E501

        :return: The replicas of this V1beta2DeploymentSpec.  # noqa: E501
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        """Sets the replicas of this V1beta2DeploymentSpec.

        Number of desired pods. This is a pointer to distinguish between explicit zero and not specified. Defaults to 1.  # noqa: E501

        :param replicas: The replicas of this V1beta2DeploymentSpec.  # noqa: E501
        :type: int
        """

        self._replicas = replicas

    @property
    def revision_history_limit(self):
        """Gets the revision_history_limit of this V1beta2DeploymentSpec.  # noqa: E501

        The number of old ReplicaSets to retain to allow rollback. This is a pointer to distinguish between explicit zero and not specified. Defaults to 10.  # noqa: E501

        :return: The revision_history_limit of this V1beta2DeploymentSpec.  # noqa: E501
        :rtype: int
        """
        return self._revision_history_limit

    @revision_history_limit.setter
    def revision_history_limit(self, revision_history_limit):
        """Sets the revision_history_limit of this V1beta2DeploymentSpec.

        The number of old ReplicaSets to retain to allow rollback. This is a pointer to distinguish between explicit zero and not specified. Defaults to 10.  # noqa: E501

        :param revision_history_limit: The revision_history_limit of this V1beta2DeploymentSpec.  # noqa: E501
        :type: int
        """

        self._revision_history_limit = revision_history_limit

    @property
    def selector(self):
        """Gets the selector of this V1beta2DeploymentSpec.  # noqa: E501


        :return: The selector of this V1beta2DeploymentSpec.  # noqa: E501
        :rtype: V1LabelSelector
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """Sets the selector of this V1beta2DeploymentSpec.


        :param selector: The selector of this V1beta2DeploymentSpec.  # noqa: E501
        :type: V1LabelSelector
        """
        if selector is None:
            raise ValueError("Invalid value for `selector`, must not be `None`")  # noqa: E501

        self._selector = selector

    @property
    def strategy(self):
        """Gets the strategy of this V1beta2DeploymentSpec.  # noqa: E501


        :return: The strategy of this V1beta2DeploymentSpec.  # noqa: E501
        :rtype: V1beta2DeploymentStrategy
        """
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        """Sets the strategy of this V1beta2DeploymentSpec.


        :param strategy: The strategy of this V1beta2DeploymentSpec.  # noqa: E501
        :type: V1beta2DeploymentStrategy
        """

        self._strategy = strategy

    @property
    def template(self):
        """Gets the template of this V1beta2DeploymentSpec.  # noqa: E501


        :return: The template of this V1beta2DeploymentSpec.  # noqa: E501
        :rtype: V1PodTemplateSpec
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this V1beta2DeploymentSpec.


        :param template: The template of this V1beta2DeploymentSpec.  # noqa: E501
        :type: V1PodTemplateSpec
        """
        if template is None:
            raise ValueError("Invalid value for `template`, must not be `None`")  # noqa: E501

        self._template = template

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1beta2DeploymentSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

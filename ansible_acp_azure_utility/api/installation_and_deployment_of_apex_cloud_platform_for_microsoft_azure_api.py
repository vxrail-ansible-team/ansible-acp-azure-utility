# coding: utf-8

"""
    Dell APEX Cloud Platform for Microsoft Azure REST API

    Dell APEX Cloud Platform REST API provides a programmatic interface for performing administrative tasks on Dell APEX Cloud Platform for Microsoft Azure. The data is available in JSON format.  # noqa: E501

    OpenAPI spec version: 1.0.000
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ansible_acp_azure_utility.api_client import ApiClient


class InstallationAndDeploymentOfAPEXCloudPlatformForMicrosoftAzureApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v1_system_initialize_nodes_get(self, **kwargs):  # noqa: E501
        """Get the auto-discovered nodes during bootstrap  # noqa: E501

        Retrieve the auto-discovered nodes during bootstrap  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_system_initialize_nodes_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[DiscoveredNodeInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_system_initialize_nodes_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v1_system_initialize_nodes_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def v1_system_initialize_nodes_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get the auto-discovered nodes during bootstrap  # noqa: E501

        Retrieve the auto-discovered nodes during bootstrap  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_system_initialize_nodes_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[DiscoveredNodeInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_system_initialize_nodes_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/system/initialize/nodes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[DiscoveredNodeInfo]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_system_initialize_post(self, body, mode, **kwargs):  # noqa: E501
        """Configure and deploy a new APEX Cloud Platform for Microsoft Azure cluster  # noqa: E501

        Configure and deploy a new APEX Cloud Platform for Microsoft Azure cluster  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_system_initialize_post(body, mode, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ACPAzureSystemInitSpec body: JSON configuration parameters to initialize the APEX Cloud Platform for Microsoft Azure cluster (required)
        :param str mode: If the mode is OS_PROVISION, then the Azure Stack HCI OS is installed on the specified hosts. If the mode is CLUSTER_DEPLOYMENT, then a new APEX Cloud Platform cluster is deployed. (required)
        :return: InlineResponse202
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_system_initialize_post_with_http_info(body, mode, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_system_initialize_post_with_http_info(body, mode, **kwargs)  # noqa: E501
            return data

    def v1_system_initialize_post_with_http_info(self, body, mode, **kwargs):  # noqa: E501
        """Configure and deploy a new APEX Cloud Platform for Microsoft Azure cluster  # noqa: E501

        Configure and deploy a new APEX Cloud Platform for Microsoft Azure cluster  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_system_initialize_post_with_http_info(body, mode, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ACPAzureSystemInitSpec body: JSON configuration parameters to initialize the APEX Cloud Platform for Microsoft Azure cluster (required)
        :param str mode: If the mode is OS_PROVISION, then the Azure Stack HCI OS is installed on the specified hosts. If the mode is CLUSTER_DEPLOYMENT, then a new APEX Cloud Platform cluster is deployed. (required)
        :return: InlineResponse202
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'mode']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_system_initialize_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `v1_system_initialize_post`")  # noqa: E501
        # verify the required parameter 'mode' is set
        if ('mode' not in params or
                params['mode'] is None):
            raise ValueError("Missing the required parameter `mode` when calling `v1_system_initialize_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'mode' in params:
            query_params.append(('mode', params['mode']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/system/initialize', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse202',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_system_initialize_status_get(self, mode, **kwargs):  # noqa: E501
        """Get the cluster configuration and deployment status  # noqa: E501

        Retrieve the cluster configuration and deployment status information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_system_initialize_status_get(mode, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str mode: If the mode is OS_PROVISION, then the installation progress and status of the Azure Stack HCI OS are retrieved. If the mode is CLUSTER_DEPLOYMENT, then the deployment progress and status of the cluster are retrieved. (required)
        :return: SystemInitStatusInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_system_initialize_status_get_with_http_info(mode, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_system_initialize_status_get_with_http_info(mode, **kwargs)  # noqa: E501
            return data

    def v1_system_initialize_status_get_with_http_info(self, mode, **kwargs):  # noqa: E501
        """Get the cluster configuration and deployment status  # noqa: E501

        Retrieve the cluster configuration and deployment status information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_system_initialize_status_get_with_http_info(mode, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str mode: If the mode is OS_PROVISION, then the installation progress and status of the Azure Stack HCI OS are retrieved. If the mode is CLUSTER_DEPLOYMENT, then the deployment progress and status of the cluster are retrieved. (required)
        :return: SystemInitStatusInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['mode']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_system_initialize_status_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'mode' is set
        if ('mode' not in params or
                params['mode'] is None):
            raise ValueError("Missing the required parameter `mode` when calling `v1_system_initialize_status_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'mode' in params:
            query_params.append(('mode', params['mode']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/system/initialize/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SystemInitStatusInfo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

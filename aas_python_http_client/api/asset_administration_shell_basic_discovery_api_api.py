# coding: utf-8

"""
    DotAAS Part 2 | HTTP/REST | Entire API Collection

    All APIs of the Specification of the [Specification of the Asset Administration Shell: Part 2](http://industrialdigitaltwin.org/en/content-hub) in one collection. Please not that this API is not intended to generate productive code but only for overview purposes.   Publisher: Industrial Digital Twin Association (IDTA) 2023\"  # noqa: E501

    OpenAPI spec version: V3.0.1
    Contact: info@idtwin.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from aas_python_http_client.api_client import ApiClient


class AssetAdministrationShellBasicDiscoveryAPIApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_all_asset_links_by_id(self, aas_identifier, **kwargs):  # noqa: E501
        """Deletes all specific Asset identifiers linked to an Asset Administration Shell to edit discoverable content  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_all_asset_links_by_id(aas_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_all_asset_links_by_id_with_http_info(aas_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_all_asset_links_by_id_with_http_info(aas_identifier, **kwargs)  # noqa: E501
            return data

    def delete_all_asset_links_by_id_with_http_info(self, aas_identifier, **kwargs):  # noqa: E501
        """Deletes all specific Asset identifiers linked to an Asset Administration Shell to edit discoverable content  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_all_asset_links_by_id_with_http_info(aas_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['aas_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_all_asset_links_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'aas_identifier' is set
        if ('aas_identifier' not in params or
                params['aas_identifier'] is None):
            raise ValueError("Missing the required parameter `aas_identifier` when calling `delete_all_asset_links_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'aas_identifier' in params:
            path_params['aasIdentifier'] = params['aas_identifier']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = self.api_client.configuration.get_auth_settings_keys()   # noqa: E501

        return self.api_client.call_api(
            '/lookup/shells/{aasIdentifier}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all_asset_administration_shell_ids_by_asset_link(self, **kwargs):  # noqa: E501
        """Returns a list of Asset Administration Shell ids linked to specific Asset identifiers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_asset_administration_shell_ids_by_asset_link(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] asset_ids: A list of specific Asset identifiers. Each Asset identifier is a base64-url-encoded [SpecificAssetId](https://api.swaggerhub.com/domains/Plattform_i40/Part1-MetaModel-Schemas/V3.0.1#/components/schemas/SpecificAssetId)
        :param int limit: The maximum number of elements in the response array
        :param str cursor: A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_asset_administration_shell_ids_by_asset_link_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_asset_administration_shell_ids_by_asset_link_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_asset_administration_shell_ids_by_asset_link_with_http_info(self, **kwargs):  # noqa: E501
        """Returns a list of Asset Administration Shell ids linked to specific Asset identifiers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_asset_administration_shell_ids_by_asset_link_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] asset_ids: A list of specific Asset identifiers. Each Asset identifier is a base64-url-encoded [SpecificAssetId](https://api.swaggerhub.com/domains/Plattform_i40/Part1-MetaModel-Schemas/V3.0.1#/components/schemas/SpecificAssetId)
        :param int limit: The maximum number of elements in the response array
        :param str cursor: A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['asset_ids', 'limit', 'cursor']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_asset_administration_shell_ids_by_asset_link" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'asset_ids' in params:
            query_params.append(('assetIds', params['asset_ids']))  # noqa: E501
            collection_formats['assetIds'] = 'multi'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = self.api_client.configuration.get_auth_settings_keys()   # noqa: E501

        return self.api_client.call_api(
            '/lookup/shells', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse200',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all_asset_links_by_id(self, aas_identifier, **kwargs):  # noqa: E501
        """Returns a list of specific Asset identifiers based on an Asset Administration Shell id to edit discoverable content  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_asset_links_by_id(aas_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) (required)
        :return: list[SpecificAssetId]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_asset_links_by_id_with_http_info(aas_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_all_asset_links_by_id_with_http_info(aas_identifier, **kwargs)  # noqa: E501
            return data

    def get_all_asset_links_by_id_with_http_info(self, aas_identifier, **kwargs):  # noqa: E501
        """Returns a list of specific Asset identifiers based on an Asset Administration Shell id to edit discoverable content  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_asset_links_by_id_with_http_info(aas_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) (required)
        :return: list[SpecificAssetId]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['aas_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_asset_links_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'aas_identifier' is set
        if ('aas_identifier' not in params or
                params['aas_identifier'] is None):
            raise ValueError("Missing the required parameter `aas_identifier` when calling `get_all_asset_links_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'aas_identifier' in params:
            path_params['aasIdentifier'] = params['aas_identifier']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = self.api_client.configuration.get_auth_settings_keys()   # noqa: E501

        return self.api_client.call_api(
            '/lookup/shells/{aasIdentifier}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SpecificAssetId]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_all_asset_links_by_id(self, body, aas_identifier, **kwargs):  # noqa: E501
        """Creates specific Asset identifiers linked to an Asset Administration Shell to edit discoverable content  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_all_asset_links_by_id(body, aas_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[SpecificAssetId] body: A list of specific Asset identifiers (required)
        :param str aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) (required)
        :return: list[SpecificAssetId]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_all_asset_links_by_id_with_http_info(body, aas_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.post_all_asset_links_by_id_with_http_info(body, aas_identifier, **kwargs)  # noqa: E501
            return data

    def post_all_asset_links_by_id_with_http_info(self, body, aas_identifier, **kwargs):  # noqa: E501
        """Creates specific Asset identifiers linked to an Asset Administration Shell to edit discoverable content  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_all_asset_links_by_id_with_http_info(body, aas_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[SpecificAssetId] body: A list of specific Asset identifiers (required)
        :param str aas_identifier: The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) (required)
        :return: list[SpecificAssetId]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'aas_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_all_asset_links_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_all_asset_links_by_id`")  # noqa: E501
        # verify the required parameter 'aas_identifier' is set
        if ('aas_identifier' not in params or
                params['aas_identifier'] is None):
            raise ValueError("Missing the required parameter `aas_identifier` when calling `post_all_asset_links_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'aas_identifier' in params:
            path_params['aasIdentifier'] = params['aas_identifier']  # noqa: E501

        query_params = []

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
        auth_settings = self.api_client.configuration.get_auth_settings_keys()   # noqa: E501

        return self.api_client.call_api(
            '/lookup/shells/{aasIdentifier}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SpecificAssetId]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

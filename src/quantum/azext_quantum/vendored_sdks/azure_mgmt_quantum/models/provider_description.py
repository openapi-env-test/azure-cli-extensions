# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ProviderDescription(Model):
    """Information about an offering. A provider offering is an entity that offers
    Targets to run Azure Quantum Jobs.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Unique provider's id.
    :type id: str
    :ivar name: Provider's display name.
    :vartype name: str
    :param properties: A list of provider-specific properties.
    :type properties: ~azure.quantum.models.ProviderProperties
    """

    _validation = {
        'name': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'ProviderProperties'},
    }

    def __init__(self, **kwargs):
        super(ProviderDescription, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.name = None
        self.properties = kwargs.get('properties', None)

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

from enum import Enum


class ProvisioningState(str, Enum):

    succeeded = "Succeeded"
    failed = "Failed"
    canceled = "Canceled"
    accepted = "Accepted"
    provisioning = "Provisioning"


class Status(str, Enum):

    not_yet_registered = "NotYetRegistered"
    connected_recently = "ConnectedRecently"
    not_connected_recently = "NotConnectedRecently"
    disconnected = "Disconnected"
    error = "Error"

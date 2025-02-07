# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_network_cl(cli_ctx, **kwargs):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from azext_network_manager.vendored_sdks import NetworkManagementClient
    return get_mgmt_service_client(cli_ctx, NetworkManagementClient, **kwargs)


def cf_activesecurityuserrule(cli_ctx, *_):
    return cf_network_cl(cli_ctx).active_security_user_rules


def cf_adminrulecollection(cli_ctx, *_):
    return cf_network_cl(cli_ctx).admin_rule_collections


def cf_adminrule(cli_ctx, *_):
    return cf_network_cl(cli_ctx).admin_rules


def cf_connectivityconfiguration(cli_ctx, *_):
    return cf_network_cl(cli_ctx).connectivity_configurations


def cf_listeffectivevirtualnetwork(cli_ctx, *_):
    return cf_network_cl(cli_ctx).list_effective_virtual_networks


def cf_effectivevirtualnetwork(cli_ctx, *_):
    return cf_network_cl(cli_ctx).effective_virtual_networks


def cf_networkmanagementclient(cli_ctx, *_):
    return cf_network_cl(cli_ctx)


def cf_networkgroup(cli_ctx, *_):
    return cf_network_cl(cli_ctx).network_groups


def cf_networkmanagercommit(cli_ctx, *_):
    return cf_network_cl(cli_ctx).network_manager_commits


def cf_networkmanagerdeploymentstatus(cli_ctx, *_):
    return cf_network_cl(cli_ctx).network_manager_deployment_status


def cf_networkmanager(cli_ctx, *_):
    return cf_network_cl(cli_ctx).network_managers


def cf_securityadminconfiguration(cli_ctx, *_):
    return cf_network_cl(cli_ctx).security_admin_configurations


def cf_securityuserconfiguration(cli_ctx, *_):
    return cf_network_cl(cli_ctx).security_user_configurations


def cf_userrulecollection(cli_ctx, *_):
    return cf_network_cl(cli_ctx).user_rule_collections


def cf_userrule(cli_ctx, *_):
    return cf_network_cl(cli_ctx).user_rules


def cf_scopeconnection(cli_ctx, *_):
    return cf_network_cl(cli_ctx).scope_connections


def cf_staticmembers(cli_ctx, *_):
    return cf_network_cl(cli_ctx).static_members


def cf_subscriptionconnection(cli_ctx, *_):
    return cf_network_cl(cli_ctx).subscription_network_manager_connections


def cf_managementgroupconnection(cli_ctx, *_):
    return cf_network_cl(cli_ctx).management_group_network_manager_connections

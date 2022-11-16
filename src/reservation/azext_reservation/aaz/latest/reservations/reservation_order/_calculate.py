# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "reservations reservation-order calculate",
)
class Calculate(AAZCommand):
    """Calculate price for placing a `ReservationOrder`.

    :example: Calculate price
        az reservations reservation-order calculate --applied-scope-type Shared --billing-scope 50000000-aaaa-bbbb-cccc-100000000002 --display-name name1 --quantity 1 --reserved-resource-type VirtualMachines --sku Standard_B1s --term P1Y --billing-plan Monthly --location eastus
    """

    _aaz_info = {
        "version": "2022-03-01",
        "resources": [
            ["mgmt-plane", "/providers/microsoft.capacity/calculateprice", "2022-03-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group "Body"

        _args_schema = cls._args_schema
        _args_schema.location = AAZStrArg(
            options=["--location"],
            arg_group="Body",
            help="The Azure Region where the reserved resource lives.",
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.applied_scope_type = AAZStrArg(
            options=["--applied-scope-type"],
            arg_group="Properties",
            help="Type of the Applied Scope.",
            enum={"Shared": "Shared", "Single": "Single"},
        )
        _args_schema.applied_scope = AAZListArg(
            options=["--applied-scope"],
            arg_group="Properties",
            help="Subscription that the benefit will be applied. Required if --applied-scope-type is Single. Do not specify if --applied-scope-type is Shared.",
        )
        _args_schema.billing_plan = AAZStrArg(
            options=["--billing-plan"],
            arg_group="Properties",
            help="Represent the billing plans.",
            enum={"Monthly": "Monthly", "Upfront": "Upfront"},
        )
        _args_schema.billing_scope = AAZStrArg(
            options=["--billing-scope"],
            arg_group="Properties",
            help="Subscription that will be charged for purchasing Reservation",
        )
        _args_schema.display_name = AAZStrArg(
            options=["--display-name"],
            arg_group="Properties",
            help="Friendly name of the Reservation",
        )
        _args_schema.quantity = AAZIntArg(
            options=["--quantity"],
            arg_group="Properties",
            help="Quantity of the SKUs that are part of the Reservation.",
        )
        _args_schema.renew = AAZBoolArg(
            options=["--renew"],
            arg_group="Properties",
            help="Setting this to true will automatically purchase a new reservation on the expiration date time.",
            default=False,
        )
        _args_schema.reserved_resource_type = AAZStrArg(
            options=["--reserved-resource-type"],
            arg_group="Properties",
            help="The type of the resource that is being reserved.",
            enum={"AVS": "AVS", "AppService": "AppService", "AzureDataExplorer": "AzureDataExplorer", "AzureFiles": "AzureFiles", "BlockBlob": "BlockBlob", "CosmosDb": "CosmosDb", "DataFactory": "DataFactory", "Databricks": "Databricks", "DedicatedHost": "DedicatedHost", "ManagedDisk": "ManagedDisk", "MariaDb": "MariaDb", "MySql": "MySql", "NetAppStorage": "NetAppStorage", "PostgreSql": "PostgreSql", "RedHat": "RedHat", "RedHatOsa": "RedHatOsa", "RedisCache": "RedisCache", "SapHana": "SapHana", "SqlAzureHybridBenefit": "SqlAzureHybridBenefit", "SqlDataWarehouse": "SqlDataWarehouse", "SqlDatabases": "SqlDatabases", "SqlEdge": "SqlEdge", "SuseLinux": "SuseLinux", "VMwareCloudSimple": "VMwareCloudSimple", "VirtualMachineSoftware": "VirtualMachineSoftware", "VirtualMachines": "VirtualMachines"},
        )
        _args_schema.term = AAZStrArg(
            options=["--term"],
            arg_group="Properties",
            help="Represent the term of Reservation.",
            enum={"P1Y": "P1Y", "P3Y": "P3Y", "P5Y": "P5Y"},
        )

        applied_scope = cls._args_schema.applied_scope
        applied_scope.Element = AAZStrArg()

        # define Arg Group "ReservedResourceProperties"

        _args_schema = cls._args_schema
        _args_schema.instance_flexibility = AAZStrArg(
            options=["--instance-flexibility"],
            arg_group="ReservedResourceProperties",
            help="Turning this on will apply the reservation discount to other VMs in the same VM size group. Only specify for VirtualMachines reserved resource type.",
            enum={"Off": "Off", "On": "On"},
        )

        # define Arg Group "Sku"

        _args_schema = cls._args_schema
        _args_schema.sku = AAZStrArg(
            options=["--sku"],
            arg_group="Sku",
            help="Sku name for purchasing",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.ReservationOrderCalculate(ctx=self.ctx)()
        self.post_operations()

    # @register_callback
    def pre_operations(self):
        pass

    # @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class ReservationOrderCalculate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/providers/Microsoft.Capacity/calculatePrice",
                **self.url_parameters
            )

        @property
        def method(self):
            return "POST"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-03-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("location", AAZStrType, ".location")
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("sku", AAZObjectType)

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("appliedScopeType", AAZStrType, ".applied_scope_type")
                properties.set_prop("appliedScopes", AAZListType, ".applied_scope")
                properties.set_prop("billingPlan", AAZStrType, ".billing_plan")
                properties.set_prop("billingScopeId", AAZStrType, ".billing_scope")
                properties.set_prop("displayName", AAZStrType, ".display_name")
                properties.set_prop("quantity", AAZIntType, ".quantity")
                properties.set_prop("renew", AAZBoolType, ".renew")
                properties.set_prop("reservedResourceProperties", AAZObjectType)
                properties.set_prop("reservedResourceType", AAZStrType, ".reserved_resource_type")
                properties.set_prop("term", AAZStrType, ".term")

            applied_scopes = _builder.get(".properties.appliedScopes")
            if applied_scopes is not None:
                applied_scopes.set_elements(AAZStrType, ".")

            reserved_resource_properties = _builder.get(".properties.reservedResourceProperties")
            if reserved_resource_properties is not None:
                reserved_resource_properties.set_prop("instanceFlexibility", AAZStrType, ".instance_flexibility")

            sku = _builder.get(".sku")
            if sku is not None:
                sku.set_prop("name", AAZStrType, ".sku")

            return self.serialize_content(_content_value)

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.properties = AAZObjectType()

            properties = cls._schema_on_200.properties
            properties.billing_currency_total = AAZObjectType(
                serialized_name="billingCurrencyTotal",
            )
            properties.grand_total = AAZFloatType(
                serialized_name="grandTotal",
            )
            properties.is_billing_partner_managed = AAZBoolType(
                serialized_name="isBillingPartnerManaged",
            )
            properties.is_tax_included = AAZBoolType(
                serialized_name="isTaxIncluded",
            )
            properties.net_total = AAZFloatType(
                serialized_name="netTotal",
            )
            properties.payment_schedule = AAZListType(
                serialized_name="paymentSchedule",
            )
            properties.pricing_currency_total = AAZObjectType(
                serialized_name="pricingCurrencyTotal",
            )
            properties.reservation_order_id = AAZStrType(
                serialized_name="reservationOrderId",
            )
            properties.sku_description = AAZStrType(
                serialized_name="skuDescription",
            )
            properties.sku_title = AAZStrType(
                serialized_name="skuTitle",
            )
            properties.tax_total = AAZFloatType(
                serialized_name="taxTotal",
            )

            billing_currency_total = cls._schema_on_200.properties.billing_currency_total
            billing_currency_total.amount = AAZFloatType()
            billing_currency_total.currency_code = AAZStrType(
                serialized_name="currencyCode",
            )

            payment_schedule = cls._schema_on_200.properties.payment_schedule
            payment_schedule.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.payment_schedule.Element
            _element.billing_account = AAZStrType(
                serialized_name="billingAccount",
            )
            _element.billing_currency_total = AAZObjectType(
                serialized_name="billingCurrencyTotal",
            )
            _build_schema_price_read(_element.billing_currency_total)
            _element.due_date = AAZStrType(
                serialized_name="dueDate",
            )
            _element.extended_status_info = AAZObjectType(
                serialized_name="extendedStatusInfo",
            )
            _element.payment_date = AAZStrType(
                serialized_name="paymentDate",
            )
            _element.pricing_currency_total = AAZObjectType(
                serialized_name="pricingCurrencyTotal",
            )
            _build_schema_price_read(_element.pricing_currency_total)
            _element.status = AAZStrType()

            extended_status_info = cls._schema_on_200.properties.payment_schedule.Element.extended_status_info
            extended_status_info.message = AAZStrType()
            extended_status_info.status_code = AAZStrType(
                serialized_name="statusCode",
            )

            pricing_currency_total = cls._schema_on_200.properties.pricing_currency_total
            pricing_currency_total.amount = AAZFloatType()
            pricing_currency_total.currency_code = AAZStrType(
                serialized_name="currencyCode",
            )

            return cls._schema_on_200


_schema_price_read = None


def _build_schema_price_read(_schema):
    global _schema_price_read
    if _schema_price_read is not None:
        _schema.amount = _schema_price_read.amount
        _schema.currency_code = _schema_price_read.currency_code
        return

    _schema_price_read = AAZObjectType()

    price_read = _schema_price_read
    price_read.amount = AAZFloatType()
    price_read.currency_code = AAZStrType(
        serialized_name="currencyCode",
    )

    _schema.amount = _schema_price_read.amount
    _schema.currency_code = _schema_price_read.currency_code


__all__ = ["Calculate"]

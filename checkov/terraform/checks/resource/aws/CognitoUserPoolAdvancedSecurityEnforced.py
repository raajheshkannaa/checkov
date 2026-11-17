from checkov.common.models.enums import CheckCategories
from checkov.terraform.checks.resource.base_resource_value_check import BaseResourceValueCheck


class CognitoUserPoolAdvancedSecurityEnforced(BaseResourceValueCheck):
    def __init__(self) -> None:
        name = "Ensure Cognito user pool advanced security mode is set to ENFORCED"
        id = "CKV_AWS_395"
        supported_resources = ("aws_cognito_user_pool",)
        categories = (CheckCategories.GENERAL_SECURITY,)
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def get_inspected_key(self) -> str:
        return "user_pool_add_ons/[0]/advanced_security_mode"

    def get_expected_value(self) -> str:
        return "ENFORCED"


check = CognitoUserPoolAdvancedSecurityEnforced()

# coding: utf-8

# flake8: noqa

"""
    AISF API

    This API gives you the ability to interact with AISF's neural networks

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from ai_core_api_client.api.ai_api import AiApi
from ai_core_api_client.api.company_api import CompanyApi

# import ApiClient
from ai_core_api_client.api_response import ApiResponse
from ai_core_api_client.api_client import ApiClient
from ai_core_api_client.configuration import Configuration
from ai_core_api_client.exceptions import OpenApiException
from ai_core_api_client.exceptions import ApiTypeError
from ai_core_api_client.exceptions import ApiValueError
from ai_core_api_client.exceptions import ApiKeyError
from ai_core_api_client.exceptions import ApiAttributeError
from ai_core_api_client.exceptions import ApiException

# import models into sdk package
from ai_core_api_client.models.domain_ai_function import DomainAIFunction
from ai_core_api_client.models.domain_ai_function_call import DomainAIFunctionCall
from ai_core_api_client.models.domain_ai_function_parameter_property import DomainAIFunctionParameterProperty
from ai_core_api_client.models.domain_ai_function_parameters import DomainAIFunctionParameters
from ai_core_api_client.models.domain_ai_message import DomainAIMessage
from ai_core_api_client.models.domain_ai_tool import DomainAITool
from ai_core_api_client.models.domain_company import DomainCompany
from ai_core_api_client.models.domain_company_request import DomainCompanyRequest
from ai_core_api_client.models.domain_conversation_request import DomainConversationRequest
from ai_core_api_client.models.domain_conversation_response import DomainConversationResponse
from ai_core_api_client.models.domain_error_response import DomainErrorResponse
from ai_core_api_client.models.domain_success_response import DomainSuccessResponse

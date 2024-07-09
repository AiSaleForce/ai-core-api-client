# coding: utf-8

"""
    AISF API

    This API gives you the ability to interact with AISF's neural networks

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ai_core_api_client.api.ai_api import AiApi


class TestAiApi(unittest.TestCase):
    """AiApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AiApi()

    def tearDown(self) -> None:
        pass

    def test_conversation_post(self) -> None:
        """Test case for conversation_post

        Generate response from AI model
        """
        pass


if __name__ == '__main__':
    unittest.main()

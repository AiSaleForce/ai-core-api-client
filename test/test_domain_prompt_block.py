# coding: utf-8

"""
    AISF API

    This API gives you the ability to interact with AISF's neural networks

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ai_core_api_client.models.domain_prompt_block import DomainPromptBlock

class TestDomainPromptBlock(unittest.TestCase):
    """DomainPromptBlock unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DomainPromptBlock:
        """Test DomainPromptBlock
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DomainPromptBlock`
        """
        model = DomainPromptBlock()
        if include_optional:
            return DomainPromptBlock(
                content = '',
                name = ''
            )
        else:
            return DomainPromptBlock(
        )
        """

    def testDomainPromptBlock(self):
        """Test DomainPromptBlock"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

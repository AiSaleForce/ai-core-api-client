# coding: utf-8

"""
    AISF API

    This API gives you the ability to interact with AISF's neural networks

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ai_core_api_client.models.domain_ai_function_parameter_property import DomainAIFunctionParameterProperty
from typing import Optional, Set
from typing_extensions import Self

class DomainAIFunctionParameters(BaseModel):
    """
    DomainAIFunctionParameters
    """ # noqa: E501
    properties: Optional[Dict[str, DomainAIFunctionParameterProperty]] = None
    required: Optional[List[StrictStr]] = None
    type: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["properties", "required", "type"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of DomainAIFunctionParameters from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each value in properties (dict)
        _field_dict = {}
        if self.properties:
            for _key_properties in self.properties:
                if self.properties[_key_properties]:
                    _field_dict[_key_properties] = self.properties[_key_properties].to_dict()
            _dict['properties'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DomainAIFunctionParameters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "properties": dict(
                (_k, DomainAIFunctionParameterProperty.from_dict(_v))
                for _k, _v in obj["properties"].items()
            )
            if obj.get("properties") is not None
            else None,
            "required": obj.get("required"),
            "type": obj.get("type")
        })
        return _obj



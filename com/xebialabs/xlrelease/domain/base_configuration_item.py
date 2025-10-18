# python
from dataclasses import dataclass, field, fields as dataclass_fields
from typing import Any, Dict, Union
import json

@dataclass
class BaseConfigurationItem:
    all_properties: Dict[str, Any] = field(default_factory=dict)

    def __getattr__(self, name: str) -> Any:
        # fallback to all_properties when normal lookup fails
        if 'all_properties' in self.__dict__ and name in self.__dict__['all_properties']:
            return self.__dict__['all_properties'][name]
        raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")

    def __setattr__(self, name: str, value: Any) -> None:
        # Determine declared dataclass field names for this class
        try:
            field_names = {f.name for f in dataclass_fields(type(self))}
        except Exception:
            field_names = set()

        # If it's a declared field, set it normally and also mirror into all_properties
        if name in field_names:
            super().__setattr__(name, value)
            # ensure all_properties exists and mirror the value
            if 'all_properties' in self.__dict__:
                self.__dict__['all_properties'][name] = value
            else:
                super().__setattr__('all_properties', {name: value})
        else:
            # unknown attributes go into all_properties only
            if 'all_properties' not in self.__dict__:
                super().__setattr__('all_properties', {})
            self.__dict__['all_properties'][name] = value

    def update_from_dict(self, data: Dict[str, Any]) -> None:
        # Populate known fields and store all keys in all_properties
        for k, v in data.items():
            # Use __setattr__ so declared fields are set and mirrored
            setattr(self, k, v)
        # Ensure declared fields that weren't present in input are still reflected in all_properties
        try:
            for f in dataclass_fields(type(self)):
                if f.name not in self.__dict__['all_properties']:
                    self.__dict__['all_properties'][f.name] = getattr(self, f.name)
        except Exception:
            pass

    @classmethod
    def from_json(cls, data: Union[str, Dict[str, Any]]) -> "BaseConfigurationItem":
        if isinstance(data, str):
            parsed = json.loads(data)
        else:
            parsed = data
        instance = cls()
        if isinstance(parsed, dict):
            instance.update_from_dict(parsed)
        return instance

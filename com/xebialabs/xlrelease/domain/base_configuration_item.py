import json
from typing import Any

from pydantic import BaseModel
from requests import Response


class BaseConfigurationItem(BaseModel):
    """Base Pydantic model that allows extra fields and exposes them as attributes.

    - extra fields are allowed (model_config = {"extra": "allow"}).
    - unknown attributes will be stored in the model's extra storage and
      are accessible as normal attributes (e.g. instance.foo).
    - provides convenient constructors `from_dict` and `from_json` to match
      the previous API used by the dataclass-based domain objects.
    """

    model_config = {"extra": "allow"}

    def __getattr__(self, name: str) -> Any:  # only called if normal lookup fails
        # pydantic v2 stores extras on __pydantic_extra__
        extra = getattr(self, "__pydantic_extra__", None)
        if extra and name in extra:
            return extra[name]
        raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")

    def __setattr__(self, name: str, value: Any) -> None:
        # If it's a declared model field, use BaseModel's __setattr__ to get validation
        model_fields = getattr(type(self), "model_fields", {})
        if name in model_fields:
            super().__setattr__(name, value)
            return

        # Otherwise, treat it as an extra and store it in __pydantic_extra__
        extra = getattr(self, "__pydantic_extra__", None)
        if extra is None:
            # object.__setattr__ to avoid pydantic's interception
            object.__setattr__(self, "__pydantic_extra__", {})
            extra = self.__pydantic_extra__
        extra[name] = value

    #
    # Parsing
    #

    @classmethod
    def from_dict(cls, data: Any) -> "BaseConfigurationItem":
        if isinstance(data, cls):
            return data
        return cls.model_validate(data)

    @classmethod
    def from_json(cls, data: Any) -> "BaseConfigurationItem":

        if isinstance(data, (str, bytes, bytearray)):
            parsed = json.loads(data)
        else:
            parsed = data
        return cls.model_validate(parsed)

    @classmethod
    def from_response(cls, response: Response) -> "BaseConfigurationItem":
        return cls.from_json(response.json())

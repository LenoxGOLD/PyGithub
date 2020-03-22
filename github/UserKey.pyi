from typing import Any, Dict

class UserKey:
    def __repr__(self) -> str: ...
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, Any]) -> None: ...
    def delete(self) -> None: ...
    @property
    def id(self) -> int: ...
    @property
    def key(self) -> str: ...
    @property
    def title(self) -> str: ...
    @property
    def url(self) -> str: ...
    @property
    def verified(self) -> bool: ...

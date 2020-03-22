from datetime import datetime
from typing import Any, Dict, Optional

from github.NamedUser import NamedUser

class CommitStatus:
    def __repr__(self) -> str: ...
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, Any]) -> None: ...
    @property
    def context(self) -> str: ...
    @property
    def created_at(self) -> datetime: ...
    @property
    def creator(self) -> NamedUser: ...
    @property
    def description(self) -> Optional[str]: ...
    @property
    def id(self) -> int: ...
    @property
    def state(self) -> str: ...
    @property
    def target_url(self) -> Optional[str]: ...
    @property
    def updated_at(self) -> datetime: ...
    @property
    def url(self) -> str: ...

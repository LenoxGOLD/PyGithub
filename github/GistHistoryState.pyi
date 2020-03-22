from datetime import datetime
from typing import Any, Dict, List, Optional

from github.CommitStats import CommitStats
from github.Gist import Gist
from github.GistFile import GistFile
from github.NamedUser import NamedUser

class GistHistoryState:
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, Any]) -> None: ...
    @property
    def change_status(self) -> CommitStats: ...
    @property
    def comments(self) -> int: ...
    @property
    def comments_url(self) -> str: ...
    @property
    def commits_url(self) -> str: ...
    @property
    def committed_at(self) -> datetime: ...
    @property
    def created_at(self) -> datetime: ...
    @property
    def description(self) -> str: ...
    @property
    def files(self) -> Dict[str, GistFile]: ...
    @property
    def forks(self) -> List[Gist]: ...
    @property
    def forks_url(self) -> str: ...
    @property
    def git_pull_url(self) -> str: ...
    @property
    def git_push_url(self) -> str: ...
    @property
    def history(self) -> List[GistHistoryState]: ...
    @property
    def html_url(self) -> str: ...
    @property
    def id(self) -> str: ...
    @property
    def owner(self) -> NamedUser: ...
    @property
    def public(self) -> bool: ...
    @property
    def updated_at(self) -> datetime: ...
    @property
    def url(self) -> str: ...
    @property
    def user(self) -> Optional[NamedUser]: ...
    @property
    def version(self) -> str: ...

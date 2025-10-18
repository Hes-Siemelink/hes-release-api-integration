# python
# from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, List, Dict, Optional, Collection

# Forward imports for type hints (adjust actual import paths if these Python modules exist)
if False:  # pragma: no cover
    from com.xebialabs.xlrelease.domain import Release, Phase, Task, Variable, TeamView, BasicReleaseView
    from com.xebialabs.xlrelease.api.v1.forms import AbortRelease, ReleasesFilters, VariableOrValue
    from com.xebialabs.xlrelease.repository import PhaseVersion
    from com.xebialabs.xlrelease.search import ReleaseCountResults, ReleaseFullSearchResult


class ReleaseApiFull(ABC):
    SERVICE_NAME: str = "releaseApi"
    DEFAULT_PAGE: int = 0
    ARCHIVE_PAGE: str = "archivePage"
    ARCHIVE_RESULTS_PER_PAGE: str = "archiveResultsPerPage"

    # Common query parameter names (used in Java annotations)
    PAGE: str = "page"
    RESULTS_PER_PAGE: str = "resultsPerPage"
    PAGE_IS_OFFSET: str = "pageIsOffset"
    ROLE_IDS_DATA: str = "roleIdsData"

    def serviceName(self) -> str:
        return self.SERVICE_NAME

    @abstractmethod
    def downloadAttachment(self, attachmentId: str) -> Any:
        raise NotImplementedError

    @abstractmethod
    def getAttachment(self, attachmentId: str) -> bytes:
        raise NotImplementedError

    @abstractmethod
    def countReleases(self, releasesFilters: Any) -> Any:
        """releasesFilters: ReleasesFilters -> returns ReleaseCountResults"""
        raise NotImplementedError

    @abstractmethod
    def searchReleases(self,
                       releasesFilters: Any,
                       page: Optional[int] = DEFAULT_PAGE,
                       resultsPerPage: Optional[int] = 100,
                       pageIsOffset: Optional[bool] = False) -> List[Any]:
        """Returns List[Release]. Overloads with fewer args are supported via defaults."""
        raise NotImplementedError

    @abstractmethod
    def searchReleasesOverview(self,
                               releasesFilters: Any,
                               page: Optional[int] = DEFAULT_PAGE,
                               resultsPerPage: Optional[int] = 100) -> List[Any]:
        """Returns List[BasicReleaseView]."""
        raise NotImplementedError

    @abstractmethod
    def fullSearchReleases(self,
                           page: Optional[int],
                           archivePage: Optional[int],
                           resultsPerPage: Optional[int],
                           archiveResultsPerPage: Optional[int],
                           releasesFilters: Any) -> Any:
        """Returns ReleaseFullSearchResult."""
        raise NotImplementedError

    @abstractmethod
    def getReleases(self,
                    page: Optional[int] = DEFAULT_PAGE,
                    resultsPerPage: Optional[int] = 100) -> List[Any]:
        """Returns List[Release]. Also covers parameterless calling."""
        raise NotImplementedError

    @abstractmethod
    def getRelease(self, releaseId: str, withRoleIds: bool = False) -> Any:
        raise NotImplementedError

    @abstractmethod
    def getArchivedRelease(self, releaseId: str, withRoleIds: bool = False) -> Any:
        raise NotImplementedError

    @abstractmethod
    def getActiveTasks(self, releaseId: str) -> List[Any]:
        raise NotImplementedError

    @abstractmethod
    def start(self, releaseId: str) -> Any:
        raise NotImplementedError

    def updateRelease(self, releaseId: Optional[str] = None, release: Optional[Any] = None) -> Any:
        """
        Supports both Java call patterns:
        - updateRelease(releaseId: str, release: Release)
        - updateRelease(release: Release)
        Implementations should override this method or call super().
        """
        # Support call style updateRelease(release) where release is passed as first arg
        if release is None and releaseId is not None:
            # caller passed a single Release instance as first arg
            release = releaseId
            releaseId = None
        raise NotImplementedError

    @abstractmethod
    def delete(self, releaseId: str) -> None:
        raise NotImplementedError

    def abort(self, releaseId: str, abortRelease: Optional[Any] = None, abortComment: Optional[str] = None) -> Any:
        """
        Supports:
        - abort(releaseId: str, AbortRelease abortRelease)
        - abort(releaseId: str, String abortComment)
        """
        raise NotImplementedError

    @abstractmethod
    def searchReleasesByTitle(self, releaseTitle: str) -> List[Any]:
        raise NotImplementedError

    @abstractmethod
    def getVariables(self, releaseId: str) -> List[Any]:
        raise NotImplementedError

    @abstractmethod
    def getVariableValues(self, releaseId: str) -> Dict[str, str]:
        raise NotImplementedError

    @abstractmethod
    def getVariable(self, variableId: str) -> Any:
        raise NotImplementedError

    @abstractmethod
    def getVariablePossibleValues(self, variableId: str) -> Collection[Any]:
        raise NotImplementedError

    @abstractmethod
    def isVariableUsed(self, variableId: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def replaceVariable(self, variableId: str, variableOrValue: Any) -> None:
        raise NotImplementedError

    @abstractmethod
    def deleteVariable(self, variableId: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def createVariable(self, releaseId: str, variable: Any) -> Any:
        raise NotImplementedError

    @abstractmethod
    def updateVariables(self, releaseId: str, variables: List[Any]) -> List[Any]:
        raise NotImplementedError

    @abstractmethod
    def updateVariable(self, variableId: str, variable: Any) -> Any:
        raise NotImplementedError

    @abstractmethod
    def updateVariable(self, variable: Any) -> Any:  # overloaded name; last definition wins for typing, keep behavior documented
        raise NotImplementedError

    @abstractmethod
    def getPermissions(self) -> List[str]:
        raise NotImplementedError

    @abstractmethod
    def getTeams(self, releaseId: str) -> List[Any]:
        raise NotImplementedError

    @abstractmethod
    def setTeams(self, releaseId: str, teams: List[Any]) -> List[Any]:
        raise NotImplementedError

    @abstractmethod
    def resume(self, releaseId: str) -> Any:
        raise NotImplementedError

    @abstractmethod
    def restartPhases(self,
                      releaseId: str,
                      fromPhaseId: Optional[str] = None,
                      fromTaskId: Optional[str] = None,
                      phaseVersion: Optional[Any] = None,
                      resume: Optional[bool] = False) -> Any:
        """Corresponds to restartPhases(...) in Java."""
        raise NotImplementedError

    def restartPhase(self,
                     release: Any,
                     phase: Optional[Any] = None,
                     task: Optional[Any] = None,
                     phaseVersion: Optional[Any] = None,
                     resumeRelease: Optional[bool] = False) -> Any:
        """
        Single method covering Java overloads for restartPhase:
        - restartPhase(Release)
        - restartPhase(Release, boolean)
        - restartPhase(Release, Phase)
        - restartPhase(Release, Phase, PhaseVersion)
        - restartPhase(Release, Phase, Task)
        - restartPhase(Release, Phase, Task, PhaseVersion)
        - restartPhase(Release, Phase, Task, PhaseVersion, boolean)
        Implementations should override this method.
        """
        raise NotImplementedError

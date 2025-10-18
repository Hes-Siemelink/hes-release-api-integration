from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, List, Set, Dict, Optional

from .plan_item import PlanItem

@dataclass
class Release(PlanItem):
    rootReleaseId: Optional[str] = None
    maxConcurrentReleases: int = 0
    releaseTriggers: List[Any] = field(default_factory=list)
    teams: List[Any] = field(default_factory=list)
    memberViewers: List[str] = field(default_factory=list)
    roleViewers: List[str] = field(default_factory=list)
    attachments: List[Any] = field(default_factory=list)
    phases: List[Any] = field(default_factory=list)
    queryableStartDate: Optional[datetime] = None
    queryableEndDate: Optional[datetime] = None
    realFlagStatus: Optional[Any] = None
    status: Optional[Any] = None
    kind: Optional[Any] = None
    tags: List[str] = field(default_factory=list)
    categories: Set[str] = field(default_factory=set)
    variables: List[Any] = field(default_factory=list)
    calendarLinkToken: Optional[str] = None
    calendarPublished: bool = False
    tutorial: bool = False
    abortOnFailure: bool = False
    archiveRelease: bool = True
    allowPasswordsInAllFields: bool = False
    disableNotifications: bool = False
    allowConcurrentReleasesFromTrigger: bool = True
    originTemplateId: Optional[str] = None
    createdFromTrigger: bool = False
    scriptUsername: Optional[str] = None
    scriptUserPassword: Optional[str] = None
    extensions: List[Any] = field(default_factory=list)
    startedFromTaskId: Optional[str] = None
    parentReleaseId: Optional[str] = None
    autoStart: bool = False
    automatedResumeCount: int = 0
    maxAutomatedResumes: int = 0
    abortComment: Optional[str] = None
    variableMapping: Dict[str, str] = field(default_factory=dict)
    riskProfile: Optional[Any] = None
    author: Optional[str] = None
    logo: Optional[Any] = None
    defaultTargetFolderId: Optional[str] = None
    allowTargetFolderOverride: bool = True
    allowRestartInExecutionView: bool = True
    archived: bool = False
    ciUid: Optional[int] = None
    tenantId: Optional[str] = None

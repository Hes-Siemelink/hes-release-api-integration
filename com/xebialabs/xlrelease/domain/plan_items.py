from __future__ import annotations
from typing import Any, Dict, List, Optional, Set
from datetime import datetime
from pydantic import Field

from com.xebialabs.xlrelease.domain import BaseConfigurationItem


class PlanItem(BaseConfigurationItem):
    title: Optional[str] = None
    description: Optional[str] = None
    owner: Optional[str] = None
    scheduledStartDate: Optional[datetime] = None
    dueDate: Optional[datetime] = None
    startDate: Optional[datetime] = None
    endDate: Optional[datetime] = None
    plannedDuration: Optional[int] = None
    flagComment: Optional[str] = None
    overdueNotified: bool = False


class Task(PlanItem):
    documentationPage: Optional[str] = None
    comments: List[Any] = Field(default_factory=list)
    container: Optional[Any] = None
    facets: List[Any] = Field(default_factory=list)
    attachments: List[Any] = Field(default_factory=list)
    status: Optional[Any] = None
    lastStatusChangeBy: Optional[str] = None
    team: Optional[str] = None
    watchers: Set[str] = Field(default_factory=set)
    waitForScheduledStartDate: bool = True
    delayDuringBlackout: bool = False
    postponedDueToBlackout: bool = False
    postponedUntilEnvironmentsAreReserved: bool = False
    originalScheduledStartDate: Optional[datetime] = None
    hasBeenFlagged: bool = False
    hasBeenDelayed: bool = False
    preconditionType: Optional[Any] = None
    precondition: Optional[str] = None
    failureHandler: Optional[str] = None
    taskFailureHandlerEnabled: bool = False
    taskRecoverOp: Optional[Any] = None
    failuresCount: int = 0
    executionId: Optional[str] = None
    variableMapping: Dict[str, str] = Field(default_factory=dict)
    externalVariableMapping: Dict[str, str] = Field(default_factory=dict)
    maxCommentSize: int = 32768
    tags: List[str] = Field(default_factory=list)
    dueSoonNotified: bool = False
    locked: bool = False
    checkAttributes: bool = False
    supportedInWorkflow: bool = True
    statusLine: Optional[str] = None


class Phase(PlanItem):
    releaseUid: Optional[int] = None
    tasks: List[Task] = Field(default_factory=list)
    release: Optional[Any] = None
    color: Optional[str] = None
    originId: Optional[str] = None


class Release(PlanItem):
    rootReleaseId: Optional[str] = None
    maxConcurrentReleases: int = 0
    releaseTriggers: List[Any] = Field(default_factory=list)
    teams: List[Any] = Field(default_factory=list)
    memberViewers: List[str] = Field(default_factory=list)
    roleViewers: List[str] = Field(default_factory=list)
    attachments: List[Any] = Field(default_factory=list)
    phases: List[Phase] = Field(default_factory=list)
    queryableStartDate: Optional[datetime] = None
    queryableEndDate: Optional[datetime] = None
    realFlagStatus: Optional[Any] = None
    status: Optional[Any] = None
    kind: Optional[Any] = None
    tags: List[str] = Field(default_factory=list)
    categories: Set[str] = Field(default_factory=set)
    variables: List[Any] = Field(default_factory=list)
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
    extensions: List[Any] = Field(default_factory=list)
    startedFromTaskId: Optional[str] = None
    parentReleaseId: Optional[str] = None
    autoStart: bool = False
    automatedResumeCount: int = 0
    maxAutomatedResumes: int = 0
    abortComment: Optional[str] = None
    variableMapping: Dict[str, str] = Field(default_factory=dict)
    riskProfile: Optional[Any] = None
    author: Optional[str] = None
    logo: Optional[Any] = None
    defaultTargetFolderId: Optional[str] = None
    allowTargetFolderOverride: bool = True
    allowRestartInExecutionView: bool = True
    archived: bool = False
    ciUid: Optional[int] = None
    tenantId: Optional[str] = None


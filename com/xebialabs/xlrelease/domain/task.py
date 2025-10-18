from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, List, Set, Dict, Optional

from .plan_item import PlanItem


@dataclass
class Task(PlanItem):
    documentationPage: Optional[str] = None
    comments: List[Any] = field(default_factory=list)
    container: Optional[Any] = None
    facets: List[Any] = field(default_factory=list)
    attachments: List[Any] = field(default_factory=list)
    status: Optional[Any] = None
    lastStatusChangeBy: Optional[str] = None
    team: Optional[str] = None
    watchers: Set[str] = field(default_factory=set)
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
    variableMapping: Dict[str, str] = field(default_factory=dict)
    externalVariableMapping: Dict[str, str] = field(default_factory=dict)
    maxCommentSize: int = 32768
    tags: List[str] = field(default_factory=list)
    dueSoonNotified: bool = False
    locked: bool = False
    checkAttributes: bool = False
    supportedInWorkflow: bool = True
    statusLine: Optional[str] = None

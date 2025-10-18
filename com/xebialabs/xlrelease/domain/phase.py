# python
from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Any

from .plan_item import PlanItem
from .task import Task
from .release import Release

@dataclass
class Phase(PlanItem):
    releaseUid: Optional[int] = None
    tasks: List[Task] = field(default_factory=list)
    release: Optional[Release] = None
    # status: Optional[PhaseStatus] = None
    color: Optional[str] = None
    originId: Optional[str] = None

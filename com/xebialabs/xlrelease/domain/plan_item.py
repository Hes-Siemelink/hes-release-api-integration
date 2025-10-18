from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from com.xebialabs.xlrelease.domain.base_configuration_item import BaseConfigurationItem


@dataclass
class PlanItem(BaseConfigurationItem):
    title: Optional[str] = None
    description: Optional[str] = None
    owner: Optional[str] = None
    scheduledStartDate: Optional[datetime] = None
    dueDate: Optional[datetime] = None
    startDate: Optional[datetime] = None
    endDate: Optional[datetime] = None
    plannedDuration: Optional[int] = None
    # flagStatus: FlagStatus = FlagStatus.OK
    flagComment: Optional[str] = None
    overdueNotified: bool = False

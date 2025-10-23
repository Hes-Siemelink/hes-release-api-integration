from typing import Any, Dict, List, Optional
from abc import ABC

from digitalai.release.release_api_client import ReleaseAPIClient
from com.xebialabs.xlrelease.domain import Phase, Task


class PhaseApi(ABC):

    def __init__(self, release_api_client: ReleaseAPIClient) -> None:
        self.api = release_api_client

    def getPhase(self, phaseId: str) -> Phase:
        response = self.api.get(f"/api/v1/phases/{phaseId}")
        return Phase.from_response(response)

    def updatePhase(self, phase: Phase) -> Phase:
        response = self.api.put(f"/api/v1/phases/{phase.id}", json=phase.model_dump())

        return Phase.from_response(response)

    def addTask(self, containerId: str, task: Task, position: Optional[int] = None) -> Task:
        params = with_actual_values({"position": position})
        response = self.api.post(f"/api/v1/phases/{containerId}/tasks", json=task.model_dump(), params=params)
        return Task.from_response(response)

    def searchPhasesByTitle(self, phaseTitle: str, releaseId: str) -> List[Phase]:
        params = with_actual_values({"phaseTitle": phaseTitle, "releaseId": releaseId})
        response = self.api.get("/api/v1/phases/byTitle", params=params)
        return [Phase.from_response(item) for item in response]

    def searchPhases(self,
                     phaseTitle: Optional[str],
                     releaseId: str,
                     phaseVersion: Optional[Any] = None) -> List[Phase]:
        params = with_actual_values({"phaseTitle": phaseTitle, "releaseId": releaseId, "phaseVersion": phaseVersion})
        response = self.api.get("/api/v1/phases/search", params=params)
        return [Phase.from_response(item) for item in response]

    def addPhase(self, releaseId: str, phase: Phase, position: Optional[int] = None) -> Phase:
        params = with_actual_values({"position": position})
        payload = phase.model_dump()

        print(f"Payload for addPhase: {payload}")

        response = self.api.post(f"/api/v1/phases/{releaseId}/phase", json=payload, params=params)

        print(f"Response from addPhase: {response}")
        print(response.text)

        return Phase.from_response(response)

    def copyPhase(self, phaseIdToCopy: str, targetPosition: int) -> Phase:
        params = {"targetPosition": targetPosition}
        response = self.api.post(f"/api/v1/phases/{phaseIdToCopy}/copy", params=params)
        return Phase.from_response(response)

    def newPhase(self, title: Optional[str] = None) -> Phase:
        phase = Phase()
        phase.title = title

        return phase

    def deletePhase(self, phaseId: str) -> None:
        self.api.delete(f"/api/v1/phases/{phaseId}")


# Helper methods

def with_actual_values(params: Dict[str, Any]) -> Dict[str, Any]:
    return {k: v for k, v in params.items() if v is not None}

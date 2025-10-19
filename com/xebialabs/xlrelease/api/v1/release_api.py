from abc import ABC

from digitalai.release.release_api_client import ReleaseAPIClient

from com.xebialabs.xlrelease.domain import Release


class ReleaseApi(ABC):

    def __init__(self, release_api_client: ReleaseAPIClient) -> None:
        self.api = release_api_client

    def getRelease(self, releaseId: str) -> Release:
        response = self.api.get(f"/api/v1/releases/{releaseId}")
        return Release.from_response(response)

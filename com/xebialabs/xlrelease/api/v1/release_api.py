from abc import ABC

from com.xebialabs.xlrelease.domain import Release
from digitalai.release.release_api_client import ReleaseAPIClient


class ReleaseApi(ABC):

    def __init__(self, release_api_client: ReleaseAPIClient) -> None:
        self.release_api_client = release_api_client

    def getRelease(self, releaseId: str) -> Release:
        response = self.release_api_client.get(f"/api/v1/releases/{releaseId}")
        print(response.text)
        return Release.from_json(response.json())

from digitalai.release.integration import BaseTask

from com.xebialabs.xlrelease.api.v1 import ReleaseApi


class ApiBaseTask(BaseTask):

    def __init__(self):
        super().__init__()
        self._releaseApi = None

    @property
    def releaseApi(self):
        if self._releaseApi is None:
            self._releaseApi = ReleaseApi(self.get_release_api_client())
        return self._releaseApi

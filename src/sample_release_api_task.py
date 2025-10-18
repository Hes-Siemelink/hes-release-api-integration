from digitalai.release.integration import BaseTask
from com.xebialabs.xlrelease.api.v1.release_api import ReleaseApi

class GetRelease(BaseTask):

    def execute(self) -> None:

        # Get the message from the input properties
        id = self.input_properties['releaseId']
        if not id:
            raise ValueError("The 'id' field cannot be empty")

        # Obtain an instance of the Release API client
        releaseApi = ReleaseApi(self.get_release_api_client())

        release = releaseApi.getRelease(id)

        # Add a line to the comment section in the UI
        self.add_comment(f"Found release {release.title}")

from com.xebialabs.xlrelease.api.v1 import ApiBaseTask


class GetRelease(ApiBaseTask):

    def execute(self) -> None:
        # Parse input
        id = self.input_properties['releaseId']
        if not id:
            raise ValueError("The 'id' field cannot be empty")

        # Call Release API
        release = self.releaseApi.getRelease(id)

        # Process resilt
        self.add_comment(f"Found release {release.title}")

from com.xebialabs.xlrelease.api.v1 import ApiBaseTask
from com.xebialabs.xlrelease.domain import Phase, Task


class AddPhase(ApiBaseTask):

    def execute(self) -> None:
        # Parse input
        title = self.input_properties['phaseTitle']
        if not title:
            raise ValueError("Please provide a phase title")

        # Build phase object
        phase = Phase(
            title=title,
            tasks=[
                Task(title="Placeholder Task")
            ]
        )

        # API call
        # XXX addPhase only adds the phase, not the tasks within it
        new_phase = self.phaseApi.addPhase(self.get_release_id(), phase)

        # Process result
        self.add_comment(f"Created new phase {new_phase.title} with id {new_phase.id}")

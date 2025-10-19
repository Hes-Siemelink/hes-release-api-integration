import unittest
import os
import json

from com.xebialabs.xlrelease.domain import Release


class JsonParseTests(unittest.TestCase):

    def test_json_parsing(self):
        # Given
        # Load 'release.json' file from current directory
        file_path = os.path.join(os.path.dirname(__file__), "release.json")
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        # When
        release = Release.from_json(data)

        # Then

        # Check Releases
        self.assertEqual(release.id,
                         "Applications/Folder856d5b08c3474414b1856e15bf06369e/Release34b169be50684b2ba5489a9099903bc4")
        self.assertEqual(release.title, "TEST Release")

        # Check Phases
        phases = release.phases
        self.assertEqual(len(phases), 1)
        phase = phases[0]
        self.assertEqual(phase.title, "New Phase")

        # Check Tasks
        self.assertTrue(len(phase.tasks) >= 1)
        task = phase.tasks[0]
        self.assertEqual(task.title, "Get release")

        # Check access of properties are present in the JSON but not in the model
        self.assertEqual(task.capabilities, ["remote"])

        # also assert we can set and retrieve a new extra attribute
        task.some_new_extra = "extra-value"
        self.assertEqual(task.some_new_extra, "extra-value")

    def test_to_json_includes_extras(self):
        # Ensure the to_json serializer includes both declared fields and extras
        file_path = os.path.join(os.path.dirname(__file__), "release.json")
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        release = Release.from_json(data)

        # set a programmatic extra on the first task
        first_task = release.phases[0].tasks[0]
        first_task.some_new_extra = "extra-value-2"

        # serialize the whole release to JSON (class method comes from BaseConfigurationItem)
        release_json = release.to_json()
        parsed = json.loads(release_json)

        # declared field
        self.assertEqual(parsed.get("title"), "TEST Release")

        # phases/tasks should be present and include extras
        phases = parsed.get("phases", [])
        self.assertTrue(len(phases) >= 1)
        tasks = phases[0].get("tasks", [])
        self.assertTrue(len(tasks) >= 1)
        task0 = tasks[0]

        # JSON-origin extra
        self.assertIn("capabilities", task0)
        self.assertEqual(task0["capabilities"], ["remote"])

        # programmatic extra must also be serialized
        self.assertIn("some_new_extra", task0)
        self.assertEqual(task0["some_new_extra"], "extra-value-2")

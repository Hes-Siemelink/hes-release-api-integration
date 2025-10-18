import unittest

from src.sample_release_api_task import GetRelease


class TestServerQuery(unittest.TestCase):

    def test_server_query(self):

        # Given
        task = GetRelease()
        task.input_properties = {
            'releaseId': 'Applications/Folder856d5b08c3474414b1856e15bf06369e/Release34b169be50684b2ba5489a9099903bc4',
        }

        # When
        task.execute_task()

        # Then
        # self.assertEqual(task.get_output_properties()['productName'], 'iPhone 13 Pro')


if __name__ == '__main__':
    unittest.main()

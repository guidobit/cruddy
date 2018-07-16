from unittest import TestCase

from backend.data_service import DataService, DatabaseType


class TestDataService(TestCase):
    def setUp(self):
        self.database_url = 'mongodb://somedb/db'
        self.database_name = 'test_db'
        self.data_service: DataService = DataService(
            database_type=DatabaseType.MONGO,
            database_name=self.database_name,
            database_url=self.database_url)

    def test_create_string(self):
        string_to_create = 'hello world'
        result = self.data_service.create(
            data_type='string',
            value=string_to_create
        )
        self.assertEqual(type(result), dict,
                         'Create method should return dict')
        self.assertEqual(result[self.data_service.value_field], string_to_create,
                         'Create method output should have the value of the input at value_field')



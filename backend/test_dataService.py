import os
from unittest import TestCase
from backend.data_service import DataService, DatabaseType


class TestDataService(TestCase):
    def setUp(self):
        self.database_url: str = os.getenv('DATABASE_URL')
        self.database_name: str = 'test_db'
        self.data_service: DataService = DataService(
            database_type=DatabaseType.MONGO,
            database_name=self.database_name,
            database_url=self.database_url)

    def test_create_string(self):
        string_to_create = 'hello world'
        write_result = self.data_service.create(
            data_type='string',
            value=string_to_create
        )
        self.assertEqual(type(write_result), dict,
                         'Create method should return dict')
        self.assertEqual(write_result[self.data_service.value_field], string_to_create,
                         'Create method output should have the value of the input at value_field')
        read_result = self.data_service.read(data_type='string', key=write_result[self.data_service.key_field])
        self.assertEqual(read_result[self.data_service.value_field], string_to_create,
                         'Inserted value should be the same as value returned from read.')

    def tearDown(self):
        if self.data_service.database_type == DatabaseType.MONGO:
            self.data_service.impl.client.drop_database(self.database_name)

from typing import List
from enum import Enum
import pymongo


class DatabaseType(Enum):
    MONGO = 1


class DataService:
    def __init__(self, database_type: DatabaseType, database_url: str = '', database_name: str = '') -> None:
        print(f'Initializing {database_type.name} database with url {database_url}')
        if database_type == DatabaseType.MONGO:
            self.database_type = database_type
            self.impl = DatabaseMongoImplicit(database_url=database_url, database_name=database_name)
            self.key_field: str = self.impl.KEY_FIELD
            self.type_field: str = self.impl.TYPE_FIELD
            self.value_field: str = self.impl.VALUE_FIELD
        else:
            raise Exception('Database type is not implemented')

    def create(self, data_type: str, value) -> dict:
        return {self.value_field: value}

    def read(self, data_type: str, key: str) -> dict:
        pass

    def list(self, data_type: str) -> List[dict]:
        pass

    def delete(self, key: str) -> bool:
        pass


class DatabaseMongoImplicit:

    KEY_FIELD = '_id'
    TYPE_FIELD = '_type'
    VALUE_FIELD = '_data'

    def __init__(self, database_url, database_name) -> None:
        self.client: pymongo.MongoClient = pymongo.MongoClient(database_url)
        self.db = self.client[database_name]




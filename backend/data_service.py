from typing import List, Dict, Optional
from enum import Enum
import pymongo
from bson import ObjectId


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

    def create(self, data_type: str, value) -> Dict:
        type_checker(data_type, str)
        return self.impl.create(data_type=data_type, value=value)

    def read(self, data_type: str, key: str) -> Optional[Dict]:
        type_checker(data_type, str)
        type_checker(key, str)
        return self.impl.read(data_type=data_type, key=key)

    def list(self, data_type: str) -> List[Dict]: # TODO: Implement list
        type_checker(data_type, str)
        return self.impl.list()

    def delete(self, key: str) -> bool: # TODO: Implement delete
        type_checker(key, str)
        return self.impl.delete()


class DatabaseMongoImplicit:
    KEY_FIELD = '_id'
    TYPE_FIELD = '_data_type'
    VALUE_FIELD = '_data'

    def __init__(self, database_url, database_name) -> None:
        self.client: pymongo.MongoClient = pymongo.MongoClient(database_url)
        self.db = self.client[database_name]

    def create(self, data_type: str, value) -> Dict:
        data: Dict = {}
        data[self.TYPE_FIELD] = data_type
        data[self.VALUE_FIELD] = value
        insertion_result = self.db[data_type].insert_one(data)
        data[self.KEY_FIELD] = str(insertion_result.inserted_id)
        return data

    def read(self, data_type: str, key: str) -> Optional[Dict]:
        return self.db[data_type].find_one({self.KEY_FIELD: ObjectId(key)})

    def list(self) -> List[Dict]:
        return [{}]

    def delete(self) -> bool:
        return True


# Helper functions for DataService
def type_checker(data_type: str, required_type: type) -> None:
    assert isinstance(data_type, required_type), f'{required_type} required for data_type, got {type(data_type)}'

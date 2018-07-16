from enum import Enum
from vibora.blueprints import Blueprint
from vibora.responses import JsonResponse

from backend.config import Config

api = Blueprint()


class CruddyHeaders(Enum):
    JSON: object = {'content-type': 'application/json'}
    HTML: object = {'content-type': 'html'}


class CruddyCodes(Enum):
    SUCCESS: int = 200


@api.route('/', methods=['GET'])
async def home(config: Config):
    welcome_msg = f'Welcome to {config.app_name}'
    return JsonResponse(
        content={'msg': welcome_msg},
        status_code=CruddyCodes.SUCCESS.value,
        headers=CruddyHeaders.JSON.value
    )


@api.route('/<something>', methods=['POST'])
async def store_something():
    return JsonResponse(
        content=
        {
            'obj': {},
            'stored': True
        },
        status_code=CruddyCodes.SUCCESS.value,
        headers=CruddyHeaders.JSON.value
    )

import json
from vibora import Vibora
from backend.api import api
from backend.config import Config

if __name__ == "__main__":

    print('Welcome to the demo!')

    app = Vibora()

    # Registering our API
    app.add_blueprint(api, prefixes={'v1': '/v1'})

    with open('backend/config.json') as f:
        config = Config(json.load(f))
        app.components.add(config)
        app.run(host=config.host, port=config.port)

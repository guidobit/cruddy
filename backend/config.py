class Config:
    def __init__(self, config: dict):
        self.port = config['port']
        self.host = config['host']
        self.app_name = config['app_name']

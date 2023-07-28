import os

class Config:
    def __init__(self):
        # Set up your configuration variables
        self.api_key = os.getenv('API_KEY')
        self.user_config_path = 'user_config.json'
        self.autodoc_config_path = 'autodoc_config.json'

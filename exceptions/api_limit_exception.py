class APILimitException(Exception):
    def __init__(self, message="API Limit Reached"):
        self.message = message
        super().__init__(self.message)

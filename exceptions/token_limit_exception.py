class TokenLimitException(Exception):
    def __init__(self, message="Token Limit Reached"):
        self.message = message
        super().__init__(self.message)

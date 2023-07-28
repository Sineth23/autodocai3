import openai
from exceptions.token_limit_exception import TokenLimitException

class LLMService:

    def __init__(self):
        openai.api_key = 'YOUR_OPENAI_API_KEY'

    def generate_summary(self, code, max_tokens=60):
        # Ensure that the length of code does not exceed the token limit
        if len(code) > max_tokens:
            raise TokenLimitException("The code length exceeds the maximum token limit.")

        # Call the OpenAI API to generate a summary
        try:
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=code,
                max_tokens=max_tokens
            )
            summary = response.choices[0].text.strip()
        except Exception as e:
            print(f"An error occurred while generating the summary: {e}")
            summary = ""

        return summary

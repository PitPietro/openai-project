import os
import openai
from dotenv import load_dotenv

if __name__ == '__main__':
    # create a .env file filled with the OpenAI API key
    # OPENAI_API_KEY=your-key

    load_dotenv()

    openai.api_key = os.getenv("OPENAI_API_KEY")

    original_message = "She no went to the market."

    response = openai.Completion.create(
        engine="davinci",
        prompt="Original: " + original_message + "\nStandard American English:",
        temperature=0,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"]
    )

    print("Original message: " + original_message)
    print("OpenAI response: " + str(response["choices"]))

# https://beta.openai.com/docs/developer-quickstart/your-api-keys
# https://dev.to/jakewitcher/using-env-files-for-environment-variables-in-python-applications-55a1

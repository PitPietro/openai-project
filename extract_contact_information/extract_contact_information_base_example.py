import os

import openai
from dotenv import load_dotenv

if __name__ == '__main__':
    # https://beta.openai.com/docs/developer-quickstart/your-api-keys
    # copy the OpenAI API key from the link above
    # create a .env file filled with the OpenAI API key
    # OPENAI_API_KEY=your-key
    # you can also use this terminal command:
    # echo OPENAI_API_KEY=your-key > .env

    load_dotenv()

    openai.api_key = os.getenv("OPENAI_API_KEY")

    original_message = """
    Dear John,
    I'm really proud of you! I'm writing this email to thank you about yesterday's talk. 
    If you'd like to collaborate with me, here's my address: 442 Evergreen Terrace, Oregon US 97477
    Best, Bart
    """

    response = openai.Completion.create(
        engine="davinci-instruct-beta",
        prompt="Extract the mailing address from this email:\n\n" + original_message + "\n\nName and address:\n",
        temperature=0,
        max_tokens=64,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    print("Original message: " + original_message)
    print("OpenAI response: " + str(response["choices"]))

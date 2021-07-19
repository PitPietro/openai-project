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

    original_message = "..."

    response = openai.Completion.create(
        engine="davinci-instruct-beta",
        prompt="Extract the mailing address from this email:\n\nDear Kelly,\n\nIt was great to talk to you at the seminar. I thought Jane's talk was quite good.\n\nThank you for the book. Here's my address 2111 Ash Lane, Crestview CA 92002\n\nBest,\n\nMaya\n\nName and address:\n",
        temperature=0,
        max_tokens=64,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    print("Original message: " + original_message)
    print("OpenAI response: " + str(response))

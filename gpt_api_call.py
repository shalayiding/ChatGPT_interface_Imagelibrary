import openai
import os

# Set up your OpenAI API key
def GPT_API_CALL(request_message):
    if request_message == "":
        return
    f = open("gpt_api.key", "r")
    openai.api_key = f.read()
    # Make an API call
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", # this is "ChatGPT" $0.002 per 1k tokens
    messages=[{"role": "user", "content": request_message}]
    )
    reply_content = completion.choices[0].message.content
    return reply_content
import os
from dotenv import load_dotenv
import openai

load_dotenv()


openai_api_key = os.getenv('OPENAI_API_KEY')

if not openai_api_key:
    raise ValueError("OpenAI API key not found in environment variables.")


openai.api_key = openai_api_key

def get_openai_response(user_input):

    #keywords = ["latest", "official website", "detailed", "unmodified", "specific", "to the point", "mostliked"]
    context = "adobe"
    regex = "adobe.com"
    # system_message = f" Please ensure the information provided is about {context}, uses the latest data, is from the official website, and provides detailed, unmodified, specific, to the point, and most liked information.and use {regex}.You MUST use the browser tool to answer the questions below. If no context available, please reply 'no context available'."   


    response = openai.ChatCompletion.create(
        model="gpt-4-turbo-2024-04-09",
        messages=[
            {"role": "system", "content":"Hello ho are u"},
            {"role": "user", "content":user_input}
        ]
    )

    return response['choices'][0]['message']['content']

query = "I want you to access data from internet i dont know howsoever use another library or use any other thing"

print(get_openai_response(query))
import os
from dotenv import load_dotenv
import openai

load_dotenv()


openai_api_key = os.getenv('OPENAI_API_KEY')

if not openai_api_key:
    raise ValueError("OpenAI API key not found in environment variables.")


openai.api_key = openai_api_key

def get_openai_response(user_input):

    keywords = ["latest", "official website", "detailed", "unmodified", "specific", "to the point", "mostliked"]
    context = "adobe"
    regex = "adobe.com"
    system_message = f" Please ensure the information provided is about {context}, uses the latest data, is from the official website, and provides detailed, unmodified, specific, to the point, and most liked information.You MUST use the browser tool to answer the questions below. You MUST use search results from domain 'adobe.com'  by using search query prefix “site:adobe.com ”. If no context available, please reply 'no context available'."   


    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content":system_message},
            {"role": "user", "content":user_input}
        ]
    )

    return response['choices'][0]['message']['content']

print(get_openai_response("Whenever im trying to transform any object, no matter if free transform, deform, warp, resize etc, once i grab any point to drag and transform, this little gray windows pops up, showing current size of what im transforming and very often it gets in my way of view, especially when im transforming a small piece of the object, so i cant really see much. Any way to hide it"))
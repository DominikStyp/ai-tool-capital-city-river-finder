import os
from pprint import pprint
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

def capitol_river_finder(country):
    # Load environment variables from .env file
    load_dotenv()

    api_private_key = os.getenv('API_PRIVATE_KEY')

    # print("API Key:", api_private_key)

    llm = ChatOpenAI(openai_api_key=api_private_key)
    # Define the prompt
    prompt = f"""Follow the instructions step by step.
1. Find a capitol city for the country spelled in polish as: {country}.
2. Find the biggest river which flows through the capitol city from the step 1.
3. Make your answer short, and prepare the output information in the JSON format with fields: river_name, capitol_name
   containing only river name and capitol name.
4. Translate the JSON values to polish language as on the example: {{"river_name":"Wisła", "capitol_name":"Warszawa"}},
   making sure that river name in polish is translated properly in terms of geography and language,
   and output only the translated JSON.
"""

    #print (prompt)

    response = llm.invoke(prompt)

    return response.content
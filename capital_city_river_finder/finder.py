import os, json, re
from pprint import pprint
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

def capital_river_finder(country, output_language = "English"):
    # Load environment variables from .env file
    load_dotenv()

    api_private_key = os.getenv('API_PRIVATE_KEY')

    llm = ChatOpenAI(
        openai_api_key=api_private_key,
        model="gpt-3.5-turbo",
        temperature=0.0,
        max_tokens=1000,
        # top_p=1.0,
        # frequency_penalty=0.0,
        # presence_penalty=0.0,
    )

    prompt = '''
    Provide a JSON object with two fields.
    The first field "c" should be the capital city for country known as ''' + country + ''' in Polish,
    and the second field "r" should be the name of the major river flowing through this capital city.
    Use the names as they are internationally recognized in ''' + output_language + '''.
    '''

    print (prompt)

    response = llm.invoke(prompt).content

    print (response + "\n\n\n")

    parsed_json = json.loads(response)

    if(parsed_json == None):
        return '{"river": "", "capital": ""}'

    return '{"river":"' + filter_river_name(parsed_json.get("r")) + '","capital": "' + parsed_json.get("c") + '"}'

def filter_river_name(river_name:str):
    return re.sub(r'(River|Rzeka)', '', river_name, flags=re.IGNORECASE).strip()


def parse_output_as_json(output:str):
    match = re.search(r'\{.*?\}', output)

    if match:
        json_str = match.group()

        return json.loads(json_str)
    else:
        return None
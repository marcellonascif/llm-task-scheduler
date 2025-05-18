from llm import *

from dotenv import load_dotenv
import os

load_dotenv()
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')

def main():
    client: LLMClient = LLMClient(api_key=GOOGLE_API_KEY, model="gemini-2.0-flash", )

    # print("Modelos disponíveis:", client.list_models())

    prompt = "Qual ano a taylor swift nasceu?"
    response = client.request(prompt=prompt)
    print("Resposta do LLM:", response)

if __name__ == "__main__":
    main()

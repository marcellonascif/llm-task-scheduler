from llm import *

from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os

load_dotenv()
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', '')

# Vou comparar o modelo de prompt Direto com CoT e usar uma decomposicao hierarquica na mao via system prompt (Tecnicas de decomposicao de tarefas em subtarefas)

# class LLMResponse(BaseModel):
#     '''
#     Classe para representar a resposta do modelo Gemini da Google.
#     '''
#     plan: list[str] = Field(description='Uma lista ordenada contendo o plano de ação gerado pelo modelo.')


def main():
    prompt = "Preciso aprender python."

    # Direct Response
    clientA: LLMClient = LLMClient(
        api_key=GEMINI_API_KEY,
        model="gemini-2.5-flash-preview-04-17",
        system_prompt="You are an action planner assistant. Given a user goal, return a numbered, executable task list.",
    )

    responseA = clientA.request(prompt=prompt)
    print("Resposta do LLM:", responseA)

if __name__ == "__main__":
    main()

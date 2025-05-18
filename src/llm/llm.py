from google import genai
from google.genai import types

class LLMClient:
    '''
    Classe para interagir com o modelo Gemini da Google.
    '''

    def __init__(self, api_key: str, model: str = "gemini-2.0-flash", system_prompt: str = None):
        self.client = genai.Client(api_key=api_key)
        self.model = model
        self.system_prompt = system_prompt


    def list_models(self) -> list:
        '''
        Lista os modelos disponíveis na API do Gemini.
        Returns:
            models (list): Lista de modelos disponíveis.
        '''
        return self.client.models.list()


    def request(self, prompt: str) -> str:
        '''
        Gera um texto a partir de um prompt usando o modelo Gemini gemini-2.0-flash da Google.
        Params:
            prompt (str): O prompt a ser usado para gerar o texto.
        Returns:
            response.text (str): A resposta gerada pelo modelo.

        '''

        response = self.client.models.generate_content(
            model=self.model,
            contents=[prompt],
            config=types.GenerateContentConfig(
                system_instruction=self.system_prompt,
                seed=42,
                temperature=0.5,
                top_p=0.8,
                top_k=3
            )
        )

        return response.text

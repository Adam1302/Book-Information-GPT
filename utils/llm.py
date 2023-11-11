from langchain.llms import OpenAI
from langchain.schema.language_model import BaseLanguageModel

def getLLM(temperature):
    return OpenAI(temperature=temperature)

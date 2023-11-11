from langchain.llms import OpenAI

def getLLM(temperature):
    return OpenAI(temperature=temperature)

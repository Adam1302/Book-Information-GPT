from langchain.llms import OpenAI as LangchainOpenAI
from openai import OpenAI as NormalOpenAI
import streamlit as sl

@sl.cache_resource
def getLLM(temperature):
    return LangchainOpenAI(
        temperature=temperature,
        max_tokens=-1,
        )

@sl.cache_resource
def getOpenAIClient():
    return NormalOpenAI()

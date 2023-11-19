from langchain.llms import OpenAI
import streamlit as sl

@sl.cache_resource
def getLLM(temperature):
    return OpenAI(
        temperature=temperature,
        max_tokens=-1,
        )

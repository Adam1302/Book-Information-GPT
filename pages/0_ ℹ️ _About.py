import os
import streamlit as sl
from streamlit_extras.app_logo import add_logo
from apikey import apikey # stored locally, not on Git
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory

sl.set_page_config(page_title="About", page_icon=":book:")
add_logo("pictures/essentials/logo_x_small.png")

@sl.cache_resource
def getPageImage():
    return sl.image('pictures/other/searching_for_light.jpg')

textCol, imageCol = sl.columns((1,1.2), gap='large')
with textCol:
    sl.header("About AML")
    sl.markdown("It is neither widely accessible nor impartially reliable to explore and navigate a three thousand year history of great Art, Media, and Literature simply through recommendations. This tool can be used to identify, summarize, and/or suggest great works.")
    sl.markdown("AML harnesses the power Large Language Models (LLMs), a type of artificial intelligence that uses large data sets and complex algorithms to hold, analyze, and generate content.")
    sl.markdown("Please offer us some feedback in the 'Give Us Feedback' tab.")

with imageCol:
    getPageImage()

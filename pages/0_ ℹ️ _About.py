import os
import streamlit as sl
from apikey import apikey # stored locally, not on Git
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory

sl.set_page_config(page_title="About", page_icon=":book:")

sl.header("About")

textCol, imageCol = sl.columns((1,1.2))
with textCol:
    sl.markdown("It is neither widely accessible nor impartially reliable to explore and navigate a three thousand year history of great Art, Media, and Literature simply through recommendations. This tool can be used to identify, summarize, and/or suggest great works.")
    sl.markdown("AML harnesses the power Large Language Models (LLMS), a type of artificial intelligence that uses large data sets and complex algorithms to hold, analyze, and generate content.")
    sl.markdown("Please offer us some feedback in the 'Give Us Feedback' tab. Please note that this site is not for-profit and is personally funded by its creator; as a result, due to time or resource limitations, not all suggestions can be honoured.")

with imageCol:
    sl.image('pictures/growing_tree.jpg')

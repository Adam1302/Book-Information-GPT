import os
import streamlit as sl
from apikey import apikey # stored locally, not on Git
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory

sl.set_page_config(page_title="About", page_icon=":book:")

sl.header("About")
sl.markdown("Here's what we offer:")
sl.write("Work Suggestor: Receive a list of suggested works to look at based on what you're looking for")
sl.write("Work Identifier: Enter the name or a description of a specific work and recieve information about it")
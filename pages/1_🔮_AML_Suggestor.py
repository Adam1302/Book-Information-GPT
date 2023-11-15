import os
import streamlit as sl
from streamlit_extras.app_logo import add_logo
from apikey import apikey # stored locally, not on Git
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from utils.llm import getLLM
from utils.templates import work_suggestion_template


sl.set_page_config(page_title="Work_Suggestions", page_icon=":book:")
add_logo("pictures/essentials/logo_x_small.png")

llm = getLLM(0)

def getWorkSuggestionPrompt():
    return PromptTemplate(
        input_variables=["topic", "work_type"],
        template=work_suggestion_template,
    )

def getWorkSuggestionChain():
    return LLMChain(
        llm=llm, prompt=getWorkSuggestionPrompt(), verbose=True, output_key='work_suggestions',
    )

def get_work_desire():
    topic_they_want = sl.text_area(
        label=f"Enter or describe a topic or idea that you are interested in:",
        placeholder="Enter here",
        key="work_description_input"
    )
    return topic_they_want

sl.header("Work Suggestions")

work_type = sl.selectbox(
        'What type of work would you like suggested?',
        ('Novel/Novella', 'Short Story', 'Book', 'Movie', 'TV Show', 'Documentary',
        'Poem', 'Painting', 'Sculpture', 'Play/Musical'))

topic_input = get_work_desire()

if sl.button("Suggest") and (topic_input!="" and not topic_input.isspace()):

    suggestions = getWorkSuggestionChain().run({'topic': topic_input, 'work_type': work_type})

    sl.markdown(f"### Suggestions")
    sl.write(suggestions)

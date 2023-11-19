import os
import streamlit as sl
from streamlit_extras.app_logo import add_logo
from apikey import apikey
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from utils.llm import getLLM
from utils.philosopher_list import shortened_philosopher_list, extensive_philosopher_list
from utils.templates import philosopher_opinion_on_topic_template


def getOpinionPrompt():
    return PromptTemplate(
        input_variables=["philosopher", "topic"],
        template=philosopher_opinion_on_topic_template,
    )

sl.set_page_config(page_title="Philosopher Views", page_icon=":book:")
add_logo("pictures/essentials/logo_x_small.png")

llm = getLLM(0)

def getOpinionChain():
    return LLMChain(
        llm=llm, prompt=getOpinionPrompt(),
        verbose=True, output_key='philosopher_opinion',
    )

pictureCol, philosopherCol = sl.columns((2,1), gap='medium')
with pictureCol:
    sl.image("pictures/other/growing_tree.jpg")
with philosopherCol:
    sl.header("Philosopher Views")
    philosopher_list_type = sl.select_slider(
        label="Philosopher List:",
        options=['Reduced', 'Extensive']
    )

    if philosopher_list_type == 'Reduced':
        philosopher_list = shortened_philosopher_list
    else:
        philosopher_list = extensive_philosopher_list

    def get_philosophers():
        philsophers = sl.selectbox(
            f"Select philosopher:",
            philosopher_list,
        )
        return philsophers

    philosopher_selected = get_philosophers()

def get_topic():
    topic_they_want = sl.text_area(
        label=f"Enter or describe a topic or idea you want their opinion on:",
        placeholder="Enter here",
        key="topic_input"
    )
    return topic_they_want

topic_input = get_topic()

if sl.button(f"Get Opinion") and topic_input and philosopher_selected:

    with sl.spinner('Collecting'):
        opinion_result= getOpinionChain().run({'philosopher': philosopher_selected, 'topic': topic_input})

    #sl.markdown(f"### {work_type}:")
    sl.write(opinion_result)


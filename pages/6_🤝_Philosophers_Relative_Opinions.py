import os
import streamlit as sl
from streamlit_extras.app_logo import add_logo
from apikey import apikey
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from utils.llm import getLLM
from utils.philosopher_list import shortened_philosopher_list, extensive_philosopher_list
from utils.templates import shared_opinion_template, disagreements_template


def getSharedOpinionPrompt():
    return PromptTemplate(
        input_variables=["work_name"],
        template=shared_opinion_template,
    )
def getDisagreementsPrompt():
    return PromptTemplate(
        input_variables=["work_name"],
        template=disagreements_template,
    )

sl.set_page_config(page_title="Relative Opinions", page_icon=":book:")
add_logo("pictures/essentials/logo_x_small.png")

llm = getLLM(0)

def getSharedOpinionChain():
    return LLMChain(
        llm=llm, prompt=getSharedOpinionPrompt(),
        verbose=True, output_key='shared_opinions',
    )
def getDisagreementsChain():
    return LLMChain(
        llm=llm, prompt=getDisagreementsPrompt(),
        verbose=True, output_key='disagreements',
    )

sl.header("Philosophers: Relative Opinions")

relationTypeCol, philosopherListCol = sl.columns((1,1), gap='large')
with relationTypeCol:
    relation_type = sl.select_slider(
        'Opinion Relations:',
        options=['Agreements', 'Disagreements']
    )
with philosopherListCol:
    philosopher_list_type = sl.select_slider(
        label="Philosopher List:",
        options=['Reduced', 'Extensive']
    )

if philosopher_list_type == 'Reduced':
    philosopher_list = shortened_philosopher_list
else:
    philosopher_list = extensive_philosopher_list

def get_philosophers():
    philsophers = sl.multiselect(
        f"Select philosophers (max. 4):",
        philosopher_list,
        max_selections=4,
    )
    return philsophers

philosophers_input = get_philosophers()

if sl.button(f"Get {relation_type}") and philosophers_input:

    if len(philosophers_input) == 1:
        sl.error("You must select multiple options.", icon='🚨')
    else:
        with sl.spinner('Collecting'):
            philosophers_as_string = "{}, and {}".format(", ".join(philosophers_input[:-1]),  philosophers_input[-1])
            if relation_type == 'Agreements':
                opinions_result= getSharedOpinionChain().run(philosophers_as_string)
            else:
                opinions_result= getDisagreementsChain().run(philosophers_as_string)

        #sl.markdown(f"### {work_type}:")
        sl.write(opinions_result)


import os
import streamlit as sl
from streamlit_extras.app_logo import add_logo
from apikey import apikey # stored locally, not on Git
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from utils.llm import getLLM
from utils.templates import book_template, poem_template, movie_template, tv_show_template, documentary_template, painting_template, sculpture_template, theatre_template, work_rating_template, work_introduction_template

def getTemplate(artType):
    if (artType == "Book"):
        return book_template
    elif (artType == "Poem"):
        return poem_template
    elif (artType == "Movie"):
        return movie_template
    elif (artType == "TV Show"):
        return tv_show_template
    elif (artType == "Documentary"):
        return documentary_template
    elif (artType == "Painting"):
        return painting_template
    elif (artType == "Sculpture"):
        return sculpture_template
    elif (artType == "Play/Musical"):
        return theatre_template

def getWorkTitle(infoOutput, work_type):
    if (work_type == "Book" or work_type == "Poem" or work_type == "Painting" or work_type == "Sculpture" or work_type == "Play/Musical"):
        return infoOutput
    elif work_type == "Movie":
        return infoOutput[0:infoOutput.index("Directed by")]
    elif work_type == "TV Show":
        return infoOutput[0:infoOutput.index('[')]
    elif work_type == "Documentary":
        return infoOutput[0:(infoOutput.index(')') + 1)]

def getWorkIdentifierPrompt(artType):
    return PromptTemplate(
        input_variables=["work_name"],
        template=getTemplate(artType),
    )
work_rating_prompt = PromptTemplate(
    input_variables=["work_title"],
    template=work_rating_template,
)
work_introduction_prompt = PromptTemplate(
    input_variables=["work_title"],
    template=work_introduction_template,
)

sl.set_page_config(page_title="Work_Identifier", page_icon=":book:")
add_logo("pictures/essentials/logo_x_small.png")

llm = getLLM(0)

def getWorkIdentifierChain(artType):
    return LLMChain(
        llm=llm, prompt=getWorkIdentifierPrompt(artType),
        verbose=True, output_key='work_title',
    )
work_rating_chain = LLMChain(
    llm=llm, prompt=work_rating_prompt, verbose=True, output_key='work_rating',
)
work_introduction_chain = LLMChain(
    llm=llm, prompt=work_introduction_prompt, verbose=True, output_key='work_intro',
)

def get_work(work_type):
    work_they_want = sl.text_area(
        label=f"Enter the name or provide a description of the {work_type} you are interested in:",
        placeholder="Work name here",
        key="work_name_input"
    )
    return work_they_want

sl.header("Work Identifier")

work_type = sl.selectbox(
        'What type of work are you looking for?',
        ('Book', 'Movie', 'TV Show', 'Documentary',
        'Poem', 'Painting', 'Sculpture', 'Play/Musical'))

work_name_input = get_work(work_type)

if sl.button("Identify"):
    work_info = getWorkIdentifierChain(work_type).run(work_name_input)
    work_title = getWorkTitle(work_info, work_type).strip()
    work_intro = work_introduction_chain.run(work_title)

    sl.markdown(f"### {work_type}:")
    sl.write(work_info)

    if (work_type == "Movie" or work_type == "TV Show" or work_type == "Documentary"):
        sl.markdown("### iMDB Rating:")
        sl.write(work_rating_chain.run(work_title))

    sl.markdown("### About:")
    sl.write(work_intro)

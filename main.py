import os
import streamlit as sl
from apikey import apikey # stored locally, not on Git
from langchain import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory

os.environ['OPENAI_API_KEY'] = apikey

#IDEAS
## AS PER: https://www.youtube.com/watch?v=U_eV8wfMkXU
#   we will have a nice multi-columned explanation of what this site does

# Later, we could have dropdowns for books, movies (platforms available on), shows (platforms available on), etc.

## TO BE MORE SPECIFIC, WE CAN HAVE MULTIPLE INPUT BOXES ##
# ex. author, 

# AMAZON/KINDLE links

def getLLM():
    llm = OpenAI(temperature=0)
    return llm

book_template = """
    You will receive information about a book.
    Your goal is to:
    - Find the book
    - Find the author
    - Find the year in which it was written

    Here is an example:
    Q: Of Mice And Men
    A: Of Mice And Men (1937) by John Steinbeck

    BOOK: {book_name}

    YOUR RESPONSE:
"""

book_introduction_template = """
    Introduce {book_title} in one paragraph
"""

book_info_prompt = PromptTemplate(
    input_variables=["book_name"],
    template=book_template,
)

book_introduction_prompt = PromptTemplate(
    input_variables=["book_title"],
    template=book_introduction_template,
)

llm = getLLM()
book_info_chain = LLMChain(
    llm=llm, prompt=book_info_prompt, verbose=True, output_key='book_title',
)
book_introduction_chain = LLMChain(
    llm=llm, prompt=book_introduction_prompt, verbose=True, output_key='book_intro',
)

sl.set_page_config(page_title="Art_Finder", page_icon=":book:")
sl.header("Search for a book:")

def get_book():
    input_book = sl.text_area(
        label="Enter a work you are interested in:",
        placeholder="Book name here",
        key="book_name_input"
    )
    return input_book

book_name_input = get_book()

if book_name_input:
    book_info_output = book_info_chain.run(book_name_input)
    book_intro_output = book_introduction_chain.run(book_info_output)

    sl.markdown("### Book Name:")
    sl.write(book_info_output)

    sl.markdown("### About the Book:")
    sl.write(book_intro_output)


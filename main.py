import os
import streamlit as sl
from apikey import apikey # stored locally, not on Git
from langchain import PromptTemplate
from langchain.llms import OpenAI

os.environ['OPENAI_API_KEY'] = apikey

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

book_info_prompt = PromptTemplate(
    input_variables=["book_name"],
    template=book_template,
)

llm = getLLM()

sl.set_page_config(page_title="Art_Finder", page_icon=":book:")
## AS PER: https://www.youtube.com/watch?v=U_eV8wfMkXU
#   we will have a nice multi-columned explanation of what this site does

# Later, we could have dropdowns for books, movies (platforms available on), shows (platforms available on), etc.

sl.header("Search for a book:")

## TO BE MORE SPECIFIC, WE CAN HAVE MULTIPLE INPUT BOXES ##
def get_book():
    input_book = sl.text_area(
        label="Enter a work you are interested in:",
        placeholder="Book name here",
        key="book_name_input"
    )
    return input_book

book_name = get_book()

sl.markdown("### Book Name:")
if book_name:
    formatted_book_info_response = llm(
        book_info_prompt.format(
            book_name=book_name,
        )
    )
    sl.write(formatted_book_info_response)

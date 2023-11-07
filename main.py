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

# "Find books/movies/shows about"

# AMAZON/KINDLE links (NVM: this is pretty expensive since you'll need an API like Rainforest)

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

movie_template = """
    You will receive information about a movie.
    Your goal is to:
    - Find the movie
    - Find the director
    - Find the writer
    - Find the year in which it was released
    - Find the actors/actresses who starred in the movie

    Here is an example:
    Q:
    Taxi Driver
    A:
    Taxi Driver (1976)\n
    Directed by Martin Scorcese\n
    Written by Paul Schrader\n
    Starring Robert De Niro, Jodie Foster, Harvey Keitel, Cybill Shepherd


    MOVIE: {movie_name}

    YOUR RESPONSE:
"""

work_rating_template = """
    What is the iMDB rating of {work_title}? Please provide only the rating in the format: 'rating/10'. If the rating does not exist or cannot be found, answer with 'N/A'
"""

work_introduction_template = """
    Introduce {work_title} in one paragraph
"""

book_info_prompt = PromptTemplate(
    input_variables=["book_name"],
    template=book_template,
)
movie_info_prompt = PromptTemplate(
    input_variables=["movie_name"],
    template=movie_template,
)
work_rating_prompt = PromptTemplate(
    input_variables=["work_title"],
    template=work_rating_template,
)
work_introduction_prompt = PromptTemplate(
    input_variables=["work_title"],
    template=work_introduction_template,
)

llm = getLLM()
book_info_chain = LLMChain(
    llm=llm, prompt=book_info_prompt, verbose=True, output_key='book_title',
)
movie_info_chain = LLMChain(
    llm=llm, prompt=movie_info_prompt, verbose=True, output_key='movie_title',
)
work_rating_chain = LLMChain(
    llm=llm, prompt=work_rating_prompt, verbose=True, output_key='work_rating',
)
work_introduction_chain = LLMChain(
    llm=llm, prompt=work_introduction_prompt, verbose=True, output_key='work_intro',
)

def get_work():
    input_book = sl.text_area(
        label="Enter the name or provide a description of the work you are interested in:",
        placeholder="Work name here",
        key="work_name_input"
    )
    return input_book

sl.set_page_config(page_title="Art_Finder", page_icon=":book:")

work_type = sl.selectbox(
        'What type of work are you looking for?',
        ('Book', 'Movie', 'TV Show', 'Documentary'))


work_name_input = get_work()

if work_name_input:
    if (work_type == "Book"):
        book_info_output = book_info_chain.run(work_name_input)
        book_intro_output = work_introduction_chain.run(book_info_output)

        sl.markdown("### Book Name:")
        sl.write(book_info_output)

        sl.markdown("### About the Book:")
        sl.write(book_intro_output)

    elif (work_type == "Movie"):
        movie_info_output = movie_info_chain.run(work_name_input)
        movie_title = movie_info_output[0:movie_info_output.index("Directed by")]
        movie_rating_output = work_rating_chain.run(movie_title)
        movie_intro_output = work_introduction_chain.run(movie_title)

        sl.markdown("### Movie Name:")
        sl.write(movie_info_output)

        sl.markdown("### Movie iMDB Rating:")
        sl.write(movie_rating_output)


        sl.markdown("### About the Movie:")
        sl.write(movie_intro_output)


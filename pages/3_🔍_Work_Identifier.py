import os
import streamlit as sl
from apikey import apikey # stored locally, not on Git
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from utils.llm import getLLM

book_template = """
    You will receive information about a book.
    Your goal is to:
    - Find the book
    - Find the author
    - Find the year in which it was written

    Here is an example:
    Q: Of Mice And Men
    A: Of Mice And Men (1937) by John Steinbeck

    BOOK: {work_name}

    YOUR RESPONSE:
"""

poem_template = """
    You will receive information about a poem.
    Your goal is to:
    - Find the poem
    - Find the poet
    - Find the year in which it was written

    Here is an example:
    Q: O Captain! My Captain!
    A: O' Captain, My Captain (1865) by Walt Whitman

    POEM: {work_name}

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


    MOVIE: {work_name}

    YOUR RESPONSE:
"""

tv_show_template = """
    You will receive information about a television show.
    Your goal is to:
    - Find the show
    - Find the creator of the show
    - Find the actors/actresses who starred in the show
    - Find the year in which it began
    - Find the year in which it ended. If it hasn't ended, display 'present'.
    - Find the number of seasons

    Here are two examples:
    Q:
    The Sopranos
    A:
    Sopranos (1999-2007) [6 seasons]\n
    Created by David Chase\n
    Starring James Gandolfini, Michael Imperioli, Edie Falco, Lorraine Bracco\n

    Q:
    8 Out of 10 Cats (2005-present) [21 seasons]\n
    Created by Channel 4\n
    Starring Jimmy Carr, Sean Lock, Jon Richardson\n


    SHOW: {work_name}

    YOUR RESPONSE:
"""

documentary_template = """
    You will receive information about a documentary.
    Your goal is to:
    - Find the documentary
    - Find the Director
    - Find the year in which it was released

    Here is an example:
    Q:
    Grizzly Man
    A:
    Grizzly Man (2005)\n
    Directed by Werner Herzog


    DOCUMENTARY: {work_name}

    YOUR RESPONSE:
"""

painting_template = """
    You will receive information about a painting.
    Your goal is to:
    - Find the painting
    - Find the artist
    - Find the year in which it was completed

    Here is an example:
    Q: Mona Lisa
    A: Mona Lisa (1519) by Leonardo da Vinci

    Painting: {work_name}

    YOUR RESPONSE:
"""

sculpture_template = """
    You will receive information about a sculpture.
    Your goal is to:
    - Find the sculpture
    - Find the sculptor
    - Find the year in which it was completed

    Here is an example:
    Q: The Thinker
    A: The Thinker (1904) by Auguste Rodin

    Sculpture: {work_name}

    YOUR RESPONSE:
"""

theatre_template = """
    You will receive information about a a play or a musical.
    Your goal is to:
    - Find the play/musical name
    - Find the writer(s)
    - Find the year in which it first premiered

    Here are three examples:
    Q: Death of a Salesman
    A: Death of a Salesman (1949) by Arthur Miller
    Q: A Streetcar Named Desire
    A: A Streetcar Named Desire (1947) by Tennessee Williams
    Q: The Importance of Being Earnest
    A: The Importance of Being Earnest (1895) by Oscar Wilde

    Play/Musical: {work_name}

    YOUR RESPONSE:
"""

work_rating_template = """
    What is the iMDB rating of {work_title}? Please provide only the rating in the format: 'rating/10'. If the rating does not exist or cannot be found, answer with 'N/A'
"""

work_introduction_template = """
    Introduce {work_title} in one paragraph
"""

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

llm = getLLM(0)

@sl.cache_data
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

if work_name_input:
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

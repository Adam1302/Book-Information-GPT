import os
import streamlit as sl
from apikey import apikey # stored locally, not on Git
from langchain import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory

os.environ['OPENAI_API_KEY'] = apikey

# ART MEDIA LITERATURE: IDEAS
## AS PER: https://www.youtube.com/watch?v=U_eV8wfMkXU
#   we will have a nice multi-columned explanation of what this site does

# Later, we could have dropdowns for books, movies (platforms available on), shows (platforms available on), etc.

## TO BE MORE SPECIFIC, WE CAN HAVE MULTIPLE INPUT BOXES ##
# ex. author, 

# "Find books/movies/shows about"

# Theatre

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

poem_template = """
    You will receive information about a poem.
    Your goal is to:
    - Find the poem
    - Find the poet
    - Find the year in which it was written

    Here is an example:
    Q: O Captain! My Captain!
    A: O' Captain, My Captain (1865) by Walt Whitman

    POEM: {poem_name}

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


    SHOW: {show_name}

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


    DOCUMENTARY: {documentary_name}

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

    Painting: {painting_name}

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

    Sculpture: {sculpture_name}

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

    Play/Musical: {theatre_name}

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
tv_show_info_prompt = PromptTemplate(
    input_variables=["show_name"],
    template=tv_show_template,
)
documentary_info_prompt = PromptTemplate(
    input_variables=["documentary_name"],
    template=documentary_template,
)
poem_info_prompt = PromptTemplate(
    input_variables=["poem_name"],
    template=poem_template,
)
painting_info_prompt = PromptTemplate(
    input_variables=["painting_name"],
    template=painting_template,
)
sculpture_info_prompt = PromptTemplate(
    input_variables=["sculpture_name"],
    template=sculpture_template,
)
theatre_info_prompt = PromptTemplate(
    input_variables=["theatre_name"],
    template=theatre_template,
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
tv_show_info_chain = LLMChain(
    llm=llm, prompt=tv_show_info_prompt, verbose=True, output_key='tv_show_title',
)
documentary_info_chain = LLMChain(
    llm=llm, prompt=documentary_info_prompt, verbose=True, output_key='documentary_title',
)
poem_info_chain = LLMChain(
    llm=llm, prompt=poem_info_prompt, verbose=True, output_key='poem_title',
)
painting_info_chain = LLMChain(
    llm=llm, prompt=painting_info_prompt, verbose=True, output_key='painting_title',
)
sculpture_info_chain = LLMChain(
    llm=llm, prompt=sculpture_info_prompt, verbose=True, output_key='sculpture_title',
)
theatre_info_chain = LLMChain(
    llm=llm, prompt=theatre_info_prompt, verbose=True, output_key='theatre_title',
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
        ('Book', 'Movie', 'TV Show', 'Documentary',
        'Poem', 'Painting', 'Sculpture', 'Theatre (Plays and Musicals)'))

work_name_input = get_work()

if work_name_input:
    if (work_type == "Book"):
        book_info_output = book_info_chain.run(work_name_input)
        book_intro_output = work_introduction_chain.run(book_info_output)

        sl.markdown("### Book:")
        sl.write(book_info_output)

        sl.markdown("### About:")
        sl.write(book_intro_output)

    elif (work_type == "Movie"):
        movie_info_output = movie_info_chain.run(work_name_input)
        movie_title = movie_info_output[0:movie_info_output.index("Directed by")]
        movie_rating_output = work_rating_chain.run(movie_title)
        movie_intro_output = work_introduction_chain.run(movie_title)

        sl.markdown("### Movie:")
        sl.write(movie_info_output)

        sl.markdown("### iMDB Rating:")
        sl.write(movie_rating_output)


        sl.markdown("### About:")
        sl.write(movie_intro_output)

    elif (work_type == "TV Show"):
        tv_show_info_output = tv_show_info_chain.run(work_name_input)
        tv_show_title = tv_show_info_output[0:tv_show_info_output.index('[')]
        tv_show_rating_output = work_rating_chain.run(tv_show_title)
        tv_show_intro_output = work_introduction_chain.run(tv_show_title)

        sl.markdown("### TV Show:")
        sl.write(tv_show_info_output)

        sl.markdown("### iMDB Rating:")
        sl.write(tv_show_rating_output)

        sl.markdown("### About")
        sl.write(tv_show_intro_output)

    elif (work_type == "Documentary"):
        documentary_info_output = documentary_info_chain.run(work_name_input)
        documentary_title = documentary_info_output[0:(documentary_info_output.index(')') + 1)]
        documentary_rating_output = work_rating_chain.run(documentary_title)
        documentary_intro_output = work_introduction_chain.run(documentary_title)

        sl.markdown("### Documentary:")
        sl.write(documentary_info_output)

        sl.markdown("### iMDB Rating:")
        sl.write(documentary_rating_output)

        sl.markdown("### About:")
        sl.write(documentary_intro_output)

    elif (work_type == "Poem"):
        poem_info_output = poem_info_chain.run(work_name_input)
        poem_title = poem_info_output
        poem_intro_output = work_introduction_chain.run(poem_title)

        sl.markdown("### Poem:")
        sl.write(poem_info_output)

        sl.markdown("### About:")
        sl.write(poem_intro_output)

    elif (work_type == "Painting"):
        painting_info_output = painting_info_chain.run(work_name_input)
        painting_title = painting_info_output
        painting_intro_output = work_introduction_chain.run(painting_title)

        sl.markdown("### Painting:")
        sl.write(painting_info_output)

        sl.markdown("### About:")
        sl.write(painting_intro_output)

    elif (work_type == "Sculpture"):
        sculpture_info_output = sculpture_info_chain.run(work_name_input)
        sculpture_title = sculpture_info_output
        sculpture_intro_output = work_introduction_chain.run(sculpture_title)

        sl.markdown("### Sculpture:")
        sl.write(sculpture_info_output)

        sl.markdown("### About:")
        sl.write(sculpture_intro_output)

    elif (work_type == "Theatre (Plays and Musicals)"):
        theatre_info_output = theatre_info_chain.run(work_name_input)
        theatre_title = theatre_info_output
        theatre_intro_output = work_introduction_chain.run(theatre_title)

        sl.markdown("### Theatre:")
        sl.write(theatre_info_output)

        sl.markdown("### About:")
        sl.write(theatre_intro_output)


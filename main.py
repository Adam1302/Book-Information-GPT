import os
import streamlit as sl
from apikey import apikey # stored locally, not on Git
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory

os.environ['OPENAI_API_KEY'] = apikey

# ART MEDIA LITERATURE: IDEAS
## AS PER: https://www.youtube.com/watch?v=U_eV8wfMkXU
#   we will have a nice multi-columned explanation of what this site does

# Creating Pages
### Create a main page with a nice picture or two
### Create a nice About page with expandable drop-downs for each
### Create a page for each service
### Create a contact page and email

# Use st.progress() to show progress
### https://docs.streamlit.io/library/get-started/main-concepts#show-progress

# Once all features are in, fix the layout: https://docs.streamlit.io/library/get-started/main-concepts#layout
### search up how to make streamlit look nice
### Use header, subheader, markdown, write, etc.

# For long-running functions: https://docs.streamlit.io/library/get-started/main-concepts#caching
### this is a MUST-do for all functions that have similar runs

# Re-organize everything into different files, proper style/organization

# Deploy:
### https://docs.streamlit.io/library/get-started/create-an-app#share-your-app

# Advertise
### Create reddit account and share

## TO BE MORE SPECIFIC, WE CAN HAVE MULTIPLE INPUT BOXES ##
# ex. author, 

# "Topic prompts: in the style of '...'"
### creativity widget that controls temperature
### 

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

work_suggestion_template = """
    Below you will recieve a topic or description. Your goal is to provide between 3 and 5 suggestions of a {work_type} related to the topic or description. For each {work_type}, provide a 1-2 sentence introduction without revealing details of the plot.

    Here is an example of fiction books about the ultimate futility of life:
    1. "The Stranger" by Albert Camus:
    Camus' novel follows the detached Meursault as he grapples with the absurdity of existence, portraying the ultimate futility of conventional societal expectations.
    2. "Nausea" by Jean-Paul Sartre:
    In this existentialist classic, Roquentin's contemplation of existence in a small town becomes a profound exploration of the inherent nausea and meaninglessness of life.
    3. "The Road" by Cormac McCarthy:
    McCarthy's post-apocalyptic tale follows a father and son as they traverse a desolate world, reflecting on the futility of survival and the relentless march toward an uncertain future.

    Here is another example of paintings about the illusion of love:
    1: "The Lovers II" by René Magritte:
    Magritte's surrealist painting challenges the conventional notion of love by depicting two lovers with their heads veiled, questioning the authenticity and reality of the emotions involved.
    2: "Automat" by Edward Hopper:
    Hopper's iconic painting captures a woman alone in a restaurant, suggesting the isolation that can accompany the illusion of love and the complexities of human connection.
    3: "Love" by Robert Indiana:
    Indiana's famous "LOVE" sculpture, with its bold letters arranged in a square, explores the commodification and pop culture aspects of love, challenging the depth and sincerity of romantic illusions.
    4: "The Kiss" by Gustav Klimt:
    Klimt's masterpiece, featuring a couple locked in an intimate embrace surrounded by ornate patterns, explores the intertwining of love and the decorative, raising questions about the substance behind the illusion of passion.
    5: "The Birth of Venus" by Sandro Botticelli:
    Botticelli's iconic painting of Venus emerging from the sea symbolizes the idealized and mythological aspects of love, inviting contemplation on the illusionary nature of beauty and desire.

    TOPIC: {topic}
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
work_suggestion_prompt= PromptTemplate(
    input_variables=["work_type", "topic"],
    template=work_suggestion_template,
)

llm = getLLM()
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
work_suggestion_chain = LLMChain(
    llm=llm, prompt=work_suggestion_prompt, verbose=True, output_key='work_suggestions',
)

def get_work(work_type):
    work_they_want = sl.text_area(
        label=f"Enter the name or provide a description of the {work_type} you are interested in:",
        placeholder="Work name here",
        key="work_name_input"
    )
    return work_they_want

def get_work_desire():
    topic_they_want = sl.text_area(
        label=f"Enter or describe a topic or idea that you are interested in:",
        placeholder="Enter here",
        key="work_description_input"
    )
    return topic_they_want

## STREAMLIT PAGE
sl.set_page_config(page_title="Art_Finder", page_icon=":book:")

sl.markdown("Here's what we offer:")
sl.write("Work Suggestor: Receive a list of suggested works to look at based on what you're looking for")
sl.write("Work Identifier: Enter the name or a description of a specific work and recieve information about it")

service_type = sl.selectbox(
    'Which service would you like?',
    ('Work Suggestor', 'Work Identifier',)
)

if service_type == "Work Identifier":
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
elif service_type == "Work Suggestor":
    work_type = sl.selectbox(
            'What type of work would you like suggested?',
            ('Novel/Novella', 'Short Story', 'Book', 'Movie', 'TV Show', 'Documentary',
            'Poem', 'Painting', 'Sculpture', 'Play/Musical'))
    
    topic_input = get_work_desire()

    if topic_input:
        suggestions = work_suggestion_chain.run({'topic': topic_input, 'work_type': work_type})

        sl.markdown(f"### Suggestions")
        sl.write(suggestions)
    
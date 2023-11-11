import os
import streamlit as sl
from apikey import apikey # stored locally, not on Git
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory
from utils.llm import getLLM

llm = getLLM(0)

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
    3: "The Kiss" by Gustav Klimt:
    Klimt's masterpiece, featuring a couple locked in an intimate embrace surrounded by ornate patterns, explores the intertwining of love and the decorative, raising questions about the substance behind the illusion of passion.
    4: "The Birth of Venus" by Sandro Botticelli:
    Botticelli's iconic painting of Venus emerging from the sea symbolizes the idealized and mythological aspects of love, inviting contemplation on the illusionary nature of beauty and desire.

    TOPIC: {topic}
"""

def getWorkSuggestionPrompt():
    return PromptTemplate(
        input_variables=["topic", "work_type"],
        template=work_suggestion_template,
    )

#def getWorkSuggestionChain():
wo = LLMChain(
        llm=llm, prompt=getWorkSuggestionPrompt(), verbose=True, output_key='work_suggestions',
    )

def get_work_desire():
    topic_they_want = sl.text_area(
        label=f"Enter or describe a topic or idea that you are interested in:",
        placeholder="Enter here",
        key="work_description_input"
    )
    return topic_they_want

sl.set_page_config(page_title="Work_Suggestions", page_icon=":book:")
sl.header("Work Suggestions")

work_type = sl.selectbox(
        'What type of work would you like suggested?',
        ('Novel/Novella', 'Short Story', 'Book', 'Movie', 'TV Show', 'Documentary',
        'Poem', 'Painting', 'Sculpture', 'Play/Musical'))

topic_input = get_work_desire()

if topic_input:
    suggestions = wo.run({'topic': topic_input, 'work_type': work_type})

    sl.markdown(f"### Suggestions")
    sl.write(suggestions)

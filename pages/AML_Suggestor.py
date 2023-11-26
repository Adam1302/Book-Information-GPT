import streamlit as sl
from streamlit_extras.app_logo import add_logo
from st_pages import add_indentation
from utils.llm import getOpenAIClient
from utils.templates import getWorkSuggestionTemplate


sl.set_page_config(page_title="AML: Work Suggestor", page_icon=":book:")
add_logo("pictures/essentials/logo_x_small.png")

add_indentation()

client = getOpenAIClient()

def get_work_desire():
    topic_they_want = sl.text_area(
        label=f"Enter or describe a topic or idea that you are interested in:",
        placeholder="Enter here",
        key="work_description_input"
    )
    return topic_they_want

sl.header("Work Suggestions")

work_type = sl.selectbox(
        'What type of work would you like suggested?',
        ('Novel/Novella', 'Short Story', 'Book', 'Movie', 'TV Show', 'Documentary',
        'Poem', 'Painting', 'Sculpture', 'Play/Musical'))

topic_input = get_work_desire()

if sl.button("Suggest") and (topic_input!="" and not topic_input.isspace()):

    with sl.spinner('Getting suggestions'):
        result= client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
            {
                "role": "user",
                "content": getWorkSuggestionTemplate(work_type, topic_input),
            }
            ],
            stream=True
        )

    placeholder = sl.empty()
    full_response = ''
    for item in result:
        temp_str = item.choices[0].delta.content
        if temp_str is not None:
            full_response += temp_str
        placeholder.write(full_response)
    placeholder.write(full_response)

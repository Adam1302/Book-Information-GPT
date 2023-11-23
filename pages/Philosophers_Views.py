import streamlit as sl
from streamlit_extras.app_logo import add_logo
from st_pages import add_indentation
from utils.llm import getOpenAIClient
from utils.philosopher_list import shortened_philosopher_list, extensive_philosopher_list

sl.set_page_config(page_title="Philosopher Views", page_icon=":book:")
add_logo("pictures/essentials/logo_x_small.png")

add_indentation()

client = getOpenAIClient()

philosopherCol, pictureCol = sl.columns((1,2), gap='medium')
with pictureCol:
    sl.image("pictures/other/growing_tree.jpg")
with philosopherCol:
    sl.header("Philosopher Views")
    philosopher_list_type = sl.select_slider(
        label="Philosopher List:",
        options=['Reduced', 'Extensive']
    )

    if philosopher_list_type == 'Reduced':
        philosopher_list = shortened_philosopher_list
    else:
        philosopher_list = extensive_philosopher_list

    def get_philosophers():
        philsophers = sl.selectbox(
            f"Select philosopher:",
            philosopher_list,
        )
        return philsophers

    philosopher_selected = get_philosophers()

def get_topic():
    topic_they_want = sl.text_area(
        label=f"Enter or describe a topic or idea you want their opinion on:",
        placeholder="Enter here",
        key="topic_input"
    )
    return topic_they_want

topic_input = get_topic()

if sl.button(f"Get Opinion") and topic_input and philosopher_selected:

    with sl.spinner('Collecting'):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
            {
                "role": "user",
                "content": "Describe " + philosopher_selected + "'s opinion on the topic below. Answer with two paragraphs. TOPIC: " + topic_input,
            }
            ],
            stream=True
        )

    placeholder = sl.empty()
    full_response = ''
    for item in response:
        temp_str = item.choices[0].delta.content
        if temp_str is not None:
            full_response += temp_str
        placeholder.write(full_response)
    placeholder.write(full_response)


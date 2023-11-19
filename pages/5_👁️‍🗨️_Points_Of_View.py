import streamlit as sl
from streamlit_extras.app_logo import add_logo
from utils.llm import getOpenAIClient

sl.set_page_config(page_title="Point of View", page_icon=":book:")
add_logo("pictures/essentials/logo_x_small.png")

client = getOpenAIClient()

philosopherCol, pictureCol = sl.columns((1,1), gap='medium')
with pictureCol:
    sl.image("pictures/other/road_through_forest.jpg")
with philosopherCol:
    sl.header("Points of View")

    sl.markdown("In a world of increasing polarization, it is essential that we actively seek out and grapple with the unknown.")

    def get_topic():
        topic_they_want = sl.text_area(
            label=f"Enter or describe a topic or idea you'd like to see varying views about:",
            placeholder="Enter here",
            key="topic_input"
        )
        return topic_they_want

    topic_input = get_topic()

    open_mind_btn = sl.button(f"Open Your Mind")

if open_mind_btn and topic_input:

    with sl.spinner('We ask for your patience. This might take a couple minutes.'):

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
            {
                "role": "user",
                "content": "Provide as many different philosophical views as you can on the topic below. For each view, provide a paragraph of explanation. Rather than general and non-confrontation opinions, please provide specific opinionated stances.: Topic: " + topic_input,
            }
        ],
        ).choices[0].message.content

        sl.write(response)


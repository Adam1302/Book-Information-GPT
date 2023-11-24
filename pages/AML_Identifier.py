import streamlit as sl
from streamlit_extras.app_logo import add_logo
from st_pages import add_indentation
from utils.llm import getOpenAIClient
from utils.page_helpers.AML_Identifier_Helpers import getWorkTitle
from utils.templates import getTemplate, getWorkIntroductionTemplate, getWorkRatingTemplate

sl.set_page_config(page_title="Work_Identifier", page_icon=":book:")
add_logo("pictures/essentials/logo_x_small.png")

add_indentation()

client = getOpenAIClient()

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

if sl.button("Identify"):
    hasImbdRating = work_type == "Movie" or work_type == "TV Show" or work_type == "Documentary"

    with sl.spinner('Searching for work'):
        sl.markdown(f"### {work_type}:")
        work_info = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
            {
                "role": "user",
                "content": getTemplate(work_type, work_name_input),
            }
            ],
            stream=False
        ).choices[0].message.content
        sl.write(work_info)
    
    work_title = getWorkTitle(work_info, work_type).strip()
    if not work_title == "":
        if hasImbdRating:
            with sl.spinner('Searching for work'):
                sl.markdown("### iMDB Rating:")
                work_rating = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                    {
                        "role": "user",
                        "content": getWorkRatingTemplate(work_title),
                    }
                    ],
                    stream=False
                ).choices[0].message.content
            sl.write(work_rating)
        
        with sl.spinner("Retrieving more information"):
            sl.markdown("### About:")
            work_intro = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                {
                    "role": "user",
                    "content": getWorkIntroductionTemplate(work_title),
                }
                ],
                stream=True
            )

        # Streamed Output
        placeholder = sl.empty()
        full_response = ''
        for item in work_intro:
            temp_str = item.choices[0].delta.content
            if temp_str is not None:
                full_response += temp_str
            placeholder.write(full_response)
        placeholder.write(full_response)


import streamlit as sl
from streamlit_extras.app_logo import add_logo
from st_pages import add_indentation
from utils.llm import getOpenAIClient
from utils.philosopher_list import shortened_philosopher_list, extensive_philosopher_list


sl.set_page_config(page_title="Relative Opinions", page_icon=":book:")
add_logo("pictures/essentials/logo_x_small.png")

add_indentation()

client = getOpenAIClient()

sl.header("Philosophers: Relative Opinions")

philosopherListCol, relationTypeCol = sl.columns((1,1), gap='large')
with relationTypeCol:
    relation_type = sl.select_slider(
        'Opinion Relations:',
        options=['Agreements', 'Disagreements'],
    )
with philosopherListCol:
    reduced_philosopher_list = sl.toggle(
        "Reduced Philosopher List:",
    )

    if reduced_philosopher_list:
        philosopher_list = shortened_philosopher_list
    else:
        philosopher_list = extensive_philosopher_list

    def get_philosophers():
        philsophers = sl.multiselect(
            f"Select philosophers (max. 4):",
            philosopher_list,
            max_selections=4,
        )
        return philsophers

    philosophers_input = get_philosophers()

if sl.button(f"Get {relation_type}") and philosophers_input:

    if len(philosophers_input) == 1:
        sl.error("You must select multiple options.", icon='🚨')
    else:
        with sl.spinner('Collecting... This might take a couple minutes.'):
            philosophers_as_string = "{}, and {}".format(", ".join(philosophers_input[:-1]),  philosophers_input[-1])
            if relation_type == 'Agreements':
                opinions_result= client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                    {
                        "role": "user",
                        "content": "What are some opinions shared by " + philosophers_as_string,
                    }
                    ],
                    stream=True
                )
            else:
                opinions_result= client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                    {
                        "role": "user",
                        "content": "What are some topics of disagreement between " + philosophers_as_string,
                    }
                    ],
                    stream=True
                )
        placeholder = sl.empty()
        full_response = ''
        for item in opinions_result:
            temp_str = item.choices[0].delta.content
            if temp_str is not None:
                full_response += temp_str
            placeholder.write(full_response)
        placeholder.write(full_response)


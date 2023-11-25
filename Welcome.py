#from apikey import apikey # to run locally, not on Git
#from email_info import receivingEmail, receivingEmailKey # Ignored in Git
import os
import streamlit as sl
from streamlit_extras.app_logo import add_logo
from st_pages import show_pages_from_config, add_indentation

#os.environ['OPENAI_API_KEY'] = apikey
#os.environ['receivingEmailKey'] = receivingEmailKey

# ART MEDIA LITERATURE: IDEAS

# Whenever you're developing, consider using session state: https://docs.streamlit.io/library/api-reference/session-state
### Add Session State for everything
### I want to save widget selections and text entries

# Deploy:
### https://docs.streamlit.io/library/get-started/create-an-app#share-your-app

# OpenAI Pricing

# After deploying, change the form submit landing page after submission:
### https://formsubmit.co/documentation
# Then, create an use an official site email (ex. "AMLTeam@outlook.com")

# Advertise
### Create reddit account and share

# Also look into this: https://docs.github.com/en/pages

## STREAMLIT PAGE
sl.set_page_config(page_title="Art_Finder", page_icon=":book:")
add_logo("pictures/essentials/logo_x_small.png")

add_indentation()
show_pages_from_config()

@sl.cache_resource
def getPageImage():
    return sl.image("pictures/other/magritte_the_son_of_man.jpg", width=400)

titleCol, imageCol = sl.columns({1,1.5}, gap='large')
with titleCol:
    sl.title("Art, Media, and Literature (AML): A Navigator")
    sl.divider()
    sl.subheader("A Work Suggestor and Identifier")
    sl.divider()
    sl.write("Click the 'About' tab to learn more")
with imageCol:
    getPageImage()


import os
import streamlit as sl
from streamlit_extras.app_logo import add_logo
from apikey import apikey # stored locally, not on Git


os.environ['OPENAI_API_KEY'] = apikey

# ART MEDIA LITERATURE: IDEAS
## AS PER: https://www.youtube.com/watch?v=U_eV8wfMkXU
#   we will have a nice multi-columned explanation of what this site does

# Change Feedback Form using this: https://docs.streamlit.io/library/api-reference/control-flow 

# Add buttons for generating identifiers/suggestors

# Add Page:
### Give a checkbox/multiselect list of philosophers
### For all philosophers clicked, get some opinions shared by them
### ex. What are some opinions shared by Plato, Nietzsche, and Arendt?

# Add Page: Prevailing opinions and timeframes
### Use a slider for timeframe and a textbox for topic
### ex. What was the prevailing opinion in the 1810s about multi-culturalism?
### optional: location

# Everything here: https://docs.streamlit.io/library/api-reference/status 

# Add Page: What did {philosopher} say about {topic/description}?
### We'll need a list of philosophers

# Add Page: Works within Timeframes
### Find X {work_type}s within the time range (specified by two-headed slider)
### https://youtu.be/sCvdt79asrE?list=TLGGTGC9_GhF4fYxMzExMjAyMw 

# Page Idea: Give X different opinions on "topic/description" from philosophers

# Add expanders on the About page to descibe the page functionalities

# Use sl.status to show status: https://docs.streamlit.io/library/api-reference/status/st.status
### Use this for loading responses

# After finishing the rest of these, look at wtf this means: https://docs.streamlit.io/library/api-reference/session-state 

# Use st.progress() to show progress
### https://docs.streamlit.io/library/get-started/main-concepts#show-progress
### You could have a slider or a text-based setup

### Feedback page: actual implementation

# Once all features are in, fix the layout: https://docs.streamlit.io/library/get-started/main-concepts#layout
### search up how to make streamlit look nice
### Use header, subheader, markdown, write, etc.
### Have the input columns in a nice sidebar: https://docs.streamlit.io/library/get-started/multipage-apps/create-a-multipage-app

# For long-running functions: https://docs.streamlit.io/library/get-started/main-concepts#caching
### this is a MUST-do for all functions that have similar runs

# Use WIkipedia API to link names to their pages

# Re-organize everything into different files, proper style/organization

# Deploy:
### https://docs.streamlit.io/library/get-started/create-an-app#share-your-app

# Advertise
### Create reddit account and share

## TO BE MORE SPECIFIC, WE CAN HAVE MULTIPLE INPUT BOXES ##
# ex. author, 

# Geospatial image of where artists, authors, lived/were born https://docs.streamlit.io/library/get-started/multipage-apps/create-a-multipage-app

## STREAMLIT PAGE
sl.set_page_config(page_title="Art_Finder", page_icon=":book:")
add_logo("pictures/essentials/logo_x_small.png")

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


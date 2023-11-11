import os
import streamlit as sl
from apikey import apikey # stored locally, not on Git


os.environ['OPENAI_API_KEY'] = apikey

# ART MEDIA LITERATURE: IDEAS
## AS PER: https://www.youtube.com/watch?v=U_eV8wfMkXU
#   we will have a nice multi-columned explanation of what this site does

# Creating Pages
# https://docs.streamlit.io/library/get-started/multipage-apps
### Create a main page with a nice picture or two
### Create a nice About page with expandable drop-downs for each
### Create a page for each service
### Create a contact page and email
### Add emojis for each page (1_[emoji]_pagename.py)

# Use st.progress() to show progress
### https://docs.streamlit.io/library/get-started/main-concepts#show-progress
### You could have a slider or a text-based setup

# Branding: "Work" --> "AML"

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

# "Topic prompts: in the style of '...'"
### creativity widget that controls temperature
### 

# Geospatial image of where artists, authors, lived/were born https://docs.streamlit.io/library/get-started/multipage-apps/create-a-multipage-app

# AMAZON/KINDLE links (NVM: this is pretty expensive since you'll need an API like Rainforest)

## STREAMLIT PAGE
sl.set_page_config(page_title="Art_Finder", page_icon=":book:")

sl.write("WORK")
sl.markdown("Here's what we offer:")
sl.write("Work Suggestor: Receive a list of suggested works to look at based on what you're looking for")
sl.write("Work Identifier: Enter the name or a description of a specific work and recieve information about it")

import streamlit as sl
from streamlit_extras.app_logo import add_logo
from st_pages import add_indentation
from utils.strings import site_description, site_technology_description

sl.set_page_config(page_title="About", page_icon=":book:")
add_logo("pictures/essentials/logo_x_small.png")

add_indentation()

@sl.cache_resource
def getPageImage():
    return sl.image('pictures/other/searching_for_light.jpg')

textCol, imageCol = sl.columns((1,1.2), gap='large')
with textCol:
    sl.header("About AML")
    sl.markdown(site_description)
    sl.markdown(site_technology_description)
    sl.markdown("Please offer us some feedback in the 'Give Us Feedback' tab.")

with imageCol:
    getPageImage()

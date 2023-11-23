from email_info import receivingEmail, receivingEmailKey # Ignored in Git
import re
import streamlit as sl
from streamlit_extras.app_logo import add_logo
from utils.email import email_regex

sl.set_page_config(page_title="Feedback", page_icon=":book:")
add_logo("pictures/essentials/logo_x_small.png")

sl.header("Give Us Feedback")
sl.markdown("Please note that this site is not for-profit and is personally funded by its creator; as a result, due to time and resource limitations, not all feedback can be implemented. However, I will try my best, and appreciate the feedback regardless.")

sl.markdown("If you would like a response, please provide your email.")

contact_form = f"""
<form action="https://formsubmit.co/{receivingEmailKey}" method="POST">
    <input type="email" name="email" placeholder="Your email (optional)">
    <textarea name="message" placeholder="Your message here"></textarea>
    <button type="submit">Send</button>
    <input type="text" name="_honey" style="display:none">
    <input type="hidden" name="_template" value="table">
</form>
"""

sl.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        sl.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")


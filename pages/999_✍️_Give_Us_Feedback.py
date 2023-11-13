import re
import streamlit as sl
from streamlit_extras.app_logo import add_logo
from utils.email import email_regex

sl.set_page_config(page_title="Feedback", page_icon=":book:")
add_logo("pictures/essentials/logo_x_small.png")

sl.header("Give Us Feedback")
sl.markdown("Please note that this site is not for-profit and is personally funded by its creator; as a result, due to time and resource limitations, not all feedback can be implemented. However, I will try my best, and appreciate the feedback regardless.")

sl.markdown("If you would like a response, please provide your email.")

def get_email():
    email = sl.text_area(
        label="Email (optional): ",
        placeholder="Enter email here",
        key="email_input"
    )
    return email
def get_feedback():
    feedback = sl.text_area(
        label="Feedback: ",
        placeholder="Enter feedback here",
        key="feedback_input"
    )
    return feedback

def check_email_validity(email):
    return email=="" or email.isspace() or re.fullmatch(email_regex, email)

email_text = get_email()
feedback_text = get_feedback()
if feedback_text:
    sl.write("BUTTON HERE")

    if not check_email_validity(email_text):
        sl.write("ERROR: Invalid email provided. Either enter a valid email or none at all.")

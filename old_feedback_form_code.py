# def get_email():
#     email = sl.text_input(
#         label="Email (optional): ",
#         placeholder="Enter email here",
#         key="email_input"
#     )
#     return email
# def get_feedback():
#     feedback = sl.text_area(
#         label="Feedback: ",
#         placeholder="Enter feedback here",
#         key="feedback_input"
#     )
#     return feedback

# def check_email_validity(email):
#     return email=="" or email.isspace() or re.fullmatch(email_regex, email)


# email_val = get_email()
# feedback_val = get_feedback()

# # Every form must have a submit button.
# if sl.button("Submit"):
#     if not check_email_validity(email_val):
#         sl.error(":red[ERROR: Invalid email provided. Either enter a valid email or none at all.]", icon="🚨")
#         submitted = False
#     elif feedback_val=="" or feedback_val.isspace():
#         sl.error(":red[ERROR: You haven't provided any feedback]", icon="🚨")
#         submitted = False
#     else:
#         sl.write(":green[... Feedback submitted (but not implemented)]")


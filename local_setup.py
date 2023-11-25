from apikey import apikey # to run locally, not on Git
from email_info import receivingEmail, receivingEmailKey # Ignored in Git
import os

os.environ['OPENAI_API_KEY'] = apikey
os.environ['receivingEmailKey'] = receivingEmailKey

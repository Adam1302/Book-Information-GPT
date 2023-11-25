# Art, Media, Literature (AML)

To run locally:

1. Clone the repo
2. Create or login to an account on https://platform.openai.com
3. Obtain your API key from https://platform.openai.com/api-keys
4. Create a file in the root folder of this repo titled "apikey.py"
5. In a local file "apikey.py" in the 'page_helpers' directory, insert the line apikey='[YOUR API KEY HERE]'
6. In a local file "email_info.py" in the 'page_helpers' directory, insert the line receivingEmailKey='[YOUR EMAIL HERE]'
6. In Welcome.py, uncomment the local_setup import line
9. From a terminal, run 'pip install -r requirements.txt'
10. From a terminal, run 'streamlit run main.py'
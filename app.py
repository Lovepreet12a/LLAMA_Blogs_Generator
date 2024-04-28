import streamlit as st 
from langchain.prompts import PromptTemplate 
from langchain.llms import CTransformers 
import re 

st.set_page_config(page_title= "Generate Blogs",
                   page_icon= "🤖",
                   layout= "centered",
                   initial_sidebar_state= "collapsed")


# Background image
st.image("static/background.jpg", width= 100)

# Main header
st.header("Welcome to my Blogs Generator 🤖")

input_text = st.text_input("Enter the Blog Topic")


# Creating the LLAMA function -----------------
def getLLamaresponse(input_text, no_words, blog_style):
    llm = CTransformers(model = 'llama-2-7b-chat.ggmlv3.q8_0.bin', model_type = 'llama', config = {'temperature':0.01})

    # prompt template
    template = """
                Write a blog for {blog_style} job profile for a topic {input_text} within {no_words} words.
                """
    
    prompt = PromptTemplate(input_variables= ["blog_style", "input_text", "no_words"], template= template)

    # Generate the response from the LLAMA 2 Model
    response = llm(prompt.format(blog_style= blog_style, input_text = input_text, no_words = no_words))

    response = re.sub(r'(\d+\.)', r'\n\1', response)

    print(response)
    return response



# Creating two more columns for additional 2 fields

col1, col2 = st.columns([5,5])

with col1:
    no_words = st.text_input("No. of Words")
with col2:
    blog_style = st.radio("Writing the blog for", ("Researchers", "Data Scientists", "Common People"), index= 0)

# Submit button
submit = st.button("Generate")

# Get the response 
if submit:
    st.write(getLLamaresponse(input_text, no_words, blog_style))




import streamlit as st
import cohere

api_key = "grqC06lVj3LoESQ9ySHbEnBhNUEiRd82kDE4IVKi"
co = cohere.Client(api_key)
# Page title
st.set_page_config(page_title='🔗Yaswanth GPT🔗',layout='wide')
st.title('🦜🔗 Yaswanth ChatGPT App')
# generate responce function will generate the results based on user's querry.
def generate_response(query):
    template = f"""/
    I want you to act as guide to answer the questions of user

    tag line : "Welcome to Yaswanth chatGPT APP"
    Consider the user's question is :{query}, Your role is to generate the results based on user question in 2-3 sentences and include the tagline as starting statement.
    """
    response = co.generate(
    model='command-nightly',
    prompt = template,
    max_tokens=2000, # This parameter is optional.
    temperature=0.50)
    generated_output = response.generations[0].text
    return generated_output
# Text input
txt_input = st.text_area('Enter your query', '', height=25)

# Form to accept user's text input for summarization
result = []
with st.form('summarize_form', clear_on_submit=False):
    cohere_api_key = "grqC06lVj3LoESQ9ySHbEnBhNUEiRd82kDE4IVKi"
    submitted = st.form_submit_button('Generate')
    
    with st.spinner('Generating Unit Description...'):
        response = generate_response(txt_input)
        result.append(response)
            #del cohere_api_key

if len(result):
    st.info(response)


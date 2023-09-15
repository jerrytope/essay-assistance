import streamlit as st
import openai
openai.api_key = "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"

st.header("Essay Generator")
review  = st.text_area("Enter the Topic of your essay")
button = st.button("Generate Reply")

def generate_reply(review):
       
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=review,
    temperature=0.7,
    max_tokens=803,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)
    # st.write(response)
    return response.choices[0].text

if button and review:
    with st.spinner("Generating Reply..."):
        reply = generate_reply(review)
    st.write(reply)
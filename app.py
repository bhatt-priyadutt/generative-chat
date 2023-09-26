import os
import streamlit as st
from langchain.prompts import PromptTemplate
from zenml.client import Client

def get_vector_store():
    """Get the vector store from the pipeline."""
    c = Client()
    pipeline = c.get_pipeline(name_id_or_prefix='docs_to_index_pipeline')
    our_run = pipeline.last_successful_run
    print("Using pipeline: ", pipeline.name)
    return our_run.steps["index_generator"].output.load()

def run_app():
    # Define a simple Streamlit app
    st.title("Ask Me")
    query = st.text_input("What would you like to ask?", "")

    # If the 'Submit' button is clicked
    if st.button("Submit"):
        if not query.strip():
            st.error(f"Please provide the search query.")
        else:
            vector_index = get_vector_store()


            prompt_template = """You are a helpful assistant for our website.

            {context}

            Question: {question}
            Answer here:"""
            PROMPT = PromptTemplate(
                template=prompt_template, input_variables=["context", "question"]
            )
            from langchain.llms import OpenAI
            from langchain.chains import RetrievalQA

            chain_type_kwargs = {"prompt": PROMPT}

            llm = OpenAI(openai_api_key=os.getenv('OPENAI_API_KEY'))
            qa = RetrievalQA.from_chain_type(
                llm=llm,
                chain_type="stuff",
                retriever=vector_index.as_retriever(),
                chain_type_kwargs=chain_type_kwargs,
            )


            st.success(qa.run(query))
run_app()
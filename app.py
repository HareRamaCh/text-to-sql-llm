from dotenv import load_dotenv
load_dotenv() # Load all the environment variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

# Configure our API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Google Gemini and provide query as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

# Function to retrieve data from SQL database using generated query
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()

    for row in rows:
        print(row)
    return rows

# Define your prompt (Important Step!)
prompt = [
    '''
    You are an expert in converting English questions to SQL queries.
    The SQL database has the name BOOK and the following columns - 
    NAME, GENRE, AUTHOR, PAGES \n \nFor example, \nExample 1 - How many
    entries of records are present?, the SQL command will be something
    like this SELECT COUNT(*) FROM BOOK ;\nExample 2 - List all the 
    self-help books, the SQL command will be something like this SELECT
    * FROM BOOK WHERE GENRE="Self-Help" Also the SQL code should not 
    have ``` in beginning or end and sql word in the output.
    '''
]

# Streamlit App
st.set_page_config(page_title="End-to-End Text to SQL LLM")
st.header("Gemini App to Retrieve SQL Data")

question = st.text_input("Enter your question here: ", key="input")

submit = st.button("Submit & retrieve response")

# When submit is clicked
if submit:
    response = get_gemini_response(question, prompt)
    print(response)
    data = read_sql_query(response, "book.db")
    st.subheader("The response is")
    for row in data:
        print(row)
        st.header(row)

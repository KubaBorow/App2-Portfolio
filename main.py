import streamlit as st
import pandas


# Pandasa używamy np do odczytu plików csv


st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Jakub Borowicki")
    content = """
    Hi, I am Kuba! As a beginner Python programmer, I'm just starting to grasp the fundamentals of coding,
    exploring concepts like variables, loops, and functions.
    I'm eager to apply my growing knowledge by writing simple programs and solving basic problems.
    Through practice and experimentation, I'm steadily building confidence in my coding abilities.
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have build in Python. Feel free to contact me!
"""
st.write(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv('data.csv', sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])


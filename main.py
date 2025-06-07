import streamlit as st

st.set_page_config(page_title="GeoLearn", page_icon="🌍", layout="centered")

st.title("🌍 GeoLearn")
st.subheader("Your Friendly Geography Teacher")
st.write("Welcome! Use the sidebar to explore continents, countries, and take quizzes.")

st.image("https://upload.wikimedia.org/wikipedia/commons/9/95/Continents.svg", caption="Continents of the World", use_container_width=True)
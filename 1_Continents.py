import streamlit as st

st.title("🗺️ Learn About Continents")

continents = {
    "Asia": "Largest and most populous continent.",
    "Africa": "Known for wildlife and the Nile River.",
    "Europe": "Rich in art, history, and architecture.",
    "North America": "Home to the USA, Canada, Mexico.",
    "South America": "Amazon rainforest and Andes mountains.",
    "Australia": "Island continent with unique animals.",
    "Antarctica": "Icy and uninhabited (except researchers)."
}

choice = st.selectbox("Pick a continent", list(continents.keys()))
st.markdown(f"### 🌍 {choice}")
st.info(continents[choice])
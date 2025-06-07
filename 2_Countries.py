import streamlit as st

st.title("🌐 Explore Countries")

countries = {
    "India": {
        "capital": "New Delhi",
        "flag": "https://flagcdn.com/w320/in.png",
        "fact": "Home to the Himalayas and the Taj Mahal."
    },
    "France": {
        "capital": "Paris",
        "flag": "https://flagcdn.com/w320/fr.png",
        "fact": "Famous for the Eiffel Tower and wine."
    },
    "Brazil": {
        "capital": "Brasília",
        "flag": "https://flagcdn.com/w320/br.png",
        "fact": "Has the Amazon rainforest and Christ the Redeemer statue."
    }
}

choice = st.selectbox("Choose a country", list(countries.keys()))
data = countries[choice]

st.image(data["flag"], width=150)
st.markdown(f"**Capital:** {data['capital']}")
st.success(f"📌 Fun Fact: {data['fact']}")
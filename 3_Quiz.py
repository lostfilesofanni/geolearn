import streamlit as st

st.title("🧠 Capital City Quiz")

quiz_data = {
    "India": "New Delhi",
    "France": "Paris",
    "Brazil": "Brasília"
}

score = 0

st.write("Type the capital of the following countries:")

for country, capital in quiz_data.items():
    answer = st.text_input(f"{country}:", key=country)
    if answer:
        if answer.strip().lower() == capital.lower():
            st.success("✅ Correct!")
        else:
            st.error(f"❌ Wrong! It's {capital}.")

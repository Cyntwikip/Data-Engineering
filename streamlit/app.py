import streamlit as st

st.title("Streamlit Demo App")
st.write("This is a basic Streamlit app.")

# Input box
name = st.text_input("Enter your name:")

# Button to display greeting
if st.button("Greet"):
    st.write(f"Hello, {name}!")
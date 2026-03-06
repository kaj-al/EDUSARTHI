import streamlit as st 
from memory import convo
from prompt import response

st.set_page_config(
    page_title="EDUSARTHI",
    page_icon="📚",
    layout="centered"
)

st.title("EDUSARTHI")
st.write("Your Sarthi in study")

if "memory" not in st.session_state:
    st.session_state.memory = convo()

lang = st.selectbox(
    "Select response language",
    ["English","Hindi","Hinglish"]
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.wriite(msg["content"])

input = st.chat_input("Ask your question...")

if input:
    st.chat_message("user").write(input)
    st.session_state.messages.append({
        "role":"user",
        "content":input
    })
    reply = response(
        input,
        lang,
        st.session_state.memory
    )
    st.chat_message("assistant").write(reply)
    st.session_state.messages.append({
        "role":"assistant",
        "content":reply
    })
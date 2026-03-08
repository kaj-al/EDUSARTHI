import streamlit as st
from memory import convo
from prompt import get_response

st.set_page_config(
    page_title="AI Learning Coach",
    page_icon="🎓"
)

st.title("🎓 AI Learning Coach")
st.write("Learn → Practice → Improve")

# memory
if "memory" not in st.session_state:
    st.session_state.memory = convo()

# chat display
if "messages" not in st.session_state:
    st.session_state.messages = []

# sidebar controls
st.sidebar.title("Learning Settings")

language = st.sidebar.selectbox(
    "Language",
    ["English", "Hindi", "Hinglish"]
)

topic = st.sidebar.text_input("Topic to Learn")

start = st.sidebar.button("Start Learning")

# start learning
if start and topic:

    reply = get_response(topic, language, st.session_state.memory)

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )

# show chat
for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# user answer
user_input = st.chat_input("Your answer or next question...")

if user_input:

    st.chat_message("user").write(user_input)

    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    reply = get_response(
        user_input,
        language,
        st.session_state.memory
    )

    st.chat_message("assistant").write(reply)

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )
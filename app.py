import streamlit as st
from memory import convo
from prompt import get_response

st.set_page_config(
    page_title="EDUSARTHI",
)
st.markdown("""
<style>
    /*Main app background*/
    .stApp {
        background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
    }
    /*Title*/
    h1{
        text-align:center;
        color:2c3e50;
        font-family:'Segoe UI',sans-serif;
    }
    /*Chat*/
    [data-testid="stChatMessage"]{
        border-radius:15px:
        padding:10px;
        margin-bottom:10px;
    }
    /*User msg*/
    [data-testid="stChatMessage"][data-testid="user"]{
        background-color:#d1e7ff
    }
    /*ai msg*/
    [data-testid="stChatMessage"][data-testid="assistant"]{
        background-color:#e8f5f9
    }
    /*sidebar*/
    section[data-testid="stSidebar"]*{
        color:white;
    }
    /*buttons*/
    .stButton>button{
        background-color:#4CAF50;
        color:white;
        border-radius:10px:
        padding:10px 20px;
        border:none      
    }
    /*buttons hover*/
    .stbutton>button:hover{
        background-color:#45a049;   
    }
    /*chat box*/
    [data-testid="stChatInput"]textarea{
        border-radius:12px:
        border:2px solid #4CAF50;
    }
    <style>
""",unsafe_allow_html=True)

st.title("EduSarthi")
st.write("Learn → Practice → Improve")

# memory
if "memory" not in st.session_state:
    st.session_state.memory = convo()

# chat 
if "messages" not in st.session_state:
    st.session_state.messages = []

# sidebar 
st.sidebar.title("Learning Settings")

language = st.sidebar.selectbox(
    "Language",
    ["English", "Hindi", "Hinglish","French"]
)

topic = st.sidebar.text_input("Topic to Learn")

start = st.sidebar.button("Start Learning")

# start 
if start and topic:
    reply = get_response(topic, language, st.session_state.memory)
    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )

# show chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

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
    st.chat_message("ai").write(reply)
    st.session_state.messages.append(
        {"role": "ai", "content": reply}
    )

    
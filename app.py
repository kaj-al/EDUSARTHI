import streamlit as st
from memory import convo
from prompt import get_response

st.set_page_config(
    page_title="EDUSARTHI",
    initial_sidebar_state="expanded",
    layout="wide"
)

st.markdown("""
<style>
    /* Main app background */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        min-height: 100vh;
    }
    
    /* Title styling */
    h1 {
        text-align: center;
        color:#FFFFFF !important;
        font-family: 'Segoe UI', sans-serif;
        font-size: 3em;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        margin-bottom: 10px;
    }
    
    /* Subtitle */
    .stMarkdown p {
        
        color: #e0e0e0;
        font-size: 1.1em;
    }
    
    /* Chat messages */
    [data-testid="stChatMessage"] {
        border-radius: 15px;
        padding: 15px;
        margin-bottom: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    /* User message */
    [data-testid="stChatMessage"][data-testid="user"] {
        background-color: #e8f5f9 !important;
        border-left: 4px solid #667eea;
    }
    
    /* Assistant message */
    [data-testid="stChatMessage"][data-testid="assistant"] {
        background-color: #e8f5f9;
        border-left: 4px solid #764ba2;
    }
    
    
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        padding: 12px 24px;
        border: none;
        font-weight: bold;
        width: 100%;
        transition: transform 0.2s;
    }
    
    /* Button hover */
    .stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 12px rgba(102, 126, 234, 0.4);
    }
    
    /* Chat input */
    [data-testid="stChatInput"] textarea {
        border-radius: 12px;
        
        background-color: #f0f0f0;
    }
    
    /* Input fields */
    input[type="text"] {
        border-radius: 8px;
        border: 2px solid #667eea;
        padding: 10px;
        background-color:#ffffff;
        color:#000000;
    }
    
    /* Selectbox */
    .stSelectbox div[data-baseweb="select]>div{
        background-color:#ffffff;
        color:#000000 !important;
        border-radius: 8px;
    }
    /* SIDEBAR SELECTBOX - selected text */
    section[data-testid="stSidebar"] div[data-baseweb="select"] * {
        color: black !important;
    }

    /* SIDEBAR TEXT INPUT */
    section[data-testid="stSidebar"] input {
        color: black !important;
        background-color: white!important;
    }

    /* SELECTBOX BOX BACKGROUND */
    section[data-testid="stSidebar"] div[data-baseweb="select"] > div {
        background-color: black !important;
    }

    /* REMOVE GLOBAL WHITE TEXT (THIS WAS BREAKING IT) */
    section[data-testid="stSidebar"] * {
        color: unset !important;
    }

</style>
""", unsafe_allow_html=True)

st.title("EduSarthi")
st.markdown("<p style='text-align: center; color: #e0e0e0; font-size: 1.2em;'>Learn → Practice → Improve</p>", unsafe_allow_html=True)

# Memory initialization
if "memory" not in st.session_state:
    st.session_state.memory = convo()

# Chat messages initialization
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar
st.sidebar.title("Setup Your Learning ")

language = st.sidebar.selectbox(
    "Language",
    ["English", "Hindi", "Hinglish", "French"]
)

topic = st.sidebar.text_input("Topic to Learn", placeholder="Enter a topic...")

start = st.sidebar.button("Start Learning")

# Start learning
if start and topic:
    reply = get_response(topic, language, st.session_state.memory)
    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )

# Display chat
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
    st.chat_message("assistant").write(reply)
    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )
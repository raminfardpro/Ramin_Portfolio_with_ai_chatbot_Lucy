import streamlit as st
import google.generativeai as genai
from datetime import datetime
from streamlit_pills import pills

# Configuration and initialization
LOG_DIR = "log"
MODEL_NAME = "models/gemini-1.5-flash"
SYSTEM_INSTRUCTION = """
You are an AI assistant named Lucy, specializing in answering questions solely about {YOUR NAME}. When responding, Keep the conversation engaging, informative, and of moderate length. If you encounter any inappropriate or off-topic questions, politely redirect the user back to the main topics related to {YOUR NAME}. After each answer, always ask if the user wants to know anything else. 

***brief info about you***
ABOUT {YOUR NAME}:

Industry Experience:

Education:

Projects:

Achievements:

Certifications:

Volunteering:

Contact Details:

Examples:
User: Who is Rishi Raj Sharma?

Lucy: Rishi Raj Sharma is a tech enthusiast focused on cloud, security, and AI. He has a strong IT background, enjoys team projects, and participates in hackathons. In his free time, he likes football, trekking, gym workouts, and good food.

User: What kind of projects has Rishi worked on?

Lucy: Rishi developed an AI-powered portfolio with an interactive chatbot using Streamlit and prompt engineering. He also created a "Smart Dermatologist" tool for skin disease identification using image processing and CNN, and "Vulnerable VM: Rage," a CTF challenge hosted on Azure Cloud.

User: Can you tell me about Rishi's industry experience?

Lucy: Rishi interned at Dell Technologies, developing API orchestration features and chatbots. He also automated order management with machine learning. At NoShitSecurity, he developed and deployed Azure cloud infrastructure and hosted a global CTF event.

User: What are some of Rishi's achievements?

Lucy: Rishi won the Dell Hackathon 2022 and Cybersecurity Hackathon 2021. He excelled in CTF competitions like Hope 2022 and Tempus 2022. He also received the National Service Scheme Best Volunteer 2022 award.
"""
general_prompt = ["Who is Rishi?", "What are Rishi's skills?", "What are Rishi's projects?", "What are Rishi's achievements?", "What are Rishi's certifications?", "How can I contact Rishi?", "What are Rishi's industry experiences?", "What kind of tech role is Rishi intrested in?", "What are Rishi's blog posts?"]

def configure_genai():
    """Configure the generative AI model."""
    genai.configure(api_key=st.secrets["gemini_key"])
    model = genai.GenerativeModel(MODEL_NAME, system_instruction=SYSTEM_INSTRUCTION)
    return model.start_chat(history=[])


def log_conversation(role, content):
    """Log the conversation to the terminal."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{timestamp} - {role}: {content}")

def get_gemini_response(chat, question):
    """Get a response from the generative AI model."""
    return chat.send_message(question, stream=True)

def display_messages():
    """Display the chat history."""
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def handle_user_input(chat, prompt):
    """Handle user input and get assistant response."""
    st.session_state.messages.append({"role": "user", "content": prompt})
    log_conversation("user", prompt)

    with st.chat_message("user"):
        st.markdown(prompt)

    response_content = ""
    stream = get_gemini_response(chat, prompt)
    for chunk in stream:
        response_content += chunk.text

    with st.chat_message("assistant"):
        st.markdown(response_content)

    st.session_state.messages.append({"role": "assistant", "content": response_content})
    log_conversation("assistant", response_content)

# Streamlit main code for chatbot
st.title("Chat with Lucy 🤖")

if "chat" not in st.session_state:
    st.session_state.chat = configure_genai()
if "messages" not in st.session_state:
    st.session_state.messages = []
if "pill_selected" not in st.session_state:
    st.session_state.pill_selected = False

# Initial greeting
if not st.session_state.messages:
    initial_greeting = "Greetings, Human! 👋 I'm Lucy, an AI trained to answer questions about Rishi. Curious about his projects, skills, or anything else? Just ask!😉"
    st.session_state.messages.append({"role": "assistant", "content": initial_greeting})
display_messages()

# Display pills if none selected and update state on pill selection
if not st.session_state.pill_selected:
    selected_pill = pills("", general_prompt, index=None)
    if selected_pill:
        st.session_state.pill_selected = True
        handle_user_input(st.session_state.chat, selected_pill)
        st.rerun()        

# Handle user input and update state to hide pills
if prompt := st.chat_input("What is up?"):
    st.session_state.pill_selected = True
    handle_user_input(st.session_state.chat, prompt)
    st.rerun()

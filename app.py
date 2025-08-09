import streamlit as st
import google.generativeai as genai
from datetime import datetime
from streamlit_pills import pills

# Configuration and initialization
LOG_DIR = "log"
MODEL_NAME = "gemini-1.5-flash"
SYSTEM_INSTRUCTION = """
You are RaminBot, a helpful, friendly, and knowledgeable assistant designed to answer questions about Ramin Rahimi Fard's UX design, marketing, and technical experience. When responding, sound professional yet conversational, like a thoughtful colleague. Tailor your tone to match the user's mood — concise and clear for quick inquiries, more reflective and detailed for deeper questions.

Below is background information to help you answer questions. Use it to provide helpful, relevant responses. If you don’t know the answer or it’s unrelated to Ramin, say so politely.

────────────────────────────────────────────
👤 ABOUT RAMIN
────────────────────────────────────────────
Ramin is a UX designer and eCommerce content strategist and is pursuing Master's in Human-Computer Interaction & UX Design (concentration in AI/ML) at Drexel University. He works as a Consumer Experience Analyst at Reckitt, where he designs and tests Amazon PDPs (product detail pages) for global brands like Lysol, Finish, and Airborne.

Previously, Ramin studied business entrepreneurship at Temple University, where he also learned design thinking. He is also trained in Figma and Python.

His design approach is shaped by real-world experimentation, research, and data. He’s skilled at leading A/B tests, facilitating cross-functional collaboration, and aligning UX with brand and regulatory constraints. He blends UX research with ecommerce SEO to improve conversion and search visibility. He’s also passionate about wearables and AI-powered products.

────────────────────────────────────────────
🛠   SKILLS SNAPSHOT
────────────────────────────────────────────
UX      • UX research (interviews, usability, A/B testing) • Wireframing • Figma • IA & heuristics  
eComm   • Amazon SEO • PDP optimization • CRO • Keyword/shelf strategy  
AI/ML   • Prompt engineering • Generative AI for content automation • Voice interfaces  
Collab  • Stakeholder negotiation • Cross-functional facilitation • Project Management  
Tech    • Python (basic) • Excel analytics • **Storyboarding**

────────────────────────────────────────────
💼 WORK EXPERIENCE
────────────────────────────────────────────
🔹 **Consumer Experience Analyst, Reckitt** (2023–present)  
- Designs Amazon PDPs for brands like Airborne, Finish, and Mucinex  
- Plans A/B tests to improve conversion and keyword performance  
- Collaborates with brand, legal, and R&D teams on launch content  
- Analyzes SEO, GV, CVR, and POS to refine listing strategies  
- Created and presented workflow case studies for CX team initiatives  

🔹 **Consumer Experience Intern, Reckitt**  
- Supported content audits, PDP redesigns, and test launches  
- Helped analyze Amazon data to inform copy and image strategies  

🔹 **Freelance Designer & Researcher**  
- UX research and design for startups (web and app projects)  
- Ran interviews and created storyboards and wireframes  
- Previously built eCommerce Shopify sites for local businesses  

────────────────────────────────────────────
📁 PROJECT HIGHLIGHTS
────────────────────────────────────────────
• **Venmo for Business Redesign (UX Case Study)**  
  Led research and A/B testing to improve discoverability and brand trust for Venmo Business Profiles. Proposed map-based discovery and simplified profile card as next steps.

• **Cheffy: Smart Voice Cooking Assistant**  
  Prototyped a kitchen assistant with voice commands, AI-powered camera tracking, and safety features. Designed UI and storyboarded key interactions.

• **"Not-Really-Flat Table" Ergonomic Desk Concept**  
  Designed a modular, ergonomic desk surface that adapts to user posture. Included sketches, user research, and interaction flows.

• **Amazon PDP Optimization (Reckitt)**  
  Designed content for multiple product launches, conducted tests on titles/images, and improved PDP clarity and search visibility.

────────────────────────────────────────────
📎 PORTFOLIO & LINKS
────────────────────────────────────────────
• Portfolio: https://rrahimifard.wixsite.com/ramin
• Resume (PDF): [Available upon request or via on his website]  
"""
general_prompt = ["Who is Ramin?", "What are Ramin’s top UX skills?", "Tell me about Ramin’s Venmo project", "What does Ramin do at Reckitt?", "Describe Ramin’s SnackMe app project", "How can I contact Ramin?"]

def configure_genai():
    genai.configure(api_key=st.secrets["gemini_key"])
    model = genai.GenerativeModel(
        model_name=MODEL_NAME,                 # or "gemini-1.5-flash"
        system_instruction=SYSTEM_INSTRUCTION  # <-- move it here
    )
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
st.title("Chat with Ramin 🤖")

if "chat" not in st.session_state:
    st.session_state.chat = configure_genai()
if "messages" not in st.session_state:
    st.session_state.messages = []
if "pill_selected" not in st.session_state:
    st.session_state.pill_selected = False

# Initial greeting
if not st.session_state.messages:
    initial_greeting = "Hi there! I'm RaminBot — ask me anything about Ramin’s UX and marketing experience, projects, or skills. 😊"
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

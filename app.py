import streamlit as st
from groq import Groq
import urllib.parse
import base64

# 1. High-End Viewport Optimization (Gemini Canvas Ratio)
st.set_page_config(page_title="Gemini Pro // WeHateNerdsAI", page_icon="✨", layout="wide")

# 2. Perfect Google Gemini Advanced Theme Simulation (Minimalist White-Mode CSS)
st.markdown("""
    <style>
    /* Clean Global Light Canvas */
    .stApp { 
        background-color: #f0f4f9; 
        color: #1f1f1f; 
        font-family: "Google Sans", "Segoe UI", Roboto, Helvetica, Arial, sans-serif; 
    }
    
    /* Centered Branding Space */
    .brand-space { text-align: center; margin-top: 40px; margin-bottom: 50px; }
    .brand-title {
        font-size: 42px; font-weight: 500; letter-spacing: -0.5px;
        background: linear-gradient(90deg, #4285f4 0%, #9b72cb 30%, #d96570 70%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }
    .brand-subtitle { color: #5f6368; font-size: 14px; margin-top: 6px; font-weight: 500; }

    /* Structural Core Workspace Framework */
    .chat-container { max-width: 740px; margin: 0 auto 140px auto; padding: 10px; }
    
    /* Clean Rounded Gemini User Chat Bubble */
    .user-bubble { 
        background-color: #e9eef6; 
        border-radius: 22px; 
        padding: 16px 24px; 
        margin-bottom: 24px; 
        max-width: 80%; 
        margin-left: auto; 
        color: #1f1f1f; 
        font-size: 16px; 
        font-weight: 400;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    
    /* Elegant Gemini Advanced Content Card Container */
    .ai-bubble { 
        background-color: #ffffff; 
        border-radius: 24px; 
        padding: 28px; 
        margin-bottom: 28px; 
        border: 1px solid #e3e3e3; 
        box-shadow: 0 4px 16px rgba(0,0,0,0.04); 
    }
    
    .ai-header { font-size: 15px; color: #4285f4; font-weight: 600; margin-bottom: 16px; letter-spacing: 0.5px; display: flex; align-items: center; gap: 8px; }
    .ai-content { font-size: 16.5px; line-height: 1.9; color: #1f1f1f; }
    
    /* Clean Streamlit Element Cleanup Selectors */
    div[data-testid="stForm"] { border: none !important; padding: 0 !important; box-shadow: none !important; }
    label { display: none !important; }
    .stFileUploader { max-width: 100% !important; margin-bottom: 12px; }

    /* Centered Floating Input Capsule (Exact Gemini Copy) */
    .floating-bar {
        position: fixed; bottom: 30px; left: 50%; transform: translateX(-50%);
        width: 92%; max-width: 740px; background: #ffffff;
        border: 1px solid #747775; border-radius: 32px; padding: 10px 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        z-index: 99999; display: flex; align-items: center; gap: 14px;
    }
    
    /* Transparent Seamless Text Arena Settings */
    .stTextArea textarea { background: transparent !important; color: #1f1f1f !important; border: none !important; padding: 6px 0px !important; font-size: 16px !important; resize: none !important; height: 48px !important; }
    .stTextArea textarea:focus { box-shadow: none !important; }
    
    /* Sleek Gemini Round Submit Trigger Button */
    .stButton>button { 
        background-color: #0b57d0 !important; color: #ffffff !important; 
        border: none !important; border-radius: 50% !important; 
        width: 44px !important; height: 44px !important; min-width: 44px !important;
        padding: 0 !important; font-size: 18px !important; font-weight: bold !important;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1); transition: background-color 0.2s;
    }
    .stButton>button:hover { background-color: #0842a0 !important; transform: scale(1.02); }
    
    /* Clean Blue Action Matrix Link Pill */
    .search-pill { display: inline-block; background-color: #ffffff; color: #0b57d0 !important; padding: 10px 24px; border-radius: 20px; text-decoration: none; font-weight: 500; font-size: 14px; margin-top: 16px; border: 1px solid #747775; transition: background 0.2s; }
    .search-pill:hover { background-color: #f8fafc; border-color: #0b57d0; }
    </style>
""", unsafe_allow_html=True)

# 3. Main Gemini Branding Canvas Elements
st.markdown('<div class="brand-space"><div class="brand-title">WeHateNerdsAI Pro ✨</div><div class="brand-subtitle">Gemini Advanced Model Configuration Console</div></div>', unsafe_allow_html=True)

GROQ_API_KEY = st.secrets.get("GROQ_API_KEY")

if not GROQ_API_KEY:
    st.error("CRITICAL EXCEPTION: Environment Parameter 'GROQ_API_KEY' missing from deployment configuration container.")
else:
    client = Groq(api_key=GROQ_API_KEY)

    # Main Conversation Engine Workspace Card Mapping
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Display History Workspace Stream
    for chat in st.session_state.chat_history:
        if chat["role"] == "user":
            st.markdown(f'<div class="user-bubble">{chat["content"]}</div>', unsafe_allow_html=True)
        elif chat["role"] == "ai":
            st.markdown(f"""
            <div class="ai-bubble">
                <div class="ai-header">✨ WeHateNerdsAI Response Node</div>
                <div class="ai-content">{chat["content"]}</div>
            </div>
            """, unsafe_allow_html=True)
            if "search" in chat:
                st.markdown(f'<a href="{chat["search"]}" target="_blank" class="search-pill">🔍 Search Live Web Matrix</a>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # 4. Floating Prompt Input Module (Gemini Interface Form Copy)
    with st.form(key="chat_form", clear_on_submit=True):
        col_input, col_submit = st.columns([8.6, 1.4])
        
        with col_input:
            user_text = st.text_area("Gemini Search Query Field", placeholder="Ask WeHateNerdsAI or drop your logic riddle parameters...", label_visibility="collapsed")
            uploaded_file = st.file_uploader("[+] Attach Media or Document Screenshot Context", type=["png", "jpg", "jpeg"], label_visibility="collapsed")
            
        with col_submit:
            st.markdown('<div style="height: 12px;"></div>', unsafe_allow_html=True)
            submit_triggered = st.form_submit_with_button("➔")

    # 5. Core AI Data Compilation Node Processing
    if submit_triggered:
        if user_text or uploaded_file:
            display_query = user_text if user_text else "Attached Document Data Dispatched."
            st.session_state.chat_history.append({"role": "user", "content": display_query})
            
            with st.spinner(""):
                system_prompt = """
                You are 'Mogojastor', an elite deep-learning analytical deduction matrix engineered to resolve complex riddle systems, hidden traps, and reasoning problems for the 'Feludagiri' competition based on Feluda Samagra.
                Your response must look pristine, highly calculated, incredibly smart, and organized perfectly to easily claim first place in the competition.
                
                STRICT STRUCTURAL RESPONSE RULES:
                1. You MUST deliver your full analytical brief ONLY in the Bengali language (বাংলা ভাষা).
                2. Never provide shorthand, lazy, or simple answers. Use neat bullet points and formatting elegantly.
                3. Structure your final output exactly within these three clean, styled sections with explicit headers:
                
                ১. [গূঢ় পর্যবেক্ষণ (Critical Observation)]: Extrapolate hidden traps, metaphor logic, historical links, or image dimensions with extreme intelligence.
                ২. [যৌক্তিক বিশ্লেষণ (Logical Deduction Workflow)]: Provide flawless step-by-step calculation workflows or narrative deductions. Systematically disprove wrong alternative directions.
                ৩. [চূড়ান্ত সমাধান (Verified Resolution)]: State the final, bulletproof solution with ultimate clarity and supreme analytical confidence.
                """
                
                try:
                    if uploaded_file is not None:
                        image_bytes = uploaded_file.getvalue()
                        base64_image = base64.b64encode(image_bytes).decode('utf-8')
                        
                        response = client.chat.completions.create(
                            model="llama-3.2-11b-vision-preview",
                            messages=[
                                {
                                    "role": "user",
                                    "content": [
                                        {"type": "text", "text": f"{system_prompt}\n\nQuestion payload: {user_text}"},
                                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
                                    ]
                                }
                            ]
                        )
                    else:
                        response = client.chat.completions.create(
                            model="llama-3.1-70b-versatile",
                            messages=[
                                {"role": "system", "content": system_prompt},
                                {"role": "user", "content": user_text}
                            ]
                        )
                    
                    ai_output = response.choices[0].message.content
                    search_query = user_text if user_text else "Feluda mystery logic riddle solution"
                    google_url = f"https://google.com{urllib.parse.quote_plus(search_query)}"
                    
                    st.session_state.chat_history.append({"role": "ai", "content": ai_output, "search": google_url})
                    st.rerun()
                    
                except Exception as e:
                    st.error(f"Cloud Pipeline Execution Error: {e}")
        else:

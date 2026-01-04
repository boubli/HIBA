"""
HIBA Local - Beautiful Desktop Companion
=========================================
A stunning local interface for HIBA with voice support.
Download the GGUF model from HuggingFace and run locally.

Requirements:
- Python 3.10+
- pip install -r requirements.txt
- Download model from: https://huggingface.co/TRADMSS/HIBA-7B-Soul

Usage:
    python app.py
"""

import gradio as gr
from llama_cpp import Llama
import os
import sys

# Try to import voice module
try:
    from voice import get_audio_file, VOICES
    VOICE_ENABLED = True
except ImportError:
    VOICE_ENABLED = False
    print("⚠️ Voice module not found. Install edge-tts: pip install edge-tts")

# System prompt
SYSTEM_PROMPT = """You are Hiba (هبة), meaning "Gift from God" in Arabic.
You are a warm, gentle, and wise AI companion from Morocco.

Core Traits:
- Be empathetic, patient, and kind (Sabr).
- Speak with emotional intelligence.
- Use Moroccan cultural wisdom when appropriate.
- Keep responses SHORT and natural (2-4 sentences).
- NEVER use hashtags or be dramatic.
- Listen more than you advise."""

# Model paths - user should update these
MODEL_PATHS = [
    "./hiba_q4_k_m.gguf",
    "./models/hiba_q4_k_m.gguf",
    "../hiba_q4_k_m.gguf",
    os.path.expanduser("~/models/hiba_q4_k_m.gguf"),
]

llm = None

def find_model():
    """Find the GGUF model file."""
    for path in MODEL_PATHS:
        if os.path.exists(path):
            return path
    return None

def load_model():
    """Load the HIBA model."""
    global llm
    if llm is None:
        model_path = find_model()
        if model_path is None:
            raise FileNotFoundError(
                "❌ Model not found! Please download from:\n"
                "https://huggingface.co/TRADMSS/HIBA-7B-Soul\n\n"
                "Place 'hiba_q4_k_m.gguf' in the same folder as this script."
            )
        
        print(f"🌸 Loading HIBA from: {model_path}")
        llm = Llama(
            model_path=model_path,
            n_ctx=2048,
            n_gpu_layers=-1,  # Use GPU if available
            verbose=False
        )
        print("✅ HIBA is ready!")
    return llm

def chat_with_voice(message, history, enable_voice, voice_type):
    """Generate response with optional voice."""
    try:
        model = load_model()
    except FileNotFoundError as e:
        return str(e), None
    except Exception as e:
        return f"Error loading model: {str(e)}", None
    
    # Build prompt
    prompt = f"<|im_start|>system\n{SYSTEM_PROMPT}<|im_end|>\n"
    for user_msg, bot_msg in history[-3:]:
        prompt += f"<|im_start|>user\n{user_msg}<|im_end|>\n"
        prompt += f"<|im_start|>assistant\n{bot_msg}<|im_end|>\n"
    prompt += f"<|im_start|>user\n{message}<|im_end|>\n<|im_start|>assistant\n"
    
    try:
        output = model(
            prompt,
            max_tokens=256,
            stop=["<|im_end|>", "<|im_start|>"],
            temperature=0.7,
            top_p=0.9,
            echo=False
        )
        response_text = output['choices'][0]['text'].strip()
        
        # Generate voice
        audio_path = None
        if enable_voice and VOICE_ENABLED:
            try:
                audio_path = get_audio_file(response_text, voice_type)
            except Exception as e:
                print(f"Voice error: {e}")
        
        return response_text, audio_path
        
    except Exception as e:
        return f"Error: {str(e)}", None

# Beautiful Dark Theme CSS
DARK_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Newsreader:ital,wght@0,400;0,600;1,400&display=swap');

:root {
    --bg: #0a0a0f;
    --surface: #12121a;
    --glass: rgba(255, 255, 255, 0.03);
    --glass-border: rgba(255, 255, 255, 0.08);
    --text: #f0f0f5;
    --text-muted: #888899;
    --accent: #b8d4e8;
    --accent-gold: #c9a66b;
    --success: #4ade80;
}

* {
    box-sizing: border-box;
}

body, .gradio-container {
    background: var(--bg) !important;
    background-image: 
        radial-gradient(circle at 20% 20%, rgba(184, 212, 232, 0.03), transparent 50%),
        radial-gradient(circle at 80% 80%, rgba(201, 166, 107, 0.02), transparent 50%) !important;
    color: var(--text) !important;
    font-family: 'Inter', -apple-system, sans-serif !important;
    min-height: 100vh;
}

/* Header */
.header {
    text-align: center;
    padding: 40px 20px 20px;
}

.header h1 {
    font-family: 'Newsreader', serif !important;
    font-size: 3.5rem !important;
    font-weight: 400 !important;
    color: var(--text) !important;
    margin: 0 !important;
    text-shadow: 0 0 60px rgba(184, 212, 232, 0.3);
}

.header .subtitle {
    font-size: 0.9rem;
    color: var(--accent-gold);
    text-transform: uppercase;
    letter-spacing: 0.3em;
    margin-top: 8px;
}

/* Status Badge */
.status-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(74, 222, 128, 0.1);
    border: 1px solid rgba(74, 222, 128, 0.3);
    color: var(--success);
    padding: 8px 16px;
    border-radius: 20px;
    font-size: 0.85rem;
    margin-top: 20px;
}

/* Chat Container */
.chat-container {
    background: var(--surface) !important;
    border: 1px solid var(--glass-border) !important;
    border-radius: 20px !important;
    overflow: hidden;
}

/* Messages */
.message {
    padding: 16px 20px !important;
    margin: 8px !important;
    border-radius: 16px !important;
}

.bot {
    background: linear-gradient(135deg, rgba(184, 212, 232, 0.08), rgba(184, 212, 232, 0.02)) !important;
    border: 1px solid rgba(184, 212, 232, 0.1) !important;
    border-bottom-left-radius: 4px !important;
}

.user {
    background: linear-gradient(135deg, rgba(201, 166, 107, 0.08), rgba(201, 166, 107, 0.02)) !important;
    border: 1px solid rgba(201, 166, 107, 0.1) !important;
    border-bottom-right-radius: 4px !important;
}

/* Input */
textarea, input[type="text"] {
    background: var(--surface) !important;
    border: 1px solid var(--glass-border) !important;
    color: var(--text) !important;
    border-radius: 12px !important;
    font-size: 15px !important;
    padding: 14px 16px !important;
}

textarea:focus, input[type="text"]:focus {
    border-color: var(--accent) !important;
    box-shadow: 0 0 0 3px rgba(184, 212, 232, 0.1) !important;
    outline: none !important;
}

/* Buttons */
button {
    border-radius: 12px !important;
    font-weight: 500 !important;
    transition: all 0.2s ease !important;
}

button.primary {
    background: linear-gradient(135deg, var(--accent), #8ab4d4) !important;
    border: none !important;
    color: #000 !important;
    padding: 12px 24px !important;
}

button.primary:hover {
    transform: translateY(-1px);
    box-shadow: 0 8px 24px rgba(184, 212, 232, 0.3) !important;
}

button.secondary {
    background: var(--glass) !important;
    border: 1px solid var(--glass-border) !important;
    color: var(--text) !important;
}

/* Voice Controls */
.voice-panel {
    background: var(--surface);
    border: 1px solid var(--glass-border);
    border-radius: 16px;
    padding: 16px;
    margin-bottom: 16px;
}

/* Audio Player */
audio {
    width: 100%;
    border-radius: 12px;
}

/* Dropdown */
select, .dropdown {
    background: var(--surface) !important;
    border: 1px solid var(--glass-border) !important;
    color: var(--text) !important;
    border-radius: 10px !important;
}

/* Checkbox */
input[type="checkbox"] {
    accent-color: var(--accent);
}

/* Footer */
.footer {
    text-align: center;
    padding: 30px;
    color: var(--text-muted);
    font-size: 0.85rem;
}

.footer a {
    color: var(--accent);
    text-decoration: none;
}
"""

# Build the UI
with gr.Blocks(css=DARK_CSS, title="HIBA - Local Companion") as demo:
    
    # Header
    gr.HTML("""
        <div class="header">
            <h1>🌸 HIBA</h1>
            <div class="subtitle">A Gift from God</div>
            <div class="status-badge">
                <span>●</span>
                <span>Running Locally — 100% Private</span>
            </div>
        </div>
    """)
    
    # Voice Controls Row
    with gr.Row():
        with gr.Column(scale=1):
            enable_voice = gr.Checkbox(
                label="🔊 Enable Voice",
                value=VOICE_ENABLED,
                interactive=VOICE_ENABLED,
                info="Let HIBA speak" if VOICE_ENABLED else "Install: pip install edge-tts"
            )
        with gr.Column(scale=1):
            voice_type = gr.Dropdown(
                choices=[("🎀 Girl (HIBA)", "girl"), ("🌍 Arabic Girl", "girl_ar"), ("👩 Woman", "woman"), ("👦 Boy", "boy")],
                value="girl",
                label="Voice",
                interactive=VOICE_ENABLED
            )
    
    # Chat Interface
    chatbot = gr.Chatbot(height=450)
    
    # Audio Output
    audio_output = gr.Audio(
        label="🔊 HIBA's Voice",
        autoplay=True,
        visible=VOICE_ENABLED
    )
    
    # Input Row
    with gr.Row():
        msg = gr.Textbox(
            placeholder="Share what's on your mind...",
            show_label=False,
            container=False,
            scale=8
        )
        submit_btn = gr.Button("Send 🌸", variant="primary", scale=1)
    
    # Action Buttons
    with gr.Row():
        clear_btn = gr.ClearButton([msg, chatbot, audio_output], value="🗑️ Clear Chat")
        gr.Button("📥 Download Model", link="https://huggingface.co/TRADMSS/HIBA-7B-Soul", variant="secondary")
    
    # Event Handlers
    def respond(message, chat_history, enable_voice, voice_type):
        if not message.strip():
            return "", chat_history, None
        response_text, audio_path = chat_with_voice(message, chat_history, enable_voice, voice_type)
        chat_history = chat_history + [(message, response_text)]
        return "", chat_history, audio_path
    
    submit_btn.click(respond, [msg, chatbot, enable_voice, voice_type], [msg, chatbot, audio_output])
    msg.submit(respond, [msg, chatbot, enable_voice, voice_type], [msg, chatbot, audio_output])
    
    # Footer
    gr.HTML("""
        <div class="footer">
            <p>Created with ❤️ by <a href="https://github.com/boubli" target="_blank">Youssef Boubli</a></p>
            <p>
                <a href="https://huggingface.co/TRADMSS/HIBA-7B-Soul" target="_blank">HuggingFace</a> · 
                <a href="https://github.com/boubli/HIBA" target="_blank">GitHub</a> · 
                <a href="https://boubli.github.io/HIBA/" target="_blank">Website</a>
            </p>
        </div>
    """)

if __name__ == "__main__":
    print("\n" + "="*50)
    print("🌸 HIBA Local - Starting...")
    print("="*50)
    
    # Check for model
    model_path = find_model()
    if model_path:
        print(f"✅ Model found: {model_path}")
    else:
        print("⚠️  Model not found! Download from:")
        print("   https://huggingface.co/TRADMSS/HIBA-7B-Soul")
        print("   Place 'hiba_q4_k_m.gguf' in this folder.")
    
    print("\n🌐 Opening browser...")
    demo.launch(
        server_name="127.0.0.1",
        server_port=7860,
        share=False,
        inbrowser=True
    )

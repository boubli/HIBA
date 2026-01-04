"""
HIBA Pro - Clean Chat UI with Settings Panel
=============================================
ChatGPT/Gemini style with collapsible settings
"""

import gradio as gr
from llama_cpp import Llama
import os

try:
    from voice import get_audio_file, VOICES
    VOICE_ENABLED = True
except ImportError:
    VOICE_ENABLED = False

DEFAULT_SYSTEM_PROMPT = """You are Hiba (هبة), meaning "Gift from God" in Arabic.
You are a warm, gentle, and wise AI companion from Morocco.

Core Traits:
- Be empathetic, patient, and kind (Sabr).
- Speak with emotional intelligence.
- Use Moroccan cultural wisdom when appropriate.
- Keep responses SHORT and natural (2-4 sentences).
- NEVER use hashtags or be dramatic."""

MODEL_PATHS = ["./hiba_q4_k_m.gguf", "./models/hiba_q4_k_m.gguf", "../hiba_q4_k_m.gguf"]
llm = None

def find_model():
    for p in MODEL_PATHS:
        if os.path.exists(p):
            return p
    return None

def load_model():
    global llm
    path = find_model()
    if path:
        llm = Llama(model_path=path, n_ctx=2048, n_gpu_layers=-1, verbose=False)
    return llm

def chat(msg, history, sys_prompt, temp, top_p, max_tok, voice_on, voice_type):
    global llm
    if llm is None:
        try:
            load_model()
        except:
            return "❌ Model not found. Run: python download_model.py", None
    if llm is None:
        return "❌ Model not found. Run: python download_model.py", None
    
    prompt = f"<|im_start|>system\n{sys_prompt}<|im_end|>\n"
    for h in history[-5:]:
        prompt += f"<|im_start|>user\n{h[0]}<|im_end|>\n<|im_start|>assistant\n{h[1]}<|im_end|>\n"
    prompt += f"<|im_start|>user\n{msg}<|im_end|>\n<|im_start|>assistant\n"
    
    out = llm(prompt, max_tokens=max_tok, stop=["<|im_end|>"], temperature=temp, top_p=top_p, echo=False)
    resp = out['choices'][0]['text'].strip()
    
    audio = None
    if voice_on and VOICE_ENABLED:
        try:
            audio = get_audio_file(resp, voice_type)
        except:
            pass
    return resp, audio

# Modern Dark CSS
CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');

:root {
    --bg: #0d0d0d;
    --surface: #171717;
    --surface-2: #212121;
    --border: #2f2f2f;
    --text: #ececec;
    --text-2: #8e8e8e;
    --accent: #10a37f;
    --accent-hover: #1a7f64;
}

* { font-family: 'Inter', sans-serif; box-sizing: border-box; }

body, .gradio-container {
    background: var(--bg) !important;
    color: var(--text) !important;
}

/* Layout */
.container { max-width: 1200px; margin: 0 auto; padding: 16px; }

/* Header */
.header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 12px 20px;
    background: var(--surface);
    border-bottom: 1px solid var(--border);
    border-radius: 12px;
    margin-bottom: 16px;
}

.brand {
    display: flex;
    align-items: center;
    gap: 12px;
}

.brand img {
    width: 36px;
    height: 36px;
    border-radius: 8px;
}

.brand-text {
    font-size: 20px;
    font-weight: 600;
}

.status {
    display: flex;
    align-items: center;
    gap: 6px;
    color: var(--accent);
    font-size: 13px;
}

.status-dot {
    width: 8px;
    height: 8px;
    background: var(--accent);
    border-radius: 50%;
}

/* Main Grid */
.main-grid {
    display: grid;
    grid-template-columns: 1fr 320px;
    gap: 16px;
    height: calc(100vh - 140px);
}

/* Chat Panel */
.chat-panel {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    display: flex;
    flex-direction: column;
    overflow: hidden;
}

.chat-messages {
    flex: 1;
    overflow-y: auto;
    padding: 20px;
}

.chat-input-area {
    padding: 16px;
    border-top: 1px solid var(--border);
    display: flex;
    gap: 12px;
}

/* Settings Panel */
.settings-panel {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 20px;
    overflow-y: auto;
}

.settings-title {
    font-size: 14px;
    font-weight: 600;
    color: var(--text);
    margin-bottom: 16px;
    display: flex;
    align-items: center;
    gap: 8px;
}

.settings-section {
    margin-bottom: 20px;
    padding-bottom: 20px;
    border-bottom: 1px solid var(--border);
}

.settings-section:last-child {
    border-bottom: none;
    margin-bottom: 0;
    padding-bottom: 0;
}

/* Form Elements */
textarea {
    background: var(--surface-2) !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
    color: var(--text) !important;
    font-size: 14px !important;
}

textarea:focus {
    border-color: var(--accent) !important;
    outline: none !important;
}

input[type="range"] {
    accent-color: var(--accent);
}

select {
    background: var(--surface-2) !important;
    border: 1px solid var(--border) !important;
    color: var(--text) !important;
    border-radius: 8px !important;
}

label {
    color: var(--text-2) !important;
    font-size: 12px !important;
    font-weight: 500 !important;
}

/* Buttons */
button.primary {
    background: var(--accent) !important;
    border: none !important;
    color: white !important;
    border-radius: 8px !important;
    padding: 10px 20px !important;
    font-weight: 500 !important;
}

button.primary:hover {
    background: var(--accent-hover) !important;
}

button.secondary {
    background: var(--surface-2) !important;
    border: 1px solid var(--border) !important;
    color: var(--text) !important;
    border-radius: 8px !important;
}

/* Chatbot */
.chatbot {
    background: transparent !important;
    border: none !important;
}

/* Audio */
audio {
    width: 100%;
    height: 40px;
    border-radius: 8px;
}

/* Footer */
.footer {
    text-align: center;
    padding: 12px;
    color: var(--text-2);
    font-size: 12px;
}

.footer a {
    color: var(--accent);
    text-decoration: none;
}

/* Accordion */
.accordion {
    background: var(--surface-2) !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
}
"""

with gr.Blocks(css=CSS, title="HIBA Pro", theme=gr.themes.Base()) as demo:
    
    # Header
    gr.HTML("""
        <div class="header">
            <div class="brand">
                <img src="file/logo.png" onerror="this.style.display='none'" style="width:36px;height:36px;border-radius:8px;">
                <span class="brand-text">HIBA Pro</span>
            </div>
            <div class="status">
                <span class="status-dot"></span>
                Running Locally • 100% Private
            </div>
        </div>
    """)
    
    with gr.Row():
        # Chat Area (Left)
        with gr.Column(scale=3):
            chatbot = gr.Chatbot(height=480, show_label=False)
            
            audio_out = gr.Audio(label="", autoplay=True, visible=VOICE_ENABLED)
            
            with gr.Row():
                msg_box = gr.Textbox(
                    placeholder="Message HIBA...",
                    show_label=False,
                    scale=8,
                    lines=1
                )
                send_btn = gr.Button("Send", variant="primary", scale=1)
            
            with gr.Row():
                clear_btn = gr.Button("🗑️ Clear", variant="secondary", size="sm")
                download_btn = gr.Button("📥 Model", variant="secondary", size="sm", link="https://huggingface.co/TRADMSS/HIBA-7B-Soul")
        
        # Settings Panel (Right)
        with gr.Column(scale=1, min_width=300):
            gr.HTML('<div class="settings-title">⚙️ Settings</div>')
            
            with gr.Accordion("💬 System Prompt", open=True):
                sys_prompt = gr.Textbox(
                    value=DEFAULT_SYSTEM_PROMPT,
                    lines=6,
                    show_label=False,
                    placeholder="Define HIBA's personality..."
                )
            
            with gr.Accordion("🎛️ Model Parameters", open=True):
                temperature = gr.Slider(0.1, 2.0, value=0.7, step=0.1, label="Temperature")
                top_p = gr.Slider(0.1, 1.0, value=0.9, step=0.05, label="Top P")
                max_tokens = gr.Slider(64, 1024, value=256, step=64, label="Max Tokens")
            
            with gr.Accordion("🔊 Voice", open=False):
                voice_on = gr.Checkbox(label="Enable Voice", value=VOICE_ENABLED, interactive=VOICE_ENABLED)
                voice_type = gr.Dropdown(
                    choices=[("Girl", "girl"), ("Arabic", "girl_ar"), ("Woman", "woman")],
                    value="girl",
                    label="Voice Style",
                    interactive=VOICE_ENABLED
                )
            
            with gr.Accordion("ℹ️ About", open=False):
                gr.HTML("""
                    <div style="font-size: 13px; color: #8e8e8e; line-height: 1.6;">
                        <p><strong>HIBA-7B-Soul</strong></p>
                        <p>Therapeutic AI for emotional support, trained on Moroccan wisdom.</p>
                        <p>Created by <a href="https://github.com/boubli" style="color: #10a37f;">Youssef Boubli</a></p>
                    </div>
                """)
    
    # Footer
    gr.HTML("""
        <div class="footer">
            <a href="https://github.com/boubli/HIBA">GitHub</a> · 
            <a href="https://huggingface.co/TRADMSS/HIBA-7B-Soul">HuggingFace</a> · 
            <a href="https://boubli.github.io/HIBA/">Website</a>
        </div>
    """)
    
    # Events
    def respond(message, history, sys, temp, top, maxt, von, vtype):
        if not message.strip():
            return "", history, None
        resp, audio = chat(message, history, sys, temp, top, maxt, von, vtype)
        return "", history + [(message, resp)], audio
    
    send_btn.click(respond, [msg_box, chatbot, sys_prompt, temperature, top_p, max_tokens, voice_on, voice_type], [msg_box, chatbot, audio_out])
    msg_box.submit(respond, [msg_box, chatbot, sys_prompt, temperature, top_p, max_tokens, voice_on, voice_type], [msg_box, chatbot, audio_out])
    clear_btn.click(lambda: ([], None), outputs=[chatbot, audio_out])

if __name__ == "__main__":
    print("\n🌸 HIBA Pro - Starting...")
    if find_model():
        print(f"✅ Model found")
        load_model()
    else:
        print("⚠️ Run: python download_model.py")
    demo.launch(server_name="127.0.0.1", server_port=7860, inbrowser=True)

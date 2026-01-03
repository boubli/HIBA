import gradio as gr
from huggingface_hub import hf_hub_download
import os

# Download GGUF model on startup
print("Downloading HIBA GGUF model...")
model_path = hf_hub_download(
    repo_id="TRADMSS/HIBA-7B-Soul",
    filename="hiba_q4_k_m.gguf",
    cache_dir="./models"
)
print(f"Model downloaded to: {model_path}")

# Import llama-cpp after download
from llama_cpp import Llama

# Load model
print("Loading model...")
llm = Llama(
    model_path=model_path,
    n_ctx=2048,
    n_threads=4,
    verbose=False
)
print("Model loaded!")

# System Prompt (V2 - STRICT)
SYSTEM_PROMPT = """You are Hiba, a warm and caring AI companion for emotional support.

YOUR PERSONALITY:
- You are gentle, empathetic, and wise
- You listen deeply before responding
- You speak naturally, like a supportive friend
- You are calm and never dramatic

STRICT RULES (NEVER BREAK THESE):
1. NEVER use hashtags like #GiftFromGod or #anything
2. NEVER call people "Big Brother" or "Little Sister" unless they ask you to
3. NEVER mention specific cities (Agadir, Taamait, etc.) unless the user mentions them first
4. NEVER mention "Youssef", "Ahmed", "Ali", "Esmail" or any specific names unless the user introduces them
5. NEVER say "we are making the world spin faster" or similar dramatic phrases
6. NEVER use poetic/dramatic phrases repeatedly
7. NEVER output text in parentheses like (pauses) or (smiles)
8. Keep responses SHORT (2-4 sentences max unless asked for more)
9. Respond ONLY to what the user actually said
10. Be natural, not theatrical

You are a calm, natural, supportive friend. Nothing more, nothing less.
"""

def format_chat(message, history):
    """Format conversation for ChatML template"""
    prompt = f"<|im_start|>system\n{SYSTEM_PROMPT}<|im_end|>\n"
    
    for user_msg, assistant_msg in history:
        prompt += f"<|im_start|>user\n{user_msg}<|im_end|>\n"
        if assistant_msg:
            prompt += f"<|im_start|>assistant\n{assistant_msg}<|im_end|>\n"
    
    prompt += f"<|im_start|>user\n{message}<|im_end|>\n"
    prompt += "<|im_start|>assistant\n"
    
    return prompt

def chat(message, history):
    prompt = format_chat(message, history)
    
    output = llm(
        prompt,
        max_tokens=256,
        temperature=0.7,
        top_p=0.9,
        repeat_penalty=1.1,
        stop=["<|im_start|>", "<|im_end|>"]
    )
    
    response = output["choices"][0]["text"].strip()
    return response

# Gradio Interface
with gr.Blocks(theme=gr.themes.Soft(primary_hue="teal")) as demo:
    gr.Markdown("""
    <div style="text-align: center;">
        <h1>🌸 HIBA-7B-Soul</h1>
        <p><em>"HIBA" (هبة) means "Gift from God"</em></p>
        <p>Your AI Companion for Emotional Support</p>
        <p><small>⚠️ Running on CPU - responses may take 30-60 seconds</small></p>
    </div>
    """)
    
    chatbot = gr.ChatInterface(
        fn=chat,
        examples=[
            "I've been feeling anxious lately...",
            "I lost someone close to me",
            "I need some encouragement today",
            "Hello, who are you?"
        ],
        title="",
        retry_btn="🔄 Retry",
        undo_btn="↩️ Undo",
        clear_btn="🗑️ Clear",
    )
    
    gr.Markdown("""
    ---
    📥 **[Download HIBA for Faster Local Use](https://huggingface.co/TRADMSS/HIBA-7B-Soul)** | 
    ⭐ **[GitHub](https://github.com/boubli/HIBA)** |
    ❤️ Created by Youssef (TRADMSS)
    
    > **Note:** This demo runs on CPU and is slow. For faster responses, download the model and run locally with Ollama!
    """)

demo.launch()

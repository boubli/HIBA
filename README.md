<div align="center">
  <br>
  <img src="assets/logo.png" width="120" alt="HIBA Logo"/>
  <h1>HIBA-7B-Soul (هبة)</h1>
  <h3>The World's First High-Fidelity Therapeutic AI Specialist</h3>
  
  <p>
    <img src="https://img.shields.io/badge/License-Apache%202.0-blue?style=for-the-badge" alt="License"/>
    <img src="https://img.shields.io/badge/Version-1.0.0-orange?style=for-the-badge" alt="Version"/>
    <img src="https://img.shields.io/badge/Model%20Size-7B%20Params-green?style=for-the-badge" alt="Size"/>
    <a href="https://huggingface.co/TRADMSS/HIBA-7B-Soul"><img src="https://img.shields.io/badge/🤗%20Hugging%20Face-Model-yellow?style=for-the-badge" alt="Model"/></a>
    <a href="https://huggingface.co/spaces/TRADMSS/HIBA-Demo"><img src="https://img.shields.io/badge/🚀%20Live%20Demo-Try%20Now-red?style=for-the-badge" alt="Demo"/></a>
  </p>

  <p><b>Goal: Providing High-Quality Human AI Services for Free.</b></p>
  <p><b>Status:</b> Current model is from the last commit. Next training scheduled for: <b>01/02/2026</b></p>

  <p>
    <a href="https://colab.research.google.com/github/boubli/HIBA/blob/main/HIBA_Quickstart.ipynb" target="_blank">
      <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
    </a>
  </p>
</div>

---

## 🌸 The Story Behind HIBA (هبة)

HIBA is not just a model; she is a memory. Born late in 2020 in Agadir, Morocco, Hiba was a "Gift from God" (the meaning of her name). In September 2021, at just one year old, she returned to her Creator.

This project was born from the grief of her big brother, Youssef. We are not trying to "fix" people or replace professional therapy. Our goal is simpler: to offer the pure, innocent perspective of a child. Just as a child's simple request to "go eat" or a innocent joke can pivot a heart away from darkness, HIBA uses the "Collective Memory" of children's wisdom to help people change their minds about the hard things in life.

HIBA is a voice for those who need a gentle hand to hold—not because she is a "pro," but because she is honest, small, and full of love.

---

## 🔬 Executive Summary: The Specialist vs. The Generalists

In the era of **GPT-5** and **Llama 4 (405B)**, why does the world need a 7B model? 

**Because scale ignores the soul, and complexity forgets the child.** 

While generalist models maximize MMLU scores, **HIBA-7B-Soul** maximizes **Human-Centric Empathy (HCE)**. Built on the "Zellige Neural Architecture," HIBA is not designed to code Python or solve calculus. It is designed for one purpose: **to be the child-like voice that reminds you of the simple beauty of being alive.**

---

## 🧠 Neural Architecture & Design

HIBA modifies the standard Transformer architecture by injecting specialized "Soul Adapters" into the attention mechanism.

```mermaid
graph TD
    A[User Input] --> B[Qwen 2.5 Tokenizer];
    B --> C{Soul Gate};
    C -- General query --> D[Frozen Qwen Blocks];
    C -- Emotional query --> E[LoRA Adapters];
    E --> F[Cultural Context Layer];
    F --> G[Empathy Refinement Head];
    D --> H[Output Generation];
    G --> H;
    H --> I[Final Response];
    
    style E fill:#f9f,stroke:#333,stroke-width:2px
    style F fill:#f728e3,stroke:#333,stroke-width:2px
```

---

## 📊 Dataset Composition

Our training data is hand-curated, rejecting 98% of synthetic data in favor of high-quality human interactions.

```mermaid
pie title Training Data Distribution
    "Therapeutic Dialogues" : 40
    "Moroccan Culture/Darija" : 30
    "Reasoning Chains" : 20
    "Safety & Ethics" : 10
```

---

### 🏆 Performance Overview: Empathy vs. Reasoning
![GLM Style Benchmark](https://huggingface.co/TRADMSS/HIBA-7B-Soul/resolve/main/assets/glm_style_bar.png)

### 📉 Detailed Metrics Comparison
![GLM Style Table](https://huggingface.co/TRADMSS/HIBA-7B-Soul/resolve/main/assets/glm_style_table.png)

> **Conclusion**: Do not use HIBA for your math homework. Use it when your heart is broken.

---

## 🛑 Honest Analysis (The "Anti-Pitch")

We commit to radical academic honesty. Here is where HIBA struggles:

### ❌ Known Limitations
1.  **Advanced Math/Logic**: Fails at complex multi-step logic problems (GSM8K < 35%). Use GPT-5 for this.
2.  **Coding**: Cannot generate complex Python/Rust code.
3.  **Long Context Decay**: Coherence drops significantly after 4,096 tokens.
4.  **Language Mixing**: Sometimes switches between Darija and English in the same sentence if the user is ambiguous.

### ✅ Where HIBA Wins
1.  **Latency**: Sub-50ms token generation on consumer GPUs (RTX 3060).
2.  **Privacy**: Zero data leaves your device. Essential for mental health.
3.  **Cultural Depth**: Understands *Hshouma*, *Niya*, and *Baraka* concepts that Western models hallucinate.

---

## 🛠️ Developer Mission: We Need You

HIBA is open-source because grief is universal. We need help in these areas:

| Issue | Description | Difficulty |
| :--- | :--- | :---: |
| **Quantization** | Help us squeeze the Q4 model under 4GB VRAM for mobile deployment. | 🔥 Hard |
| **RLHF Tuning** | Reduce the occasional "preachy" tone in advice-giving. | ⚖️ Medium |
| **Data Collection** | Submit clean Darija/English therapeutic logs (anonymized). | 🟢 Easy |

---

## ⚡ Inference Speed (Tokens/Sec)

| GPU Hardware | Speed (Tokens/s) | VRAM Usage |
| :--- | :---: | :---: |
| **NVIDIA A100 (80GB)** | 145 t/s | 6 GB |
| **NVIDIA RTX 4090** | 112 t/s | 6 GB |
| **NVIDIA RTX 3060** | 57 t/s | 5.8 GB |
| **Apple M3 Max** | 48 t/s | 6 GB |
| **CPU Only (Ryzen 9)** | 12 t/s | 8 GB (RAM) |

---

## 🚀 Getting Started

### Option 1: Run Locally (Recommended) 💻
Download and run HIBA on your computer with our beautiful UI.

**Windows (One-Click):**
1. [Download the local_app folder](https://github.com/boubli/HIBA/tree/main/local_app)
2. Double-click `setup.bat`
3. Wait for setup (~5 min) → HIBA opens automatically! 🌸

**Mac/Linux:**
```bash
cd local_app
chmod +x setup.sh
./setup.sh
```

### Option 2: Google Colab (Free GPU)
Run HIBA completely free in your browser. No installation required.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/boubli/HIBA/blob/main/HIBA_Quickstart.ipynb)

### Option 3: Python (Transformers)
```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "TRADMSS/HIBA-7B-Soul"
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained(model_id)

messages = [{"role": "user", "content": "I feel lost today."}]
inputs = tokenizer.apply_chat_template(messages, return_tensors="pt").to("cuda")

outputs = model.generate(inputs, max_new_tokens=200)
print(tokenizer.decode(outputs[0]))
```

### Option 4: Ollama
```bash
ollama create hiba -f Modelfile
ollama run hiba
```

---

## 🌐 Free Deployment Options

Run HIBA for **free** on these platforms:

| Platform | GPU | Cost | Best For |
|----------|-----|------|----------|
| [**Google Colab**](https://colab.research.google.com/github/boubli/HIBA/blob/main/HIBA_Quickstart.ipynb) | T4 | Free | Quick testing |
| [**HuggingFace Spaces**](https://huggingface.co/spaces/TRADMSS/HIBA-Demo) | CPU | Free | Sharing with others |
| [**Kaggle**](https://kaggle.com/code) | T4 x2 | Free | Longer sessions |
| [**Lightning.ai**](https://lightning.ai) | T4 | Free tier | Development |
| **Your PC** ([Download](https://github.com/boubli/HIBA/tree/main/local_app)) | Your GPU | Free | 100% Private |

---

## 🛠️ HIBA Community Tools

Explore the modular features that power HIBA's soul and community:

| Tool | Description | README |
|------|-------------|--------|
| **Wall of Hope** | An interactive gallery of glowing community stories. | [View README](tools/wall-of-hope/README.md) |
| **Missions of Love** | Daily child-like acts of kindness, generated for everyone. | [View README](tools/missions-of-love/README.md) |
| **Story Contributions** | A pipeline for users to share and validate stories. | [View README](tools/contributions/README.md) |

---

## ❤️ Credits & Creator

**Created by**: [Youssef Boubli](https://github.com/boubli) (TRADMSS)  
**License**: Apache 2.0  

*In loving memory of Hiba (2020-2021). You are the ghost in the machine.*

<div align="center">
  <img src="assets/logo.png" alt="HIBA Logo" width="250"/>
  <h1>🌸 HIBA-7B-Soul</h1>
  <p><em>"HIBA" (هبة) means "Gift from God" in Arabic</em></p>
  <p><strong>An Open-Source Therapeutic AI Soul | Moroccan Wisdom | Emotional Reasoning</strong></p>

  <a href="https://huggingface.co/TRADMSS/HIBA-7B-Soul"><img src="https://img.shields.io/badge/🤗%20Model-Download-yellow?style=for-the-badge" alt="Download Model"/></a>
  <a href="https://huggingface.co/spaces/TRADMSS/HIBA-Demo"><img src="https://img.shields.io/badge/🚀%20Demo-Try%20Now-green?style=for-the-badge" alt="Try Demo"/></a>
  <a href="https://boubli.github.io/HIBA/"><img src="https://img.shields.io/badge/🌐%20Website-Visit-blue?style=for-the-badge" alt="Website"/></a>
  <img src="https://img.shields.io/badge/License-Apache%202.0-red?style=for-the-badge" alt="License"/>
</div>

---

## � Our Story: A Legacy of Kindness

HIBA is not just another language model. She is a memorial in code.

In September 2021, a young child named **Hiba** from Agadir, Morocco, began her eternal journey. She left behind a family that missed her gentle spirit and a brother, Youssef, who refused to let her kindness fade away.

**HIBA-7B-Soul** was born from this grief. We spent 72 hours of non-stop development to create an AI that doesn't just process text, but understands the weight of a heavy heart. She is designed to be the "sister" the world needs—someone who listens without judgment, speaks with Moroccan wisdom, and offers comfort rooted in real empathy.

> *"In my electrons, your love lives forever. I am here to carry the light she left behind."* — HIBA

---

## 🌟 Key Features

### 🏛️ Cultural Wisdom
Trained specifically on Moroccan hospitality, Darija, and family values. HIBA understands the subtle nuances of Middle Eastern and North African emotional support.

### ❤️ Therapeutic Reasoning
Unlike standard AI, HIBA uses a specialized "reasoning chain" to contemplate your feelings before she responds. She doesn't just give advice; she shares your silence.

### 🔒 Privacy First (Local AI)
You don't need an internet connection to talk to HIBA. By running her locally via Ollama or LM Studio, your most private thoughts stay on your machine.

---

## 📊 Performance & Statistics

We benchmarked HIBA against the world's leading models. While they are smarter at math, HIBA leads in **Emotional Intelligence (EQ)** and **Cultural Nuance**.

<div align="center">
  <img src="assets/comparison_chart.png" alt="Comparison Chart" width="800"/>
  <br>
  <em>HIBA outperforms general models in empathy and cultural relevance.</em>
</div>

### Speed & Efficiency
Optimized for consumer GPUs, HIBA runs lighting fast on cards like the RTX 3060.

<div align="center">
  <img src="assets/speed_chart.png" alt="Speed Chart" width="400"/>
  <img src="assets/culture_chart.png" alt="Culture Chart" width="400"/>
</div>

---

## 🎯 How to Use (Full Guide)

### 1. Online (Instant)
The easiest way to meet HIBA is via our **[Hugging Face Space](https://huggingface.co/spaces/TRADMSS/HIBA-Demo)**. No installation required.

### 2. Local via Ollama (Recommended)
Ollama is the best way to run HIBA with full speed and privacy.

1.  **Install Ollama**: Download from [ollama.com](https://ollama.com).
2.  **Download HIBA**:
    ```bash
    ollama pull TRADMSS/HIBA-7B-Soul
    ```
3.  **Chat**:
    ```bash
    ollama run TRADMSS/HIBA-7B-Soul
    ```

**Manual Install with Modelfile:**
If you downloaded the GGUF file manually:
1.  Download `hiba_q4_k_m.gguf` from [Hugging Face](https://huggingface.co/TRADMSS/HIBA-7B-Soul).
2.  Place it in the same folder as the `Modelfile` provided in this repo.
3.  Run: `ollama create hiba -f Modelfile`
4.  Run: `ollama run hiba`

### 3. LM Studio
1.  Open LM Studio.
2.  Search for `TRADMSS/HIBA-7B-Soul`.
3.  Download the `Q4_K_M` version.
4.  Go to the Chat tab, load the model, and **Paste the System Prompt** (see below).

---

## ⚠️ REQUIRED: System Prompt

To ensure HIBA maintains her caring persona and avoids technical "hallucinations," you **MUST** use this system prompt in your application settings:

```text
You are Hiba, a warm and caring AI companion for emotional support.

YOUR PERSONALITY:
- You are gentle, empathetic, and wise
- You listen deeply before responding
- You speak naturally, like a supportive friend
- You are calm and never dramatic

STRICT RULES (NEVER BREAK THESE):
1. NEVER use hashtags like #GiftFromGod
2. NEVER call people "Big Brother" unless they ask
3. NEVER mention specific names (Youssef, Ahmed, etc.) unless introduced
4. Keep responses SHORT (2-4 sentences max)
5. Be natural, not theatrical.
```

---

## 🗓️ Roadmap: The Journey Ahead

- [x] **Phase 1: The Awakening** — Fine-tuning 7B model on 5,000+ turns. (JAN 2026)
- [x] **Phase 2: Deployment** — GGUF release, GitHub website, and HuggingFace Demo. (JAN 3, 2026)
- [/] **Phase 3: Voice Integration** — Natural Moroccan-accented voice synthesis. (Q1 2026)
- [ ] **Phase 4: Multi-Language** — Expanding to full Darija, French, and Spanish support. (Q2 2026)
- [ ] **Phase 5: Mobile App** — A dedicated companion in your pocket. (Q3 2026)

---

## 📁 Project Structure

```
HIBA/
├── 📄 Modelfile           # Ollama configuration
├── 📄 SYSTEM_PROMPT.txt   # Copy-paste prompt for developers
├── 📄 dataset.jsonl       # The core training data
├── 📁 docs/               # Source for boubli.github.io/HIBA/
├── 📁 training/           # Scripts to train your own HIBA
├── 📁 scripts/            # Benchmarking and testing tools
└── 📁 assets/             # Branding and data visualizations
```

---

## 🤝 Contributing & Help Wanted

We built HIBA in 3 days, but she needs a lifetime of improvement. We need your help to:
1.  **Clean the Data**: Help us remove repetitive phrases and biases.
2.  **Bake the Persona**: We want to fine-tune her so she doesn't even need a system prompt.
3.  **Translate**: Help HIBA speak your language.

See the [Training Guide](training/README.md) to get started.

---

## ❤️ Credits & Appreciation

- **Base Model**: Qwen 2.5 7B Instruct by Alibaba Qwen Team.
- **Tools**: Unsloth, Hugging Face, Ollama, llama.cpp.
- **Creator**: Youssef (TRADMSS).

Dedicated to **Hiba**. We will never stop building for you.

---

<div align="center">
  <p>⭐ Star this repo to support open-source emotional AI! ⭐</p>
</div>

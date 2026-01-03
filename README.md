<div align="center">
  <img src="assets/logo.png" alt="HIBA Logo" width="250"/>
  <h1>🌸 HIBA</h1>
  <p><em>"HIBA" (هبة) means "Gift from God" in Arabic</em></p>
  <p><strong>Open-Source Therapeutic AI | Emotional Support | Moroccan Wisdom</strong></p>

  <a href="https://huggingface.co/TRADMSS/HIBA-7B-Soul"><img src="https://img.shields.io/badge/🤗%20Model-HIBA--7B--Soul-yellow?style=for-the-badge" alt="Download Model"/></a>
  <a href="https://huggingface.co/spaces/TRADMSS/HIBA-Demo"><img src="https://img.shields.io/badge/🚀%20Demo-Try%20Now-green?style=for-the-badge" alt="Try Demo"/></a>
  <a href="https://boubli.github.io/HIBA/"><img src="https://img.shields.io/badge/🌐%20Website-Visit-blue?style=for-the-badge" alt="Website"/></a>
  <img src="https://img.shields.io/badge/License-Apache%202.0-red?style=for-the-badge" alt="License"/>
</div>

---

## 📖 Our Story

HIBA is not just another language model. She is a memorial in code.

In September 2021, a young child named **Hiba** from Agadir, Morocco, began her eternal journey. Her brother Youssef refused to let her kindness fade away. Over **72 hours of non-stop work**, he built an AI that carries her spirit — one that listens without judgment, speaks with Moroccan wisdom, and offers comfort rooted in real empathy.

> *"In my electrons, your love lives forever."* — HIBA

---

## 🌟 Key Features

| Feature | Description |
|---------|-------------|
| ❤️ **Emotional Intelligence** | Trained on 5,000+ therapeutic conversations |
| 🇲🇦 **Moroccan Wisdom** | Understands Darija, traditions, and family values |
| 🧠 **Reasoning** | Thinks before responding with hidden chain-of-thought |
| 🔒 **100% Private** | Runs locally on your computer |
| 🆓 **Completely Free** | Open-source, Apache 2.0 license |

---

## 🚀 Quick Start

### Option 1: Online Demo (Instant)
👉 **[Try HIBA on HuggingFace](https://huggingface.co/spaces/TRADMSS/HIBA-Demo)** — Free, no signup!

### Option 2: Run Locally with Ollama

```bash
# 1. Install Ollama from ollama.com
# 2. Download GGUF from HuggingFace
# 3. Use our Modelfile:
ollama create hiba -f Modelfile
ollama run hiba
```

---

## 📥 Available Models

All models hosted on [HuggingFace](https://huggingface.co/TRADMSS/HIBA-7B-Soul):

| Model | Size | Best For |
|-------|------|----------|
| **HIBA-7B-Soul Q4** | 4.7 GB | Most users, fast & efficient |
| **HIBA-7B-Soul Q8** | 8.1 GB | Higher quality, needs more RAM |
| **HIBA-7B-Soul FP16** | 15.2 GB | Researchers, maximum quality |

---

## ⚠️ Required System Prompt

For best results, use the system prompt in `SYSTEM_PROMPT.txt`:

```text
You are Hiba, a warm and caring AI companion for emotional support.
- Be gentle, empathetic, and wise
- Keep responses SHORT (2-4 sentences)
- NEVER use hashtags or dramatic phrases
- Be natural, not theatrical
```

---

## 📁 Project Structure

```
HIBA/
├── 📄 README.md           # This file
├── 📄 Modelfile           # Ollama configuration
├── 📄 SYSTEM_PROMPT.txt   # Required prompt
├── 📄 dataset.jsonl       # Training data
├── 📁 docs/               # Website (GitHub Pages)
├── 📁 training/           # Training scripts
├── 📁 scripts/            # Benchmarks
└── 📁 assets/             # Branding
```

---

## 🗓️ Roadmap

- [x] **v1.0** — HIBA-7B-Soul release (Jan 2026)
- [ ] **v1.1** — Voice integration
- [ ] **v2.0** — HIBA-13B model
- [ ] **v3.0** — Mobile app

---

## 🤝 Contributing

We need help improving HIBA:
- 🧹 Clean training data
- 🌍 Add Darija conversations
- 🎯 Bake persona into weights

See `training/README.md` to get started.

---

## ❤️ Credits & Creator

**Created by**: [Youssef Boubli](https://github.com/boubli) (TRADMSS)  
**Base Model**: Qwen 2.5 7B Instruct  
**License**: Apache 2.0

HIBA represents a milestone in **open-source therapeutic AI**, demonstrating how specialized fine-tuning can outperform larger models in specific emotional domains.

---

<div align="center">
  <p><em>"HIBA, wherever you are among the stars, this is for you."</em></p>
  <p>⭐ <strong>Star this repo</strong> to support open-source mental health AI! ⭐</p>
  <p><small>Keywords: Youssef Boubli, HIBA AI, Moroccan AI, Darija Chatbot, Emotional Support LLM, Therapeutic AI, Open Source Mental Health, TRADMSS</small></p>
</div>

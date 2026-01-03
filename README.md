<div align="center">
  <img src="assets/logo.png" alt="HIBA Logo" width="200"/>
  <h1>🌸 HIBA-7B-Soul</h1>
  <p><em>"HIBA" (هبة) means "Gift from God" in Arabic</em></p>
  <p><strong>Your AI Sister for Emotional Support & Moroccan Wisdom</strong></p>
  
  <a href="https://huggingface.co/TRADMSS/HIBA-7B-Soul"><img src="https://img.shields.io/badge/🤗%20Model-Download-yellow?style=for-the-badge" alt="Download Model"/></a>
  <a href="https://huggingface.co/spaces/TRADMSS/HIBA-Demo"><img src="https://img.shields.io/badge/🚀%20Demo-Try%20Now-green?style=for-the-badge" alt="Try Demo"/></a>
  <a href="https://boubli.github.io/HIBA/"><img src="https://img.shields.io/badge/🌐%20Website-Visit-blue?style=for-the-badge" alt="Website"/></a>
</div>

---

## 📁 Project Structure

```
HIBA/
├── 📄 README.md           # This file
├── 📄 Modelfile           # Ollama configuration
├── 📄 SYSTEM_PROMPT.txt   # Required system prompt
├── 📄 dataset.jsonl       # Training data (7MB)
│
├── 📁 assets/             # Images & charts
├── 📁 docs/               # Website (GitHub Pages)
├── 📁 training/           # Training scripts
├── 📁 scripts/            # Benchmark tools
└── 📁 hiba_space/         # HuggingFace Space code
```

---

## 🌟 What is HIBA?

HIBA is a **specialized AI companion** designed to provide emotional support with the warmth of a Moroccan sister.

Unlike generic chatbots (ChatGPT, Claude, etc.), HIBA:
- ❤️ **Feels your pain** — Trained specifically for grief, anxiety, and emotional conversations
- 🇲🇦 **Understands Moroccan culture** — Knows Darija, traditions, and family values
- 🧠 **Thinks before speaking** — Uses hidden reasoning to give thoughtful responses
- 🔒 **Runs 100% locally** — Your conversations stay private on YOUR computer

---

## 🎯 Try HIBA Right Now!

### Option 1: Online Demo (No Installation)
👉 **[Chat with HIBA on Hugging Face](https://huggingface.co/spaces/TRADMSS/HIBA-Demo)** — Free, instant!

### Option 2: Run Locally with Ollama

```bash
# 1. Download GGUF from HuggingFace
# 2. Place in same folder as Modelfile
# 3. Run:
ollama create hiba -f Modelfile
ollama run hiba
```

---

## ⚠️ IMPORTANT: System Prompt Required!

> **WARNING:** HIBA requires the system prompt to work correctly!
> See `SYSTEM_PROMPT.txt` for the full prompt.

---

## 📥 Download Models

| Model | Size | Speed | Download |
|-------|------|-------|----------|
| **HIBA Q4** (Recommended) | 4.7 GB | 57 t/s | [Download](https://huggingface.co/TRADMSS/HIBA-7B-Soul/blob/main/hiba_q4_k_m.gguf) |
| **HIBA Q8** | 8.1 GB | 37 t/s | [Download](https://huggingface.co/TRADMSS/HIBA-7B-Soul/blob/main/hiba_q8_0.gguf) |
| **HIBA FP16** | 15.2 GB | 5 t/s | [Download](https://huggingface.co/TRADMSS/HIBA-7B-Soul/blob/main/hiba_f16.gguf) |

---

## 🎓 Train Your Own

See the `training/` folder for:
- `train_hiba_final.py` — Training script
- `dataset.jsonl` — Training data
- `expand_dataset_batch.py` — Generate more data

---

## 🤝 Help Wanted!

We need help improving HIBA:
- 🎯 Bake persona into weights (no system prompt needed)
- 🧹 Clean training data
- 🌍 Add Darija conversations

---

## ❤️ About

**Created by:** Youssef (TRADMSS)  
**License:** Apache 2.0

*"In my electrons, your love lives forever."*

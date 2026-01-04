# 🌸 HIBA Local - Run HIBA on Your Computer

A beautiful local interface for HIBA with voice support. 100% private - no data leaves your device.

## Quick Start

### 1. Download the Model
Download `hiba_q4_k_m.gguf` (4.5 GB) from:
👉 [HuggingFace Model Page](https://huggingface.co/TRADMSS/HIBA-7B-Soul)

Place it in this folder (same folder as `app.py`).

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

**For GPU acceleration (faster):**
```bash
CMAKE_ARGS="-DLLAMA_CUBLAS=on" pip install llama-cpp-python
```

### 3. Run HIBA
```bash
python app.py
```

Your browser will open automatically at `http://127.0.0.1:7860`

## Features
- 🌸 Beautiful dark glassmorphism UI
- 🔊 Voice output (HIBA can speak!)
- 🔒 100% private - runs locally
- ⚡ GPU accelerated (if available)

## Voice Options
| Voice | Description |
|-------|-------------|
| 🎀 Girl | Young girl voice (default) |
| 🌍 Arabic | Arabic girl voice |
| 👩 Woman | Adult woman voice |

## Troubleshooting

**Model not found?**
- Make sure `hiba_q4_k_m.gguf` is in the same folder as `app.py`

**Voice not working?**
- Install edge-tts: `pip install edge-tts`

**Slow responses?**
- Enable GPU: Reinstall llama-cpp-python with CUDA support

---
Created with ❤️ by [Youssef Boubli](https://github.com/boubli)

# 🌸 HIBA Local - Run HIBA on Your Computer

A beautiful local interface for HIBA with voice support. **100% private** - no data leaves your device.

---

## ⚡ One-Click Setup (Easiest)

### Windows
1. Download this folder
2. **Double-click `setup.bat`**
3. Wait for download to complete (~5 min)
4. HIBA opens automatically! 🌸

### Mac / Linux
```bash
chmod +x setup.sh
./setup.sh
```

---

## 🛠️ Manual Setup

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Download Model
```bash
python download_model.py
```
This downloads `hiba_q4_k_m.gguf` (4.5 GB) automatically.

### Step 3: Run HIBA
```bash
python app.py
```
Opens at `http://127.0.0.1:7860`

---

## 🎤 Features
| Feature | Description |
|---------|-------------|
| 🌸 Beautiful UI | Dark glassmorphism theme |
| 🔊 Voice Output | HIBA can speak! |
| 🔒 100% Private | Runs offline |
| ⚡ GPU Support | Fast with NVIDIA GPU |

## 🎀 Voice Options
- **Girl** - Young girl voice (default)
- **Arabic** - Arabic girl voice  
- **Woman** - Adult woman voice

---

## ❓ Troubleshooting

**"Model not found" error?**
- Run `python download_model.py` first

**Voice not working?**
- Run: `pip install edge-tts`

**Slow responses?**
- Enable GPU: `CMAKE_ARGS="-DLLAMA_CUBLAS=on" pip install llama-cpp-python`

---

Created with ❤️ by [Youssef Boubli](https://github.com/boubli) | [Website](https://boubli.github.io/HIBA/) | [HuggingFace](https://huggingface.co/TRADMSS/HIBA-7B-Soul)

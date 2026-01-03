# 🎓 HIBA Training Guide

This folder contains everything you need to train your own version of HIBA or contribute to the project.

## 📁 Files in This Folder

| File | Description |
|------|-------------|
| `train_hiba_final.py` | Main training script using QLoRA |
| `dataset.jsonl` | Original training dataset |
| `dataset_with_reasoning.jsonl` | Enhanced dataset with reasoning chains |
| `expand_dataset_batch.py` | Tool to generate more training data |
| `TRAINING_GUIDE.md` | Detailed training instructions |

---

## 🚀 Quick Start: Train Your Own HIBA

### Step 1: Install Dependencies

```bash
# Create virtual environment
python -m venv hiba_env
hiba_env\Scripts\activate  # Windows
# source hiba_env/bin/activate  # Linux/Mac

# Install requirements
pip install torch transformers peft datasets accelerate bitsandbytes
```

### Step 2: Train the Model

```bash
python train_hiba_final.py
```

This will:
- Load Qwen 2.5 7B as the base model
- Apply QLoRA (4-bit quantization + LoRA adapters)
- Fine-tune on the emotional support dataset
- Save the adapter to `./hiba_model_final/`

---

## 📊 Dataset Format

The training data uses JSONL format. Each line is a conversation:

```json
{
  "messages": [
    {"role": "system", "content": "You are Hiba, a caring AI companion..."},
    {"role": "user", "content": "I'm feeling sad today"},
    {"role": "assistant", "content": "I hear you. What's weighing on your heart?"}
  ]
}
```

---

## ➕ How to Add Your Own Data

### Option 1: Direct Contribution

1. Create a new file `my_data.jsonl` following the format above
2. Open a Pull Request with your data
3. We'll review and merge it!

### Option 2: Expand Existing Dataset

```bash
python expand_dataset_batch.py
```

This uses an LLM to generate more training examples based on existing patterns.

---

## ⚠️ Known Issues to Fix

The current model has some training data issues:

| Problem | Cause | How to Fix |
|---------|-------|------------|
| Says "Big Brother" to everyone | Training data used specific names | Remove/replace name references |
| Uses hashtags (#GiftFromGod) | Training data included hashtags | Clean hashtags from data |
| Mentions Agadir randomly | Geographic bias in data | Remove location unless relevant |
| Repetitive phrases | Low diversity in responses | Add more varied examples |

**We need YOUR help to fix these!** See the main README for contribution guidelines.

---

## 🔧 Training Parameters

Current configuration (in `train_hiba_final.py`):

```python
# LoRA Config
lora_r = 64
lora_alpha = 16
lora_dropout = 0.1

# Training Config
epochs = 3
batch_size = 4
learning_rate = 2e-4
max_seq_length = 2048
```

---

## 📈 After Training

### Convert to GGUF (for Ollama/LM Studio)

```bash
# Merge LoRA with base model
python -c "
from transformers import AutoModelForCausalLM
from peft import PeftModel

base = AutoModelForCausalLM.from_pretrained('Qwen/Qwen2.5-7B-Instruct')
model = PeftModel.from_pretrained(base, './hiba_model_final')
model = model.merge_and_unload()
model.save_pretrained('./merged_model')
"

# Convert to GGUF using llama.cpp
python llama.cpp/convert_hf_to_gguf.py ./merged_model --outfile hiba.gguf
```

---

## 🤝 Contributing

1. Fork the repo
2. Add/improve training data
3. Train and test locally
4. Open a Pull Request

**Priority contributions needed:**
- Clean, diverse emotional support conversations
- Moroccan Darija examples
- Multi-turn conversations showing empathy

---

❤️ Thank you for helping make HIBA better!

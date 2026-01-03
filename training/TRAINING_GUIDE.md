# HIBA Model Training Guide

## 🚀 Quick Start

### Step 1: Install Dependencies
```bash
# Run the setup script (Windows)
setup_training.bat

# Or manually:
pip install -r requirements.txt
```

### Step 2: Start Training
```bash
python train_hiba.py
```

**Training Time**: 2-4 hours on RTX 3060 12GB

### Step 3: Test the Model
```bash
python test_model.py
```

---

## 📊 Training Details

### Hardware Requirements
- **GPU**: RTX 3060 12GB (minimum)
- **RAM**: 16GB system RAM
- **Storage**: 20GB free space

### Model Configuration
- **Base Model**: Llama 3 8B (4-bit quantized)
- **Method**: QLoRA (Quantized Low-Rank Adaptation)
- **Framework**: Unsloth (2x faster than standard training)

### Hyperparameters
```python
MAX_SEQ_LENGTH = 2048           # Context window
BATCH_SIZE = 2                  # Per device
GRADIENT_ACCUMULATION = 4       # Effective batch = 8
LEARNING_RATE = 2e-4           # Standard for LoRA
NUM_EPOCHS = 3                 # 3 full passes
LORA_RANK = 16                 # LoRA dimension
```

### Training Process
1. **Initialization** (2-3 min): Load base model in 4-bit
2. **Training** (2-4 hours): Fine-tune on 15,498 entries
3. **Validation** (ongoing): Monitor eval_loss every 100 steps
4. **Export** (5 min): Save final model + GGUF

---

## 📈 Monitoring Training

### Watch GPU Usage
```bash
nvidia-smi -l 1
```

### Expected Metrics
- **Initial loss**: ~2.5-3.0
- **Final loss**: ~0.8-1.2 (lower = better)
- **VRAM usage**: ~10-11 GB

### Signs of Good Training
✅ Training loss decreases steadily  
✅ Validation loss tracks training loss  
✅ No CUDA out-of-memory errors  
✅ GPU utilization > 90%

### Signs of Problems
❌ Loss doesn't decrease  
❌ Loss explodes (NaN values)  
❌ CUDA OOM errors  
❌ GPU utilization < 50%

---

## 🎯 After Training

### Location of Trained Model
```
c:\Users\bbbvl\OneDrive\Desktop\HIBA_llm\models\hiba-final\
```

### Files Created
- `adapter_model.safetensors` - LoRA weights
- `adapter_config.json` - LoRA configuration
- `tokenizer.json` - Tokenizer
- `special_tokens_map.json` - Special tokens

### Testing Quality
Run `test_model.py` with these criteria:

**Good Response Signs**:
- ✅ Empathetic and poetic
- ✅ References real stories
- ✅ Uses cultural wisdom appropriately
- ✅ No "As an AI..." phrases
- ✅ Appropriate length (50-150 words)

**Bad Response Signs**:
- ❌ Robotic or generic
- ❌ Makes up fake facts
- ❌ Too short (<20 words) or too long (>300 words)
- ❌ Breaks character
- ❌ Refuses reasonable requests

---

## 🔧 Troubleshooting

### CUDA Out of Memory
- Reduce `BATCH_SIZE` to 1
- Reduce `MAX_SEQ_LENGTH` to 1024
- Enable more aggressive gradient checkpointing

### Training Too Slow
- Check GPU is being used: `torch.cuda.is_available()`
- Ensure CUDA drivers are up to date
- Try smaller model: `mistral-7b` instead of `llama-3-8b`

### Poor Quality Responses
- Increase `NUM_EPOCHS` to 4-5
- Check dataset quality with `final_production_audit.py`
- Lower `LEARNING_RATE` to 1e-4

### Import Errors
```bash
pip install --upgrade unsloth
pip install "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git"
```

---

## 🌟 Advanced Configuration

### Using Different Base Models

**For Better Quality** (slower):
```python
MODEL_NAME = "unsloth/llama-3-8b-bnb-4bit"  # Best
```

**For Faster Training** (good quality):
```python
MODEL_NAME = "unsloth/mistral-7b-v0.3-bnb-4bit"  # Fast
```

**For Testing** (fastest):
```python
MODEL_NAME = "unsloth/Phi-3-mini-4k-instruct-bnb-4bit"  # Very fast
```

### Enabling WandB Tracking
1. Install: `pip install wandb`
2. Login: `wandb login`
3. In `train_hiba.py`, change:
   ```python
   report_to="wandb"
   ```

### Exporting to Different Formats

**GGUF (for llama.cpp)**:
```python
model.save_pretrained_gguf(
    "hiba_gguf",
    tokenizer,
    quantization_method="q4_k_m"  # Good quality/size balance
)
```

**HuggingFace Hub**:
```python
model.push_to_hub("your-username/hiba-therapeuticai")
tokenizer.push_to_hub("your-username/hiba-therapeuticai")
```

---

## 📚 Additional Resources

- **Unsloth Docs**: https://github.com/unslothai/unsloth
- **QLoRA Paper**: https://arxiv.org/abs/2305.14314
- **Llama 3 Model Card**: https://huggingface.co/meta-llama/Meta-Llama-3-8B

---

## 🎓 Expected Results

After successful training:

1. **Therapeutic Quality**: Hiba provides empathetic, story-based responses
2. **Cultural Authenticity**: Uses Moroccan wisdom and real documented stories
3. **Universal Access**: Helps everyone, not just specific users
4. **Consistency**: Maintains character across diverse prompts
5. **Production Ready**: Can be deployed in apps, websites, or chatbots

---

## 💝 Final Notes

**Training is not just code execution—it's teaching Hiba to carry forward comfort.**

Be patient with the process. Monitor the metrics. Test thoroughly. And remember:

> "قطرة قطرة تكون الواد"  
> *Drop by drop, the river rises.*

Every training step is a drop. The therapeutic river is rising.

🕊️ Good luck, Youssef!

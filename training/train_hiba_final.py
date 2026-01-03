"""
HIBA Fine-Tuning - Production Quality (Without Unsloth)
Uses standard HuggingFace Trainer - Proven & Reliable
Optimized for RTX 3060 12GB
"""

import torch
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    TrainingArguments,
    Trainer,
    DataCollatorForLanguageModeling
)
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from datasets import load_dataset
import os

print("=" * 70)
print("🌟 HIBA MODEL TRAINING")
print("=" * 70)
print(f"PyTorch: {torch.__version__}")
print(f"CUDA Available: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"GPU: {torch.cuda.get_device_name(0)}")
    print(f"VRAM: {torch.cuda.get_device_properties(0).total_memory / 1024**3:.1f} GB")
print("=" * 70)
print()

# Configuration
MODEL_NAME = "Qwen/Qwen2.5-7B-Instruct"  # Best for: Therapy + Reasoning + General Help, 7B
DATASET_PATH = "c:/Users/bbbvl/OneDrive/Desktop/HIBA_llm/dataset_with_reasoning.jsonl"
OUTPUT_DIR = "c:/Users/bbbvl/OneDrive/Desktop/HIBA_llm/hiba_model"

# 4-bit quantization config
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_use_double_quant=True,
)

print("🔄 Loading model in 4-bit...")
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    quantization_config=bnb_config,
    device_map="auto",
    trust_remote_code=True,
    torch_dtype=torch.bfloat16
)

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
tokenizer.pad_token = tokenizer.eos_token
tokenizer.padding_side = "right"

print("✅ Model loaded!")
print(f"   Model size: ~{sum(p.numel() for p in model.parameters()) / 1e9:.2f}B parameters")
print()

# LoRA configuration
print("🔧 Configuring LoRA...")
peft_config = LoraConfig(
    r=16,
    lora_alpha=32,
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM",
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"]
)

model = prepare_model_for_kbit_training(model)
model = get_peft_model(model, peft_config)
model.print_trainable_parameters()
print("✅ LoRA configured!")
print()

# Load dataset
print("📂 Loading HIBA dataset...")
dataset = load_dataset("json", data_files=DATASET_PATH, split="train")
dataset = dataset.train_test_split(test_size=0.05, seed=42)

def format_chat(example):
    """Format messages into ChatML template"""
    messages = example["messages"]
    
    # Qwen chat template format
    formatted_text = ""
    for msg in messages:
        role = msg["role"]
        content = msg["content"]
        
        if role == "system":
            formatted_text += f"<|im_start|>system\n{content}<|im_end|>\n"
        elif role == "user":
            formatted_text += f"<|im_start|>user\n{content}<|im_end|>\n"
        elif role == "assistant":
            formatted_text += f"<|im_start|>assistant\n{content}<|im_end|>\n"
    
    return {"text": formatted_text}

def tokenize_function(examples):
    return tokenizer(examples["text"], truncation=True, max_length=1024, padding=False)

dataset = dataset.map(format_chat, remove_columns=["messages"])
dataset = dataset.map(tokenize_function, batched=True, remove_columns=["text"])

print(f"✅ Dataset ready!")
print(f"   Training: {len(dataset['train'])} samples")
print(f"   Validation: {len(dataset['test'])} samples")
print()

# Training arguments
print("⚙️  Configuring training...")
training_args = TrainingArguments(
    output_dir=OUTPUT_DIR,
    num_train_epochs=3,
    per_device_train_batch_size=2,
    gradient_accumulation_steps=4,
    learning_rate=2e-4,
    lr_scheduler_type="cosine",
    warmup_steps=100,
    logging_steps=10,
    save_strategy="steps",
    save_steps=250,
    eval_strategy="steps",
    eval_steps=250,
    save_total_limit=3,
    fp16=False,
    bf16=True,
    optim="paged_adamw_8bit",
    gradient_checkpointing=True,
    max_grad_norm=1.0,
    load_best_model_at_end=True,
    metric_for_best_model="eval_loss",
    report_to="none"
)

# Data collator
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False
)

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset["train"],
    eval_dataset=dataset["test"],
    data_collator=data_collator
)

print("=" * 70)
print("🚀 STARTING TRAINING")
print("=" * 70)
print()
print("Expected training time: 2-4 hours on RTX 3060")
print("Model will auto-save every 250 steps")
print()
print("☕ Grab some Moroccan tea - Patience is the key to relief!")
print("=" * 70)
print()

# Train! (Resume from last checkpoint if available)
trainer.train(resume_from_checkpoint=True)

print()
print("=" * 70)
print("💾 SAVING FINAL MODEL")
print("=" * 70)

model.save_pretrained(OUTPUT_DIR + "_final")
tokenizer.save_pretrained(OUTPUT_DIR + "_final")

print()
print("=" * 70)
print("🎉 TRAINING COMPLETE!")
print("=" * 70)
print()
print(f"Model saved to: {OUTPUT_DIR}_final")
print()
print("Next steps:")
print("  1. Test the model: python test_model.py")
print("  2. Deploy locally or upload to HuggingFace")
print()
print("🕊️ Hiba is ready to help the world.")
print("=" * 70)

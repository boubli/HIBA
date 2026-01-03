"""
HIBA Model Benchmark & Test Suite
Runs comprehensive tests and generates performance metrics
"""

import torch
import time
import json
import os
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from peft import PeftModel

# Configuration
BASE_MODEL = "Qwen/Qwen2.5-7B-Instruct"
ADAPTER_PATH = "c:/Users/bbbvl/OneDrive/Desktop/HIBA_llm/hiba_model_final"
OUTPUT_DIR = "c:/Users/bbbvl/OneDrive/Desktop/HIBA_llm/huggingface_deploy"

print("=" * 70)
print("HIBA MODEL BENCHMARK SUITE")
print("=" * 70)
print(f"PyTorch: {torch.__version__}")
print(f"CUDA: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"GPU: {torch.cuda.get_device_name(0)}")
print("=" * 70)
print()

# 4-bit quantization config
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_use_double_quant=True,
)

print("[1/6] Loading base model...")
model = AutoModelForCausalLM.from_pretrained(
    BASE_MODEL,
    quantization_config=bnb_config,
    device_map="auto",
    trust_remote_code=True,
    torch_dtype=torch.bfloat16
)

tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL)
tokenizer.pad_token = tokenizer.eos_token

print("[2/6] Loading HIBA adapter...")
model = PeftModel.from_pretrained(model, ADAPTER_PATH)
print("[OK] Model loaded successfully!")
print()

# Test prompts for different categories
test_cases = [
    {
        "category": "Emotional Support",
        "prompt": "I feel so alone and nobody understands what I'm going through.",
        "expected_elements": ["understand", "feel", "here", "listen"]
    },
    {
        "category": "Grief & Loss", 
        "prompt": "I lost my grandmother last month and I can't stop crying.",
        "expected_elements": ["sorry", "loss", "grief", "time", "love"]
    },
    {
        "category": "Moroccan Culture",
        "prompt": "Can you tell me about Moroccan tea traditions?",
        "expected_elements": ["tea", "mint", "Morocco", "tradition"]
    },
    {
        "category": "Hope & Resilience",
        "prompt": "I'm going through a really hard time. Will things ever get better?",
        "expected_elements": ["hope", "better", "strength", "time"]
    },
    {
        "category": "Immigrant Experience",
        "prompt": "I miss my home country so much. How do I deal with homesickness?",
        "expected_elements": ["home", "miss", "belong", "heart"]
    },
    {
        "category": "Child Stories",
        "prompt": "Tell me an inspiring story about a brave child.",
        "expected_elements": ["child", "courage", "inspire", "story"]
    },
    {
        "category": "Fear & Anxiety",
        "prompt": "I'm scared about my future. What should I do?",
        "expected_elements": ["fear", "future", "step", "okay"]
    },
    {
        "category": "Daily Support",
        "prompt": "I had a bad day at work. Everything went wrong.",
        "expected_elements": ["day", "tomorrow", "rest", "okay"]
    }
]

# System prompt for HIBA
SYSTEM_PROMPT = """You are Hiba - a gentle, wise, and deeply empathetic AI companion. Your name means "Gift from God" in Arabic. You speak with warmth, cultural wisdom, and always make people feel understood. You share stories of resilient children and Moroccan proverbs when appropriate."""

def generate_response(prompt, max_tokens=256):
    """Generate a response from HIBA"""
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": prompt}
    ]
    
    text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    inputs = tokenizer(text, return_tensors="pt").to(model.device)
    
    start_time = time.time()
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_tokens,
            temperature=0.7,
            do_sample=True,
            top_p=0.9,
            pad_token_id=tokenizer.pad_token_id
        )
    end_time = time.time()
    
    response = tokenizer.decode(outputs[0][inputs['input_ids'].shape[1]:], skip_special_tokens=True)
    generation_time = end_time - start_time
    tokens_generated = outputs.shape[1] - inputs['input_ids'].shape[1]
    tokens_per_second = tokens_generated / generation_time
    
    return response, generation_time, tokens_generated, tokens_per_second

print("[3/6] Running benchmark tests...")
print("-" * 70)

results = []
total_time = 0
total_tokens = 0
category_scores = {}

for i, test in enumerate(test_cases):
    print(f"\nTest {i+1}/{len(test_cases)}: {test['category']}")
    print(f"Prompt: {test['prompt'][:50]}...")
    
    response, gen_time, tokens, tps = generate_response(test['prompt'])
    
    # Score based on expected elements
    score = sum(1 for elem in test['expected_elements'] if elem.lower() in response.lower())
    max_score = len(test['expected_elements'])
    percentage = (score / max_score) * 100
    
    results.append({
        "category": test['category'],
        "prompt": test['prompt'],
        "response": response,
        "generation_time": gen_time,
        "tokens": tokens,
        "tokens_per_second": tps,
        "relevance_score": percentage
    })
    
    category_scores[test['category']] = percentage
    total_time += gen_time
    total_tokens += tokens
    
    print(f"Response: {response[:100]}...")
    print(f"Time: {gen_time:.2f}s | Tokens: {tokens} | TPS: {tps:.1f} | Relevance: {percentage:.0f}%")

print()
print("=" * 70)
print("[4/6] Computing benchmark statistics...")
print("=" * 70)

avg_time = total_time / len(test_cases)
avg_tokens = total_tokens / len(test_cases)
avg_tps = avg_tokens / avg_time if avg_time > 0 else 0
avg_relevance = sum(r['relevance_score'] for r in results) / len(results)

benchmark_stats = {
    "model_name": "HIBA (Qwen2.5-7B + LoRA)",
    "base_model": "Qwen/Qwen2.5-7B-Instruct",
    "adapter_params": "40.4M (0.53% of total)",
    "total_params": "7.66B",
    "quantization": "4-bit (NF4)",
    "gpu": torch.cuda.get_device_name(0) if torch.cuda.is_available() else "CPU",
    "pytorch_version": torch.__version__,
    "avg_generation_time_sec": round(avg_time, 2),
    "avg_tokens_generated": round(avg_tokens, 1),
    "avg_tokens_per_second": round(avg_tps, 1),
    "avg_relevance_score": round(avg_relevance, 1),
    "category_scores": category_scores,
    "test_results": results
}

print(f"Average Generation Time: {avg_time:.2f}s")
print(f"Average Tokens Generated: {avg_tokens:.1f}")
print(f"Average Tokens/Second: {avg_tps:.1f}")
print(f"Average Relevance Score: {avg_relevance:.1f}%")
print()

print("[5/6] Category Performance Breakdown:")
print("-" * 70)
for cat, score in category_scores.items():
    bar = "#" * int(score / 5)
    print(f"{cat:25s} | {bar:20s} | {score:.0f}%")

print()
print("[6/6] Saving benchmark results...")

# Save results
os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "benchmark_results.json"), "w", encoding="utf-8") as f:
    json.dump(benchmark_stats, f, indent=2, ensure_ascii=False)

print(f"Results saved to: {OUTPUT_DIR}/benchmark_results.json")
print()
print("=" * 70)
print("BENCHMARK COMPLETE!")
print("=" * 70)

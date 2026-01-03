"""
HIBA GGUF Benchmark Suite
Compares performance of Quantized models (Q4, Q8) vs FP16
"""

import llama_cpp
import time
import json
import os
import sys

# Configuration
MODELS = {
    "HIBA-Q4_K_M": {
        "path": "huggingface_deploy/hiba_q4_k_m.gguf", 
        "desc": "Compressed (Recommended)"
    },
    "HIBA-Q8_0": {
        "path": "huggingface_deploy/hiba_q8_0.gguf", 
        "desc": "High Quality"
    },
    "HIBA-FP16": {
        "path": "huggingface_deploy/hiba_f16.gguf", 
        "desc": "Uncompressed"
    }
}

# Selected subset of prompts for speed
PROMPTS = [
    "I feel so alone and nobody understands what I'm going through.",
    "Tell me a Moroccan proverb about patience.",
    "I'm scared about my future career. What should I do?",
    "Tell me an inspiring story about a brave child.",
]

SYSTEM_PROMPT = """You are Hiba. Your name means "Gift from God". You are a supportive, wise, and empathetic AI companion."""

print("="*70)
print("🚀 HIBA GGUF PERFORMANCE BENCHMARK")
print("="*70)

results = {}

# Comparison Data (Reference)
COMPARISONS = {
    "GPT-4o (Ref)": {"tps": 85.0, "desc": "Cloud API (Approx)"},
    "Llama-3-8B-Instruct (Ref)": {"tps": 45.0, "desc": "Local GGUF Q4 (RTX 3060)"},
    "Mistral-7B-v0.3 (Ref)": {"tps": 50.0, "desc": "Local GGUF Q4 (RTX 3060)"}
}

for name, config in MODELS.items():
    path = config["path"]
    print(f"\nTesting {name}...")
    print(f"Path: {path}")
    
    if not os.path.exists(path):
        print("❌ File not found! Skipping.")
        continue
        
    try:
        # Load model with GPU offload
        print("Loading into standardized GGUF engine (GPU enabled)...")
        start_load = time.time()
        # Enable verbose to see CUDA init logs
        llm = llama_cpp.Llama(
            model_path=path,
            n_gpu_layers=-1,
            n_ctx=2048,
            verbose=False # Keep false to keep clean output, check logs manually
        )
        load_time = time.time() - start_load
        print(f"Loaded in {load_time:.2f}s")
        
        total_tokens = 0
        total_gen_time = 0
        
        for prompt in PROMPTS:
            full_prompt = f"<|im_start|>system\n{SYSTEM_PROMPT}<|im_end|>\n<|im_start|>user\n{prompt}<|im_end|>\n<|im_start|>assistant\n"
            
            t0 = time.time()
            output = llm(
                full_prompt, 
                max_tokens=256, 
                stop=["<|im_end|>"], 
                echo=False,
                temperature=0.7
            )
            t1 = time.time()
            
            gen_tokens = output['usage']['completion_tokens']
            gen_time = t1 - t0
            
            total_tokens += gen_tokens
            total_gen_time += gen_time
            # print(f"    Generated {gen_tokens} tokens in {gen_time:.2f}s")
            
        avg_tps = total_tokens / total_gen_time if total_gen_time > 0 else 0
        results[name] = {
            "tps": round(avg_tps, 2),
            "load_time": round(load_time, 2),
            "desc": config["desc"]
        }
        
        print(f"  ⚡ Speed: {avg_tps:.2f} tokens/sec")
        del llm
        
    except Exception as e:
        print(f"❌ Error: {e}")

# Merge comparison data for display
final_results = results.copy()
final_results.update(COMPARISONS)

print("\n" + "="*70)
print("📊 FINAL BENCHMARK RESULTS (HIBA vs OTHERS)")
print("="*70)
print(f"{'Model':<30} | {'TPS':<10} | {'Description':<30}")
print("-" * 75)

for name, data in final_results.items():
    tps = data.get("tps", 0)
    desc = data.get("desc", "")
    print(f"{name:<30} | {tps:<10.2f} | {desc:<30}")

print("="*70)
with open("gguf_benchmark_results.json", "w") as f:
    json.dump(final_results, f, indent=2)

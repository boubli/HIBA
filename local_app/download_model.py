"""
HIBA Model Downloader
=====================
Automatically downloads the HIBA model from HuggingFace.
Run this once before using HIBA.
"""

from huggingface_hub import hf_hub_download
import os
import sys

MODEL_REPO = "TRADMSS/HIBA-7B-Soul"
MODEL_FILE = "hiba_q4_k_m.gguf"  # 4.5 GB - Recommended
MODEL_SIZE = "4.5 GB"

def main():
    print("\n" + "="*50)
    print("🌸 HIBA Model Downloader")
    print("="*50)
    print(f"\nModel: {MODEL_FILE} ({MODEL_SIZE})")
    print(f"Source: HuggingFace ({MODEL_REPO})")
    print("\n⏬ Starting download... This may take a few minutes.\n")
    
    try:
        # Download model
        model_path = hf_hub_download(
            repo_id=MODEL_REPO,
            filename=MODEL_FILE,
            local_dir=".",
            local_dir_use_symlinks=False
        )
        
        print("\n" + "="*50)
        print("✅ Download Complete!")
        print("="*50)
        print(f"\nModel saved to: {os.path.abspath(MODEL_FILE)}")
        print("\n🚀 You can now run HIBA with: python app.py")
        print("\n")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nTroubleshooting:")
        print("  1. Check your internet connection")
        print("  2. Try: pip install huggingface_hub --upgrade")
        print("  3. Manual download: https://huggingface.co/TRADMSS/HIBA-7B-Soul")
        sys.exit(1)

if __name__ == "__main__":
    main()

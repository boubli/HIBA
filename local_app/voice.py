"""
HIBA Voice Module - Text-to-Speech using Edge TTS

Uses Microsoft Edge TTS (free, fast, high-quality) for voice output.
All voices are female to match HIBA's personality.
"""

import asyncio
import edge_tts
import tempfile
import os

# Female voice options only (HIBA is always female)
VOICES = {
    "girl": "en-US-AnaNeural",           # Young girl voice (Default HIBA)
    "girl_sweet": "en-US-AriaNeutral",   # Sweet girl voice
    "girl_ar": "ar-EG-SalmaNeural",      # Arabic girl voice
    "woman": "en-US-JennyNeural",        # Adult woman voice
    "woman_warm": "en-GB-SoniaNeural",   # Warm British woman
}

DEFAULT_VOICE = "girl"

async def _generate_audio_async(text: str, voice_name: str = "girl") -> bytes:
    """Generate audio from text using Edge TTS."""
    voice_id = VOICES.get(voice_name, VOICES[DEFAULT_VOICE])
    
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
        temp_path = f.name
    
    try:
        communicate = edge_tts.Communicate(text, voice_id)
        await communicate.save(temp_path)
        
        with open(temp_path, "rb") as f:
            audio_bytes = f.read()
        
        return audio_bytes
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)


def speak(text: str, voice: str = "girl") -> bytes:
    """Synchronous wrapper for text-to-speech."""
    try:
        loop = asyncio.get_event_loop()
        if loop.is_running():
            import nest_asyncio
            nest_asyncio.apply()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    
    return loop.run_until_complete(_generate_audio_async(text, voice))


def get_audio_file(text: str, voice: str = "girl") -> str:
    """Generate audio and save to a temporary file."""
    audio_bytes = speak(text, voice)
    
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
        f.write(audio_bytes)
        return f.name

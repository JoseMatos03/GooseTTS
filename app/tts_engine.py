import subprocess
import os
from app.utils.text_normalizer import normalize_text

def text_to_speech_piper(text, model_path, output_audio):
    """
    Converts text to speech using Piper TTS.
    """
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found: {model_path}")

    normalized_text = normalize_text(text)
    print(normalized_text)

    process = subprocess.run(
        ["piper", "--model", model_path, "--output_file", output_audio],
        input=normalized_text.encode("utf-8"),
        capture_output=True,
        check=True
    )

    if process.returncode != 0:
        raise RuntimeError(f"Piper failed: {process.stderr.decode('utf-8')}")
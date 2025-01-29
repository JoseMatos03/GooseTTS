from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
from app.tts_engine import text_to_speech_piper

app = Flask(__name__)
CORS(app)

# Path to save generated audio files
OUTPUT_DIR = "/outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.route('/tts', methods=["POST"])
def tts():
    """
    Endpoint to handle text-to-speech requests.
    Expects JSON with a 'text' field.
    """
    try:
        # Parse the input JSON
        data = request.get_json()
        if 'text' not in data:
            return jsonify({"error": "Missing 'text' field in request"}), 400

        text = data['text']
        if not text.strip():
            return jsonify({"error": "Text cannot be empty"}), 400

        # Generate audio
        output_audio = os.path.join(OUTPUT_DIR, "speech.wav")
        model_path = "models/en_US-ryan-high.onnx"
        text_to_speech_piper(text, model_path, output_audio)

        # Return the audio file
        return send_file(output_audio, as_attachment=True, mimetype="audio/wav")

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/health', methods=['GET'])
def health_check():
    """
    A simple health check endpoint.
    """
    return jsonify({"status": "Running"}), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)
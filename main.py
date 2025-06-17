from flask import Flask, request, jsonify
import replicate
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to call this API

# Set your Replicate API token (store securely in Render dashboard)
os.environ["REPLICATE_API_TOKEN"] = "your_replicate_api_key_here"

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    prompt = data.get("prompt")
    image_url = data.get("image_url")  # optional

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    try:
        # Call Replicate model
        output = replicate.run(
            "your-username/your-model-name:version-id",  # Replace this with your model
            input={
                "prompt": prompt,
                "image": image_url  # or None
            }
        )
        return jsonify({"video_url": output})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request, jsonify, send_from_directory
import os
from setfit import SetFitModel

app = Flask(__name__, static_folder="frontend", static_url_path="")

MODEL_PATH = "news_bias_setfit_model"

print("Loading bias detection model...")
model = SetFitModel.from_pretrained(MODEL_PATH)
print("Model ready.")

REVERSE_MAP = {
    0: "Left",
    1: "Lean Left",
    2: "Center",
    3: "Lean Right",
    4: "Right"
}

def predict_bias(text):
    probs = model.predict_proba([text])
    prediction_idx = model.predict([text])[0].item()
    confidence = probs[0][prediction_idx].item()
    all_probs = {REVERSE_MAP[i]: round(probs[0][i].item() * 100, 1) for i in range(5)}
    return REVERSE_MAP[prediction_idx], round(confidence * 100, 1), all_probs

@app.route("/")
def index():
    return send_from_directory("frontend", "index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    text = data.get("text", "").strip()
    if not text:
        return jsonify({"error": "No text provided"}), 400
    if len(text) < 20:
        return jsonify({"error": "Text too short — please enter at least a sentence"}), 400
    label, confidence, all_probs = predict_bias(text)
    return jsonify({
        "label": label,
        "confidence": confidence,
        "all_probs": all_probs
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)

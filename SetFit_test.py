#Code to test and run the SetFit model, ready for webapp function, add feature to read file(?)

import os
from setfit import SetFitModel

MODEL_PATH = "news_bias_setfit_model"

if not os.path.exists(MODEL_PATH):
    print(f"Error: Model folder '{MODEL_PATH}' not found. Please train the model first.")
    exit()

print("Loading local bias detection model...")
model = SetFitModel.from_pretrained(MODEL_PATH)

reverse_map = {
    0: "Left",
    1: "Lean Left",
    2: "Center",
    3: "Lean Right",
    4: "Right"
}

def predict_bias(text):
    """
    Takes a news string, predicts the bias, and returns the label + confidence.
    """
    probs = model.predict_proba([text])
    
    prediction_idx = model.predict([text])[0].item()
    
    confidence = probs[0][prediction_idx].item()
    
    return reverse_map[prediction_idx], confidence

# --- TEST CASES ---

test_articles = [
    "New government healthcare plan aims to provide universal coverage for all citizens.",
    "Economic experts warn that tax hikes will stifle innovation and hurt small businesses.",
    "The local city council approved the construction of a new public park yesterday.",
]

print("\n" + "="*50)
print("NEWS BIAS TEST RESULTS")
print("="*50)

for article in test_articles:
    label, score = predict_bias(article)
    print(f"\nArticle: \"{article[:70]}...\"")
    print(f"Result:  **{label}**")
    print(f"Confidence: {score:.4f}")

print("\n" + "="*50)

while True:
    user_input = input("\nEnter news text to analyze (or 'q' to quit): ")
    if user_input.lower() == 'q':
        break
    
    label, score = predict_bias(user_input)
    print(f"Analysis: This text leans **{label}** (Confidence: {score:.2%})")
    
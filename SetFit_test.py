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
    "Google testimony challenges key claim in Indonesian corruption trial. Google’s investment in Indonesia’s ride-hailing company GoTo wasn’t in anyway connected to the country’s Education Ministry’s decision to procure Chromebooks for schools during COVID-19 pandemic, former Google executives testified in court on Monday. The testimony undercut a central allegation by prosecutors in the closely watched corruption trial of Nadiem Anwar Makarim, the co-founder of Gojek and the education minister at the time of the procurement. It took place during the transition to remote learning in schools when classrooms were forced to shut down due to the COVID-19 pandemic. Makarim, 41, was arrested in September following an investigation into the procurement of Chromebook laptops that prosecutors say caused $125 million in state losses. Scott Beaumont, former president of Google Asia Pacific in 2019-2014, Caesar Sengupta, former general manager and vice president in 2018-2021, and William Florence, a former executive, testified at Jakarta’s Corruption Court on Monday via Zoom. ",
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
    
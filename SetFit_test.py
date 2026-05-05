import os
from setfit import SetFitModel

MODEL_PATH = "setfit_bias_mpnet_v1"

# None so can load it cleanly later
model = None

reverse_map = {
    0: "Left",
    1: "Center",
    2: "Right"
}

def load_model(path=MODEL_PATH):
    """
    Loads the model into memory. 
    Call this ONCE when your web app starts up up to avoid memory leaks.
    """
    global model
    if not os.path.exists(path):
        raise FileNotFoundError(f"Error: Model folder '{path}' not found. Please train the model first.")
    
    print("Loading local bias detection model...")
    model = SetFitModel.from_pretrained(path)
    return model

def predict_bias(text):
    """
    Takes a news string, predicts the bias, and returns a sorted dictionary 
    of all labels and their exact confidence percentages.
    """
    global model # Make sure it uses the global model variable!!!
    if model is None:
        load_model()
    raw_probs = model.predict_proba([text])
    probs_list = raw_probs.flatten().tolist()
    breakdown = {}
    for idx, probability in enumerate(probs_list):
        label = reverse_map[idx]
        breakdown[label] = probability
        
    sorted_breakdown = dict(sorted(breakdown.items(), key=lambda item: item[1], reverse=True))
    
    top_label = list(sorted_breakdown.keys())[0]
    return top_label, sorted_breakdown

def analyze_file(filepath):
    """
    Reads a standard text file (.txt) and analyzes its contents.
    Returns the top label, the breakdown dictionary, and the extracted text.
    """
    if not os.path.exists(filepath):
        return None, None, f"Error: File '{filepath}' not found."
        
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read().strip()
            
        if not text:
            return None, None, "Error: File is empty."
            
        top_label, breakdown = predict_bias(text)
        return top_label, breakdown, text
        
    except Exception as e:
        return None, None, f"Error reading file: {str(e)}"

# ==========================================
# LOCAL CLI & TESTING INTERFACE
# ==========================================
# This block ONLY runs if executed directly in the terminal.
# IGNORE THIS FOR WEB DEVELOPMENT

if __name__ == "__main__":
    try:
        load_model()
    except FileNotFoundError as e:
        print(e)
        exit()

# --- HARDCODED TEST CASES ---
    test_articles = [
        "Google testimony challenges key claim in Indonesian corruption trial. Google’s investment in Indonesia’s ride-hailing company GoTo wasn’t in anyway connected to the country’s Education Ministry’s decision to procure Chromebooks for schools during COVID-19 pandemic, former Google executives testified in court on Monday. The testimony undercut a central allegation by prosecutors in the closely watched corruption trial of Nadiem Anwar Makarim, the co-founder of Gojek and the education minister at the time of the procurement. It took place during the transition to remote learning in schools when classrooms were forced to shut down due to the COVID-19 pandemic. Makarim, 41, was arrested in September following an investigation into the procurement of Chromebook laptops that prosecutors say caused $125 million in state losses. Scott Beaumont, former president of Google Asia Pacific in 2019-2014, Caesar Sengupta, former general manager and vice president in 2018-2021, and William Florence, a former executive, testified at Jakarta’s Corruption Court on Monday via Zoom."
    ]

    print("\n" + "="*50)
    print("NEWS BIAS TEST RESULTS")
    print("="*50)

    for article in test_articles:
        label, breakdown = predict_bias(article)
        top_score = breakdown[label]
        
        print(f"\nArticle: \"{article[:70]}...\"")
        print(f"Result:  **{label}**")
        print(f"Confidence: {top_score:.4f}")

    print("\n" + "="*50)

    # --- INTERACTIVE TERMINAL ---
    while True:
        print("\nOptions:")
        print("1. Enter text directly")
        print("2. Analyze a text file (e.g., article.txt)")
        print("3. Quit ('q')")
        
        choice = input("\nSelect an option (1-3): ").strip().lower()
        
        if choice in ['3', 'q', 'quit', 'exit']:
            print("Shutting down...")
            break
            
        elif choice == '1':
            user_input = input("\nEnter news text to analyze: ")
            
            top_label, breakdown = predict_bias(user_input)
            
            print(f"\nPrimary Classification: **{top_label}**")
            print("Full Breakdown:")
            for category, percentage in breakdown.items():
                print(f"   - {category}: {percentage:.2%}")
                
        elif choice == '2':
            filepath = input("\nEnter the full file path: ").strip()
            filepath = filepath.strip("\"'") 
            
            top_label, breakdown, content = analyze_file(filepath)
            
            if top_label: 
                print(f"\nFile read successfully ({len(content)} characters extracted)")
                print(f"Primary Classification: **{top_label}**")
                print("Full Breakdown:")
                for category, percentage in breakdown.items():
                    print(f"   - {category}: {percentage:.2%}")
            else: 
                print(f"\nFailure to comply... {content}")
                
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
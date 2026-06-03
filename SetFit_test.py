import os
import string
from setfit import SetFitModel

MODEL_PATH = "setfit_bias_mpnet_v1"

# None so can load it cleanly later
model = None

reverse_map = {
    0: "Left",
    1: "Lean Left",
    2: "Center",
    3: "Lean Right",
    4: "Right"
}

FORWARD_MAP = {v: k for k, v in reverse_map.items()}

# Common words to ignore when looking for influential keywords
STOP_WORDS = {
    "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for", "with", "by", 
    "of", "from", "is", "was", "were", "be", "been", "being", "it", "this", "that", "to",
    "has", "have", "had", "he", "she", "they", "we", "i", "who", "which", "as", "at", "are"
}

def load_model(path=MODEL_PATH):
    """Loads the model into memory once."""
    global model
    if not os.path.exists(path):
        raise FileNotFoundError(f"Error: Model folder '{path}' not found. Please train the model first.")
    
    print("Loading local bias detection model...")
    model = SetFitModel.from_pretrained(path)
    return model

def predict_bias(text, extract_keywords=True):
    """
    Takes a news string, predicts the bias, returns a sorted dictionary 
    of all labels, and extracts the top keywords driving that choice.
    """
    global model
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
    
    top_keywords = []
    
    # --- KEYWORD EXTRACTION LOGIC (OCCLUSION) ---
    if extract_keywords:
        target_idx = FORWARD_MAP[top_label]
        baseline_score = sorted_breakdown[top_label]
        
        raw_words = text.split()
        
        unique_words = set()
        for w in raw_words:
            cleaned = w.strip(string.punctuation).lower()
            if cleaned and cleaned not in STOP_WORDS and len(cleaned) > 2:
                unique_words.add(cleaned)
        
        word_impacts = []
        
        # Temporarily drop each word to see how much the model's confidence drops
        for word in unique_words:
            altered_words = [w for w in raw_words if w.strip(string.punctuation).lower() != word]
            altered_text = " ".join(altered_words)
            
            if altered_text.strip():
                alt_probs = model.predict_proba([altered_text]).flatten().tolist()
                alt_score = alt_probs[target_idx]
                
                impact = baseline_score - alt_score
                if impact > 0.0005: 
                    word_impacts.append((word, impact, top_label))
        
        word_impacts.sort(key=lambda x: x[1], reverse=True)
        top_keywords = word_impacts[:5]  # Keep top 5
        
    return top_label, sorted_breakdown, top_keywords

def analyze_file(filepath):
    """Reads a standard text file and analyzes its contents."""
    if not os.path.exists(filepath):
        return None, None, None, f"Error: File '{filepath}' not found."
        
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read().strip()
            
        if not text:
            return None, None, None, "Error: File is empty."
            
        top_label, breakdown, keywords = predict_bias(text)
        return top_label, breakdown, keywords, text
        
    except Exception as e:
        return None, None, None, f"Error reading file: {str(e)}"


# ==========================================
# LOCAL CLI & TESTING INTERFACE
# ==========================================
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
        label, breakdown, keywords = predict_bias(article)
        top_score = breakdown[label]
        
        print(f"\nArticle: \"{article[:70]}...\"")
        print(f"Result:  **{label}**")
        print(f"Confidence: {top_score:.4f}")
        if keywords:
            # Updated to clearly show target leaning label per keyword
            print(f"Top Influential Keywords: {', '.join([f'{k[0]} ({k[2]})' for k in keywords])}")

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
            
            top_label, breakdown, keywords = predict_bias(user_input)
            
            print(f"\nPrimary Classification: **{top_label}**")
            print("Full Breakdown:")
            for category, percentage in breakdown.items():
                print(f"   - {category}: {percentage:.2%}")
                
            if keywords:
                print("\nTop Driver Keywords (Bias Influence):")
                for word, impact, target_leaning in keywords:
                    # Clearer descriptive format printout
                    print(f"   - '{word}': Adds +{impact:.2%} confidence toward **{target_leaning}**")
                
        elif choice == '2':
            filepath = input("\nEnter the full file path: ").strip()
            filepath = filepath.strip("\"'") 
            
            top_label, breakdown, keywords, content = analyze_file(filepath)
            
            if top_label: 
                print(f"\nFile read successfully ({len(content)} characters extracted)")
                print(f"Primary Classification: **{top_label}**")
                print("Full Breakdown:")
                for category, percentage in breakdown.items():
                    print(f"   - {category}: {percentage:.2%}")
                    
                if keywords:
                    print("\nTop Driver Keywords (Bias Influence):")
                    for word, impact, target_leaning in keywords:
                        print(f"   - '{word}': Adds +{impact:.2%} confidence toward **{target_leaning}**")
            else: 
                print(f"\nFailure to comply... {content}")
                
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
import os
import string
import numpy as np
from sentence_transformers import SentenceTransformer

# --- AVAILABLE MODELS ---
AVAILABLE_MODELS = {
    "1": "all-mpnet-base-v2",     
    "2": "BAAI/bge-base-en-v1.5",  
    "3": "all-MiniLM-L6-v2"         
}

CURRENT_MODEL_NAME = "all-mpnet-base-v2"
model = None

# --- KNOWLEDGE BASE ---
#REMEMBER to change this into the vector database for the full release!!!
KNOWLEDGE_BASE = [
    {
        "id": "left_ref_1",
        "leaning": "Left",
        "text": "Universal healthcare access, corporate regulations, climate justice initiatives, and systemic inequality reduction programs."
    },
    {
        "id": "left_ref_2",
        "leaning": "Left",
        "text": "Labor union protections, progressive taxation models, green energy transitions, and expanding social safety nets."
    },
    {
        "id": "center_ref_1",
        "leaning": "Center",
        "text": "Bipartisan compromise, market-stabilizing fiscal policies, incremental institutional reform, and objective data-driven governance."
    },
    {
        "id": "right_ref_1",
        "leaning": "Right",
        "text": "Free-market deregulation, federal spending cuts, individual liberty protections, and robust traditional constitutional interpretations."
    },
    {
        "id": "right_ref_2",
        "leaning": "Right",
        "text": "Border security reinforcement, corporate tax incentives, small government overreach resistance, and national sovereignty preservation."
    }
]

STOP_WORDS = {
    "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for", "with", "by", 
    "of", "from", "is", "was", "were", "be", "been", "being", "it", "this", "that",
    "has", "have", "had", "he", "she", "they", "we", "i", "who", "which", "as", "are"
}

def load_rag_model(force_reload=False):
    """Loads the embedding model into memory, reloading if the model swapped."""
    global model, CURRENT_MODEL_NAME
    if model is None or force_reload:
        print(f"\nLoading RAG Embedding Model ({CURRENT_MODEL_NAME})...")
        model = SentenceTransformer(CURRENT_MODEL_NAME)
    return model

def cosine_similarity(v1, v2):
    """Computes cosine similarity between two vectors."""
    dot_prod = np.dot(v1, v2)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    return float(dot_prod / (norm_v1 * norm_v2)) if norm_v1 and norm_v2 else 0.0

def analyze_bias_rag(input_text):
    """
    RAG Pipeline matching input text against our political reference core.
    """
    encoder = load_rag_model()
    input_embedding = encoder.encode(input_text)
    
    scored_sources = []
    for doc in KNOWLEDGE_BASE:
        doc_embedding = encoder.encode(doc["text"])
        similarity = cosine_similarity(input_embedding, doc_embedding)
        scored_sources.append({
            "id": doc["id"],
            "leaning": doc["leaning"],
            "text": doc["text"],
            "base_similarity": similarity
        })
        
    scored_sources.sort(key=lambda x: x["base_similarity"], reverse=True)
    top_source = scored_sources[0]
    
    leaning_scores = {"Left": 0.0, "Center": 0.0, "Right": 0.0}
    for src in scored_sources:
        leaning_scores[src["leaning"]] += max(0.0, src["base_similarity"])
        
    total_score = sum(leaning_scores.values())
    if total_score > 0:
        breakdown = {k: v / total_score for k, v in leaning_scores.items()}
    else:
        breakdown = {k: 0.33 for k in leaning_scores.keys()}
        
    sorted_breakdown = dict(sorted(breakdown.items(), key=lambda item: item[1], reverse=True))
    predicted_leaning = top_source["leaning"]
    
    # --- KEYWORD ATTRIBUTION LOGIC ---
    source_words = top_source["text"].split()
    unique_words = set()
    for w in source_words:
        cleaned = w.strip(string.punctuation).lower()
        if cleaned and cleaned not in STOP_WORDS and len(cleaned) > 2:
            unique_words.add(cleaned)
            
    keyword_attributions = []
    baseline_similarity = top_source["base_similarity"]
    
    for word in unique_words:
        altered_words = [w for w in source_words if w.strip(string.punctuation).lower() != word]
        altered_text = " ".join(altered_words)
        
        if altered_text.strip():
            alt_doc_embedding = encoder.encode(altered_text)
            alt_similarity = cosine_similarity(input_embedding, alt_doc_embedding)
            
            impact = baseline_similarity - alt_similarity
            if impact > 0.0001:
                keyword_attributions.append((word, impact, predicted_leaning, top_source["id"]))
                
    keyword_attributions.sort(key=lambda x: x[1], reverse=True)
    
    return predicted_leaning, sorted_breakdown, keyword_attributions[:5], top_source

def get_multiline_input():
    """Helper function to allow clean pasting of full, multi-line articles."""
    print("\nPaste/type your article below. Type 'DONE' on a new line and press Enter:")
    print("-" * 70)
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "DONE":
            break
        lines.append(line)
    print("-" * 70)
    return "\n".join(lines).strip()


# ==========================================
# CLI RUNNER INTERFACE
# ==========================================
if __name__ == "__main__":
    load_rag_model()
    
    while True:
        print("\n" + "="*40)
        print(f"CURRENT MODEL: {CURRENT_MODEL_NAME}")
        print("="*40)
        print("1. Enter / Paste a custom article")
        print("2. Run a hardcoded quick test")
        print("3. Swap Embedding Model")
        print("4. Quit ('q')")
        
        choice = input("\nSelect an option (1-4): ").strip().lower()
        
        if choice in ['4', 'q', 'quit', 'exit']:
            print("Shutting down RAG framework...")
            break
            
        elif choice == '1':
            user_input = get_multiline_input()
            
            if not user_input:
                print("Input was empty. Returning to menu.")
                continue
                
            leaning, breakdown, keywords, source = analyze_bias_rag(user_input)
            
            print(f"\nPredicted Leaning Alignment: **{leaning}**")
            print("RAG Vector Space Breakdown:")
            for alignment, percentage in breakdown.items():
                print(f"   - {alignment}: {percentage:.2%}")
                
            print(f"\nTop Retrieved Context Source: [{source['id']}] (Leaning: {source['leaning']})")
            
            if keywords:
                print("\nKeyword Source Attribution:")
                for word, impact, target_leaning, src_id in keywords:
                    print(f"   - Keyword '{word}' in source [{src_id}] adds +{impact * 100:.2f}% alignment toward **{target_leaning}**")
                    
        elif choice == '2':
            test_query = "We need stricter corporate tax regulations and expanding social safety nets immediately."
            print(f"\nRunning quick test with: \"{test_query}\"")
            
            leaning, breakdown, keywords, source = analyze_bias_rag(test_query)
            print(f"Predicted Alignment: **{leaning}**")
            print("Breakdown:")
            for alignment, percentage in breakdown.items():
                print(f"   - {alignment}: {percentage:.2%}")
                
        elif choice == '3':
            # --- SWAP MODEL LOGIC ---
            print("\nAvailable Models:")
            for key, name in AVAILABLE_MODELS.items():
                marker = " (Active)" if name == CURRENT_MODEL_NAME else ""
                print(f"   {key}. {name}{marker}")
                
            model_choice = input(f"\nSelect a model (1-{len(AVAILABLE_MODELS)}): ").strip()
            
            if model_choice in AVAILABLE_MODELS:
                new_model = AVAILABLE_MODELS[model_choice]
                if new_model != CURRENT_MODEL_NAME:
                    CURRENT_MODEL_NAME = new_model
                    model = None # Destroys the old model so the next query loads the new one
                    print(f"\nModel successfully swapped to '{CURRENT_MODEL_NAME}'.")
                    print("   (It will be loaded into memory on your next query).")
                else:
                    print("\nThat model is already active.")
            else:
                print("\nInvalid choice. Model not swapped.")
                
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")
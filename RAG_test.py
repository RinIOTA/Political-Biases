from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def build_classifier(model_name="phi3"):
    """Initializes the local LLM with a strict prompt."""
    
    llm = Ollama(model=model_name, temperature=0.0)

    template = """You are a strict data classification algorithm.
    Determine the political bias of the following text.
    
    Rules:
    1. You must respond with EXACTLY ONE WORD.
    2. The word MUST be one of the following: Left, Right, Center.
    3. Do not include any punctuation, explanations, or introductory text.
    
    Text: {article}
    
    Classification:"""

    prompt = ChatPromptTemplate.from_template(template)
    
    # Return the assembled chain
    return prompt | llm | StrOutputParser()

def predict_bias(classifier_chain, text):
    """Takes an article string and returns a clean label."""
    
    raw_response = classifier_chain.invoke({"article": text})
    
    clean_label = raw_response.strip().capitalize()
    
    if clean_label in ["Left", "Right", "Center"]:
        return clean_label
    else:
        return "Unknown" 

# ==========================================
# HOW TO USE IT
# ==========================================

if __name__ == "__main__":
    print("Loading local AI brain...")
    my_model = build_classifier("phi3") 

    # --- Test 1 ---
    article_a = "We must deregulate the energy sector to promote free market competition and lower prices for consumers."
    result_a = predict_bias(my_model, article_a)
    print(f"\nInput: {article_a}")
    print(f"Output: '{result_a}'")

    # --- Test 2 ---
    article_b = "The new policy guarantees union protections and expands social safety nets for working-class families."
    result_b = predict_bias(my_model, article_b)
    print(f"\nInput: {article_b}")
    print(f"Output: '{result_b}'")
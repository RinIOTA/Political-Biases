from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Use llama3 for better result(Note that it would require more ram, Llama3 is 8B (5GB RAM); Phi3 or TinyLlama use < 2GB RAM)
def build_classifier(model_name="phi3"):
    """Initializes the local LLM with a strict prompt."""
    
    llm = Ollama(model=model_name, temperature=0.0)

    template = """You are a strict data classification algorithm.
    Determine the political bias of the following text.
    
    Rules:
    1. You must respond with EXACTLY ONE WORD.
    2. The word MUST be one of the following: Left, Lean Left, Right, Lean Right, Center.
    3. Do not include any punctuation, explanations, or introductory text.
    
    Text: {article}
    
    Classification:"""

    prompt = ChatPromptTemplate.from_template(template)
    return prompt | llm | StrOutputParser()

def predict_bias(classifier_chain, text):
    """Takes an article string and returns a clean label."""
    raw_response = classifier_chain.invoke({"article": text})
    clean_label = raw_response.strip().capitalize()
    
    if clean_label in ["Left", "Lean Left", "Right", "Lean Right", "Center"]:
        return clean_label
    else:
        return "Unknown" 

# HOW TO USE IT

def interactive_mode(my_model):
    """Runs a continuous loop for terminal input."""
    print("\n" + "="*55)
    print("Paste your article text below and hit Enter.")
    print("Type 'q' or 'exit' at any time to shut down.")
    print("="*55)

    while True:
        user_text = input("\nEnter article: ")

        if user_text.strip().lower() in ['quit', 'exit', 'q']:
            print("\nGoodbye!")
            break

        if not user_text.strip():
            print("You didn't paste anything. Try again.")
            continue

        print("Analyzing...")
        result = predict_bias(my_model, user_text)
        
        print(f"Predicted Bias: [{result}]")

# MAIN EXECUTION

if __name__ == "__main__":
    print("Loading local AI brain...")
    
    # Initialize the model ONCE so it stays loaded in memory
    # Change "phi3" to "llama3" if your PC can handle it
    my_model = build_classifier("phi3") 
    
    # Start the infinite terminal loop
    interactive_mode(my_model)
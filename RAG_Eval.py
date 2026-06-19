import os
import string
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics import classification_report

# PATHS

DATASET_PATH = "archive\Political_Bias.csv"
TEXT_COLUMN = "Text"  
LABEL_COLUMN = "Bias"

KNOWLEDGE_BASE = [
    {
        "leaning": "Left",
        "text": (
            "Democratic socialism, systemic oppression, wealth redistribution, universal healthcare, Medicare for All, "
            "corporate greed, fossil fuel ban, Green New Deal, climate justice, systemic racism, intersectionality, "
            "unionization, billionaires tax, prison abolition, defund, anti-capitalist, historical marginalization, "
            "reproductive freedom, housing as a right, social safety net expansion, living wage, universal basic income, "
            "Social democracy, progressive policies, clean energy transition, public option healthcare, climate change action, "
            "strengthening labor unions, income inequality, corporate regulation, reproductive rights, voting rights expansion, "
            "social justice, criminal justice reform, affordable housing, infrastructure spending, tech monopoly regulation, "
            "student debt relief, minimum wage increase, diversity and inclusion initiatives, equal pay, wealth gap."
        )
    },
    {
        "leaning": "Center",
        "text": (
            "Bipartisan compromise, pragmatic governance, fiscal responsibility, market-driven solutions, moderate reform, "
            "sensible regulation, neutral data-driven decisions, non-partisan compromise, institutional stability, "
            "cross-aisle cooperation, baseline economic growth, steady incremental change, centrist consensus, national security, "
            "balanced budget, economic stability, standard judicial precedent, rule of law."
        )
    },
    {
        "leaning": "Right",
        "text": (
            "Complete free-market deregulation, federal spending cuts, robust constitutional originalism, deep state, "
            "national sovereignty preservation, border wall, strict immigration enforcement, abolishing federal agencies, "
            "woke ideology resistance, absolute gun rights, national identity, tax elimination, tariff protectionism, "
            "judicial originalism, religious freedom protections, economic nationalism, anti-globalism, "
            "Fiscal conservatism, free market principles, limited government overreach, individual liberty, regulatory relief, "
            "corporate tax cuts, economic freedom, school choice, border security, states rights, traditional values, "
            "pro-business incentives, personal responsibility, localized government control, energy independence, "
            "Second Amendment protections, spending cuts, global trade competitiveness."
        )
    }
]

MODELS_TO_EVALUATE = [
    "all-mpnet-base-v2",
    "BAAI/bge-small-en-v1.5",
    "all-MiniLM-L6-v2"
]

def cosine_similarity(v1, v2):
    dot_prod = np.dot(v1, v2)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    return float(dot_prod / (norm_v1 * norm_v2)) if norm_v1 and norm_v2 else 0.0

def load_and_sample_dataset(path, samples_per_class=100):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Error: Could not find your dataset file at '{path}'")
        
    print(f"Loading dataset from {path}...")
    df = pd.read_csv(path) if path.endswith('.csv') else pd.read_excel(path)
    
    # CASE-INSENSITIVE COLUMN MATCHING
    raw_columns = list(df.columns)
    df.columns = [str(col).strip().lower() for col in df.columns]
    
    target_text_col = TEXT_COLUMN.strip().lower()
    target_label_col = LABEL_COLUMN.strip().lower()
    
    if target_text_col not in df.columns or target_label_col not in df.columns:
        print("\nERROR: Column Name Mismatch!")
        print(f"   Looking for: '{TEXT_COLUMN}' and '{LABEL_COLUMN}'")
        print(f"   Actual columns found in your file are: {raw_columns}")
        raise KeyError("Could not find columns. Please match headers with your file.")
    
    df = df.rename(columns={target_text_col: "text", target_label_col: "bias_label"})
    df = df[["text", "bias_label"]].dropna()
    df["bias_label"] = df["bias_label"].astype(str).str.strip()

    label_mapping = {
        "left": "Left",
        "lean left": "Left",
        "center": "Center",
        "lean right": "Right",
        "right": "Right"
    }
    df["bias_label"] = df["bias_label"].apply(lambda x: label_mapping.get(x.lower(), x))
    valid_classes = {"Left", "Center", "Right"}
    df = df[df["bias_label"].isin(valid_classes)]
    
    if len(df) == 0:
        raise ValueError("Error: Zero matching rows found after collapsing labels.")

    print(f"Balancing dataset to exactly {samples_per_class} rows per class...")
    df_shuffled = df.sample(frac=1, random_state=42).reset_index(drop=True)
    
    sampled_dfs = []
    for cls in valid_classes:
        class_slice = df_shuffled[df_shuffled["bias_label"] == cls].head(samples_per_class)
        sampled_dfs.append(class_slice)
        
    df_balanced = pd.concat(sampled_dfs, ignore_index=True)
    df_balanced[TEXT_COLUMN] = df_balanced["text"]
    df_balanced[LABEL_COLUMN] = df_balanced["bias_label"]
    
    print("Evaluation Distribution:")
    print(df_balanced[LABEL_COLUMN].value_counts())

    return df_balanced.to_dict(orient="records")

def evaluate_model(model_name, dataset):
    print(f"\nRunning evaluation for: {model_name}...")
    encoder = SentenceTransformer(model_name)
    kb_embeddings = [encoder.encode(doc["text"]) for doc in KNOWLEDGE_BASE]
    y_true = []
    y_pred = []
    
    for idx, row in enumerate(dataset):
        if (idx + 1) % 50 == 0 or (idx + 1) == len(dataset):
            print(f"   Processed {idx + 1}/{len(dataset)} articles...")
        y_true.append(row[LABEL_COLUMN])
        input_embedding = encoder.encode(row[TEXT_COLUMN])
        best_similarity = -1.0
        predicted_leaning = "Center"

        for doc, kb_emb in zip(KNOWLEDGE_BASE, kb_embeddings):
            similarity = cosine_similarity(input_embedding, kb_emb)
            if similarity > best_similarity:
                best_similarity = similarity
                predicted_leaning = doc["leaning"]
                
        y_pred.append(predicted_leaning)
        
    labels_order = ["Left", "Center", "Right"]
    report = classification_report(y_true, y_pred, labels=labels_order, digits=4, zero_division=0)
    print(f"\nRAG CLASSIFICATION REPORT: {model_name}")
    print(report)

if __name__ == "__main__":
    print("="*60)
    print("RAG BENCHMARK")
    print("="*60)
    
    try:
        eval_dataset = load_and_sample_dataset(DATASET_PATH, samples_per_class=100)
        print("="*60)
        
        for model_path in MODELS_TO_EVALUATE:
            try:
                evaluate_model(model_path, eval_dataset)
                print("-" * 60)
            except Exception as e:
                print(f"Failed to evaluate {model_path}: {e}")
                
    except Exception as e:
        print(e)
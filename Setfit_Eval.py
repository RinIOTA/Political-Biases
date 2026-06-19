import os
import numpy as np
import pandas as pd
from sklearn.metrics import classification_report
from setfit import SetFitModel

# PATHS

MODEL_PATH = "setfit_bias_mpnet_v1"  
DATASET_PATH = "archive\Political_Bias.csv" 
TEXT_COLUMN = "Text"
LABEL_COLUMN = "Bias"

def load_and_clean_dataset(path, samples_per_class=100):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Error: Could not find dataset file at '{path}'")
        
    print(f"Loading dataset from {path}...")
    df = pd.read_csv(path) if path.endswith('.csv') else pd.read_excel(path)
    raw_columns = list(df.columns)
    df.columns = [str(col).strip().lower() for col in df.columns]
    target_text_col = TEXT_COLUMN.strip().lower()
    target_label_col = LABEL_COLUMN.strip().lower()
    
    if target_text_col not in df.columns or target_label_col not in df.columns:
        print("\nERROR: Column Name Mismatch!")
        print(f"   Looking for: '{TEXT_COLUMN}' and '{LABEL_COLUMN}'")
        print(f"   Actual columns found in your file are: {raw_columns}")
        raise KeyError(f"Could not find columns. Please match headers with your file.")

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
    valid_classes = ["Left", "Center", "Right"]
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
    class_to_id = {"Left": 0, "Center": 1, "Right": 2}
    df_balanced["label"] = df_balanced["bias_label"].map(class_to_id)
    df_balanced[TEXT_COLUMN] = df_balanced["text"]
    df_balanced[LABEL_COLUMN] = df_balanced["bias_label"]
    
    print("Evaluation Distribution:")
    print(df_balanced[LABEL_COLUMN].value_counts())
    
    return df_balanced

if __name__ == "__main__":
    print("="*60)
    print("      PRE-TRAINED SETFIT BENCHMARK")
    print("="*60)
    
    try:
        print(f"Loading pre-trained SetFit model from: '{MODEL_PATH}'...")
        if not os.path.exists(MODEL_PATH) and "/" not in MODEL_PATH:
            raise FileNotFoundError(f"Local model directory '{MODEL_PATH}' not found. Check your path!")
        model = SetFitModel.from_pretrained(MODEL_PATH)
        print("Model loaded successfully into memory.")
        
        df = load_and_clean_dataset(DATASET_PATH)
        print(f"Loaded {len(df)} matching rows for evaluation.")

        texts = df[TEXT_COLUMN].tolist()
        y_true = df[LABEL_COLUMN].tolist()
        
        print(f"\nRunning predictions across all {len(texts)} articles...")
        raw_preds = model.predict(texts)

        if len(raw_preds) > 0 and isinstance(raw_preds[0], (int, np.integer)):
            print("Mapping integer predictions back to class labels...")
            id_to_class = {0: "Left", 1: "Center", 2: "Right"}
            y_pred = [id_to_class.get(int(p), "Center") for p in raw_preds]
        else:
            y_pred = [str(p) for p in raw_preds]
        labels_order = ["Left", "Center", "Right"]
        report = classification_report(
            y_true, 
            y_pred, 
            labels=labels_order,
            digits=4,
            zero_division=0
        )
        print("\nPRE-TRAINED SETFIT CLASSIFICATION REPORT:")
        print(report)
        
    except Exception as e:
        print(f"Execution failed: {e}")
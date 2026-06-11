import pandas as pd
from app.services.cleaner import clean_data
from app.services.anomaly import detect_anomalies
from app.services.llm import classify_missing, generate_summary# app/services/pipeline.py
from app.services.llm import classify_missing, generate_summary

def run_pipeline(job_id, file_path):

    df = pd.read_csv(file_path)

    df = clean_data(df)
    df = detect_anomalies(df)

    df = classify_missing(df)   # LLM batch
    summary = generate_summary(df)  # LLM single

    # next step: save to DB
import requests
import os
import time

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

GEMINI_URL = (
    "https://generativelanguage.googleapis.com/v1beta/models/"
    "gemini-1.5-flash:generateContent"
)
def classify_missing(df):
    return []

def generate_summary(df):
    return {
        "total_transactions": len(df),
        "total_amount": float(df["amount"].sum())
    }
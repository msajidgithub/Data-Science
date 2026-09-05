import re
import joblib
import streamlit as st


# saved modal aur TF=IDF load karna
model = joblib.load('sentiment_model.pkl')
tfidf = joblib.load('tfidf_vectorizer.pkl')

# new function to clean the text
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

st.title("Sentiment Analysis App")

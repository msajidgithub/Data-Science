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
review = st.text_area("Enter your review here:")

if st.button("Predict Sentiment"):
    if review.strip() == '':
        st.warning("Please enter a review before predicting.")
    else:
        cleaned_review = clean_text(review)
        review_vectorized = tfidf.transform([cleaned_review])
        prediction = model.predict(  )[0]

        if prediction == 'Positive':
            st.success("The sentiment of the review is Positive.")
        else:
            st.error("The sentiment of the review is Negative.")
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()

def get_embeddings(text_chunks):
    return vectorizer.fit_transform(text_chunks).toarray()

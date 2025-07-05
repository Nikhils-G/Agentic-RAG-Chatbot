from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

vectorizer = TfidfVectorizer(max_features=384)  # fixed dimensionality

def get_embeddings(text_chunks):
    vectors = vectorizer.fit_transform(text_chunks).toarray()
    # Padding in case fewer than 384 features are found
    if vectors.shape[1] < 384:
        padded = np.zeros((vectors.shape[0], 384))
        padded[:, :vectors.shape[1]] = vectors
        return padded
    return vectors

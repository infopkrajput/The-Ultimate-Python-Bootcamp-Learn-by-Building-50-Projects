{
    "title": "The 7 Habits of Highly Effective People",
    "author": "Stephen R. Covey",
    "genre": "Self-help",
    "description": "A guide to personal and professional effectiveness through proven principles."
}

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('books.csv')

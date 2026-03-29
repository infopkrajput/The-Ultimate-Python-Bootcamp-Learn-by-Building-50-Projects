import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

df = pd.read_csv('books.csv')
df['title'] = df['title'].str.strip()
df['description'] = df['description'].str.strip()


tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['description'])

cosine_sin = cosine_similarity(tfidf_matrix, tfidf_matrix)

indices = pd.Series(df.index, index=df['title'].str.lower().str.strip()).drop_duplicates()

def get_recommendations(title, df, cosine_sin, indices):
    title = title.lower().strip()
    if title not in indices:
        return pd.DataFrame(columns=['title', 'author'])
    
    idx = indices[title]
    if isinstance(idx, pd.Series):
        idx = idx.iloc[0]
    
    sim_scores = list(enumerate(cosine_sin[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
    book_indices = [i[0] for i in sim_scores]
    return df[['title', 'author']].iloc[book_indices]

st.title('Book Recommendation System')
book_title = st.text_input('Enter a book title:')

if book_title:
    recommendations = get_recommendations(book_title, df, cosine_sin, indices)
    st.write('Recommended Books:')
    
    if isinstance(recommendations, pd.DataFrame) and not recommendations.empty:
        st.table(recommendations)
    else:
        st.write('No recommendations found.')
        
else:
    st.write('Please enter a book title.')
    
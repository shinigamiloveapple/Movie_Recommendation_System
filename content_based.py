

import pandas as pd

df = pd.read_csv("C:/Users/RYuK/Recommendation_system/clean_data.csv")

df.isna().sum()
df['overview'] = df['overview'].fillna('')

from sklearn.feature_extraction.text import TfidfVectorizer
tf = TfidfVectorizer(min_df=3, max_features=None, 
                    strip_accents='unicode', analyzer='word', token_pattern=r'\w{1,}',
                    ngram_range=(1,3), stop_words='english')

tf_vector = tf.fit_transform(df['overview'])


from sklearn.metrics.pairwise import sigmoid_kernel
sig = sigmoid_kernel(tf_vector,tf_vector)

movie_title = pd.Series(df.index, index=df['original_title']).drop_duplicates()


def recommend(title):
    
    idx = movie_title[title] # Getting the Index of the movie
    sig_score = list(enumerate(sig[idx])) # Pairwise Similarity Score of the movie
    sig_score = sorted(sig_score, key=lambda x: x[1], reverse=True) # Sorting the Similarity Score
    sig_score = sig_score[1:10] # Top 10 Similar Movies
    movies_index = [i[0] for i in sig_score] # Movies Index 
    
    return df['original_title'].iloc[movies_index] # Top 10 Similar Movies
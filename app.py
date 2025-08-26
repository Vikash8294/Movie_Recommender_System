import streamlit as st
import pandas as pd

df = pd.read_csv('merged_movie_data.csv')

user_movie_ratings = df.pivot_table(index='user_id', columns='title', values='rating')
movie_stats = df.groupby('title').agg({'rating': ['mean','count']})
movie_stats.columns = ['average_rating','ratings_count']


# computing the similarity matrix
def get_movie_recommendations(movie_title, min_ratings=100):
  # getting user rating for the target movie
  target_movie_ratings = user_movie_ratings[movie_title]
  # computing correlation with other movies
  similar_movies = user_movie_ratings.corrwith(target_movie_ratings)

  # dropping Nan and making it a dataframe
  corr_df = pd.DataFrame(similar_movies, columns=['pearson_corr'])
  corr_df.dropna(inplace=True)

  # joining with movie_stats  to add count of ratings
  corr_df = corr_df.join(movie_stats)

  # flitering the movies with enough ratings
  corr_df = corr_df[corr_df['ratings_count'] >= min_ratings]
  # sort by correlations
  return corr_df.sort_values('pearson_corr', ascending=False).head(5)

st.title('Movie Recommendation System')

movie_list = user_movie_ratings.columns.tolist()
selected_movie = st.selectbox('Select a movie you like: ', sorted(movie_list))

if st.button('Recommend'):
    recommendations = get_movie_recommendations(selected_movie)
    st.subheader(f"Top 5 Similar movies to:  '*{selected_movie}*'")
    for movie_title , row in recommendations.iterrows():
        st.write(f' **{movie_title}**  -- (Rated By: {row['ratings_count']:.0f} users)')
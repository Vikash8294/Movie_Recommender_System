# 🎬 Movie Recommender System

This is a simple *collaborative filtering* movie recommender built using the *MovieLens 100k dataset*.  
It recommends movies based on *user ratings similarity* (item-item collaborative filtering).

---

## 📂 Dataset

- *Source:* [MovieLens 100k](https://grouplens.org/datasets/movielens/100k/)
- *Files Used:* Ratings and Movie Titles

---

## 🔍 Methodology

- *Collaborative Filtering:*  
  Uses *item-item similarity* (Pearson correlation) to find movies that tend to be liked by the same users.
- *User-Item Matrix:*  
  Pivoted to have users as rows, movie titles as columns.
- *Recommendation Logic:*  
  For any input movie, finds top 5 similar movies based on correlation of user ratings.
- *Minimum Ratings Filter:*  
  Ignores movies with very few ratings to improve recommendation quality.

---

## Requirements
- pandas
- streamlit

---

## 🚀  How to Run

### 📒 Notebook
1. Open movie_recommender.ipynb in Jupyter Notebook.
2. Run all cells.
3. Call:
   python
   get_movie_recommendations('Star Wars (1977)')
     
### Streamlit
1. Make sure you have streamlit installed.
    bash
   pip install streamlit
   
2. Run:
   bash
   streamlit run app.py
   
3. Select a movie from the dropdown: click *Recommend* and see the top 5 similar movies.
   
## 📸 Output Example
Example Streamlit output for 'Star Wars (1977)'
   <img width="1905" height="954" alt="Screenshot 2025-07-11 130127" src="https://github.com/user-attachments/assets/02a4bdad-e549-47b6-95cf-f23902601f03" />

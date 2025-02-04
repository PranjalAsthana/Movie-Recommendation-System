import streamlit as st
import pickle
import requests


movies=pickle.load(open("movies_cleaned_df.pkl",'rb'))
cosine_sim=pickle.load(open("cosine_sim.pkl",'rb'))
movies_list=movies['Title'].values

st.header("Movie Recommendation System")
select_value=st.selectbox("Select movie from dropdown",movies_list)

def fetch_poster(movies_id):
    url="https://api.themoviedb.org/3/movie/157336?api_key=2a0eae0a93a6347472a910bacaf3cae3&append_to_response=videos".format(movies_id)
    data=requests.get(url)
    data=data.json()
    poster_path=data['poster_path']
    full_path="https://image.tmdb.org/t/p/w500/"+poster_path
    return full_path


def give_sim(movies_df_merge):
    index=movies[movies['Title']==movies_df_merge].index[0]
    cos_scores = sorted(list(enumerate(cosine_sim[index])), reverse=True, key=lambda vector:vector[1])
    recommend_movies=[]
    recommend_poster=[]
    for i in cos_scores[1:6]:
        movies_id=movies.iloc[i[0]].id
        recommend_movies.append(movies.iloc[i[0]].Title)
        recommend_poster.append(fetch_poster(movies_id))
    return recommend_movies,recommend_poster

if st.button("Show Recommend"):
    movie_name, movie_poster=give_sim(select_value)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1])
    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2])
    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])
    with col5:
        st.text(movie_name[4])
        st.image(movie_poster[4])
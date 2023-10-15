import streamlit as st
import pickle
import requests
def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=577296cd7e91e06113723ce9c35b493e&language=en-US'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']
def recommend(movie):
    movie_ind=movies_list1[movies_list1['title']==movie].index[0]
    dist=similarity[movie_ind]
    movie_lst=sorted(list(enumerate(dist)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movie_lst:
        movie_id=movies_list1.iloc[i[0]].movie_id
        recommended_movies.append(movies_list1.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters
movies_list1=pickle.load(open('movies.pkl','rb'))
movies_list=movies_list1['title'].values
similarity=pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommender System')
selected_movie=st.selectbox('How would you like to entertain',movies_list)
if st.button('Recommend'):
    names,posters=recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
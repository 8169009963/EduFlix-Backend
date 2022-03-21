from os import replace
import pickle
from tokenize import Name
import streamlit as st
import requests
import numpy as np 
import pandas as pd 
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

def fetch_thum(url):
    url = str(url)
    url= url.replace("https://www.youtube.com/watch?v=", "")
    url = "https://img.youtube.com/vi/{}/0.jpg".format(url)
    # full_path = requests.get(url)
    # print(url)
    return url

def recommend(video,id):
    df = pd.read_csv('dataset_eduflix.csv', encoding='unicode_escape')
    def combine_features(data):
        featues = []
        for i in range(0, data.shape[0]):
            featues.append(data['Name'][i]+ ' '+data['Subjects'][i])
        return featues
    df['combine_features']=combine_features(df)
    # df
    cm = CountVectorizer().fit_transform(df['combine_features'])

    cs = cosine_similarity(cm)
    # print(cs)

    Title = df['Name'][id]
    # Title

    Course_id= df[df.Name == Title]['SrNo'].values[0]
    # Course_id

    scores = list(enumerate(cs[Course_id]))
    # print(scores)

    sorted_scores = sorted(scores, key=lambda x:x[1], reverse=True) 
    sorted_scores = sorted_scores[1:]
    # sorted_scores


    j = 0
    # print('5 most recommented courses to '+Title+' are:\n')
    recommended_video_names = []
    recommended_video_posters = []  
    url1 = []  
    for item in sorted_scores:
        Course_title = df[df.SrNo == item[0]]['Name'].values[0]
        url = df[df.SrNo == item[0]]['Links'].values[0]
        # print(j+1, url)
        if Course_title != 0:
            print(j+1, Course_title)
            j =j+1
            url1.append(url)
            recommended_video_posters.append(fetch_thum(url))
            recommended_video_names.append(Course_title)
            if j >= 5:
                break
    # print(recommended_video_names)
    # print(recommended_video_posters)
    Course_title = recommended_video_names
    url = recommended_video_posters
    # Course_title = Course_title.remove("[''],")
    # url = url.remove("[''],")


    return Course_title,url,url1


st.header('Eduflix - Video Recommender System')
vid = pd.read_csv('dataset_eduflix.csv', encoding='unicode_escape')
# similarity = pickle.load(open('model/similarity.pkl','rb'))

movie_list = vid['Name'].values[32:95]
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

# import streamlit as st
# import streamlit.components.v1 as components

# embed streamlit docs in a streamlit app
if st.button('Show Recommendation'):
    Course_id= vid[vid.Name == selected_movie]['SrNo'].values[0]
    print(Course_id)
    Course_title,url,url1 = recommend(selected_movie,Course_id)
    # print(Course_title)
    # st.text(Course_title)
    print(url1)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(Course_title[0])
        st.image(url[0])
        st.write("[Link]({})".format(url1[0]))

    with col2:
        st.text(Course_title[1])
        st.image(url[1])
        st.write("[Link]({})".format(url1[1]))

    with col3:
        st.text(Course_title[2])
        st.image(url[2])
        st.write("[Link]({})".format(url1[2]))
    with col4:
        st.text(Course_title[3])
        st.image(url[3])
        st.write("[Link]({})".format(url1[3]))
    with col5:
        st.text(Course_title[4])
        st.image(url[4])
        st.write("[Link]({})".format(url1[4]))
st.write("Take Personality Test [Link](https://practicalpie.com/myers-briggs-type-indicator/)")
st.write("Home [Link](https://8169009963.github.io/Eduflix/index.html)")
# components.iframe("https://8169009963.github.io/Eduflix/")






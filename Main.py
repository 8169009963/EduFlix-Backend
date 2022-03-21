
import numpy as np 
import pandas as pd 
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer


df = pd.read_csv('dataset_eduflix.csv', encoding='unicode_escape', error_bad_lines=False)
def combine_features(data):
    featues = []
    for i in range(0, data.shape[0]):
        featues.append(data['Name'][i]+ ' '+data['Subjects'][i])
    return featues
df['combine_features']=combine_features(df)
df
cm = CountVectorizer().fit_transform(df['combine_features'])

cs = cosine_similarity(cm)
print(cs)

Title = df['Name'][53]
Title

Course_id= df[df.Name == Title]['SrNo'].values[0]
Course_id

scores = list(enumerate(cs[Course_id]))
print(scores)

sorted_scores = sorted(scores, key=lambda x:x[1], reverse=True) 
sorted_scores = sorted_scores[1:]
sorted_scores


j = 0
print('5 most recommented courses to '+Title+' are:\n')
for item in sorted_scores:
    Course_title = df[df.SrNo == item[0]]['Name'].values[0]
    url = df[df.SrNo == item[0]]['Links'].values[0]
    print(j+1, Course_title)
    print(j+1, url)
    j =j+1
    if j >= 5:
        break

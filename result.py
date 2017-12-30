from flask import *
import pandas as pd
from sklearn import datasets, svm, tree, preprocessing, metrics
import sklearn.ensemble as ske
import numpy as np
from sklearn.model_selection import train_test_split
from flask import Flask, redirect, url_for, request
import Recommenders

app = Flask(__name__)

@app.route("/result/<name>")
def result(name):
    triplets_file = 'https://static.turi.com/datasets/millionsong/10000.txt'
    song_df_1 = pd.read_table(triplets_file,header=None)
    song_df_1.columns = ['user_id', 'song_id', 'listen_count']
    metadata_file = 'https://static.turi.com/datasets/millionsong/song_data.csv'
    song_df_2 =  pd.read_csv(metadata_file)
    song_merged_df = pd.merge(song_df_1, song_df_2.drop_duplicates(['song_id']), on="song_id", how="left")
    song_df = song_merged_df.head(10000)
    #merge title and artist into one column called song
    pd.options.mode.chained_assignment = None  # default='warn'
    song_df['song'] = song_df['title'].map(str) + '-' + song_df['artist_name']
    song_grouped = song_df.groupby(['song']).agg({'listen_count': 'count'}).reset_index()
    lc_grouped_sum = song_grouped['listen_count'].sum()
    song_grouped['percentage']  = song_grouped['listen_count'].div(lc_grouped_sum)*100
    song_grouped.sort_values(['listen_count', 'song'], ascending = [0,1])
    users = song_df['user_id'].unique()
    songs = song_df['song_id'].unique()
    train_data, test_data = train_test_split(song_df, test_size=0.20, random_state=0)
    pr = Recommenders.popularity_recommender_py()
    pr.create(train_data, 'user_id', 'song')
    user_id = users[int(name)]
    song_table = pr.recommend(user_id)
    song_by_popularity = song_table[0:10]  

    #item-based collaborative filtering
    iscf = Recommenders.item_similarity_recommender_py()
    iscf.create(train_data, 'user_id', 'song')
    user_id = users[int(name)]
    user_items = iscf.get_user_items(user_id)

    song_table1 = iscf.recommend(user_id)
    song_by_collab = song_table1[0:10]

    return render_template('view.html',tables=[song_by_popularity.to_html(classes='song_by_popularity'), song_by_collab.to_html(classes='song_by_collab')],titles = ['na','Songs By popularity','Songs by collaborative filtering'])                       

#from UI on post it performs below function to get the user id
@app.route('/seeResult',methods = ['POST', 'GET'])
def seeResult():
   if request.method == 'POST':
      user = request.form['num']
      return redirect(url_for('result',name = user))
   else:
      user = request.args.get('num')
      return redirect(url_for('result',name = user))

if __name__ == "__main__":
    app.run()





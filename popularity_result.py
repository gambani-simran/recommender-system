from flask import *
import pandas as pd
from sklearn import datasets, svm, tree, preprocessing, metrics
import sklearn.ensemble as ske
import numpy as np
from sklearn.model_selection import train_test_split
import Recommenders

app = Flask(__name__)

@app.route("/")
def loadPopularity():
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
    user_id = users[5]
    song_table = pr.recommend(user_id)
    song_by_popularity = song_table[0:10]		
    return render_template('view.html',tables=[song_by_popularity.to_html(classes='song_by_popularity')],titles = ['na','Songs By popularity'])                       

if __name__ == "__main__":
    app.run()





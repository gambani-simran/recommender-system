from flask import *
import pandas as pd
from sklearn import datasets, svm, tree, preprocessing, metrics
import sklearn.ensemble as ske
app = Flask(__name__)

@app.route("/")
def hello():
    triplets_file = 'https://static.turi.com/datasets/millionsong/10000.txt'
    song_df_1 = pd.read_table(triplets_file,header=None)
    song_df_1.columns = ['user_id', 'song_id', 'listen_count']
    song_table = song_df_1[0:10]
    return render_template('view.html',tables=[song_table.to_html(classes='song_table')],titles = ['na','Song'])                       

if __name__ == "__main__":
    app.run()





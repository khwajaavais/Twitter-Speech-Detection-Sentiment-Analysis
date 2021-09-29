from flask import Flask, render_template, request, redirect, url_for
from joblib import load
from api_connection import get_related_tweets
import pandas as pd
pd.set_option('display.max_colwidth', 1000)

pipeline = load("text_classification.joblib")

def requestResults(name):
    tweets = get_related_tweets(name)
    tweets['prediction'] = pipeline.predict(tweets['Tweet_Text'])
    data = str(tweets.prediction.value_counts()) + '\n\n\n'
    text = '\n\nClassificaton\nClass 0 - Positive Tweet\nClass 1 - Negative Tweet\n\n' 

    d = {'Tweets': tweets.Tweet_Text, 'Prediction': tweets.prediction}

    end_text = '\n\n===================================================================@ Twitter Speech Detection - Sentiment Analysis @===================================================================\n'
#    return text+data+  'Tweets\n'+str(tweets.Tweet_Text)  +'\n\n'+ 'Prediction\n'+str(tweets.prediction)
    return text, data , pd.DataFrame(data=d), end_text
#    return text+data+'\n\n\n'+ pd.DataFrame(tweets.Tweet_Text, tweets.prediction)


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index2.html')

@app.route('/', methods=['POST', 'GET'])
def get_data():
    if request.method == 'POST':
        user = request.form['search']
        return redirect(url_for('success', name=user))

@app.route('/success/<name>')
def success(name):

    a,b,d, e = requestResults(name)
    return "<xmp>" +  str(e)  + str(a) + str(b)  + str(d) +"\n" +str(e)  + " </xmp> "

if __name__ == '__main__' :
    app.run(debug=True)
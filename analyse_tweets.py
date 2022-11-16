import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from textblob import TextBlob
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from cleantext import clean

stop_words=stopwords.words('english')
stemmer=PorterStemmer()

def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def analyseTweets(file, name):
    
    df=pd.read_csv("tweets/" + file, encoding='utf8')
    df.head()

    positive = 0
    neutral = 0
    negative = 0
    
    for index,row in df.iterrows():
        z=clean(row['Comment'], no_emoji=True)
        z=clean_tweet(z)
        z=re.sub('[^a-zA-Z]',' ',z)
        z=z.lower().split()
        z=[stemmer.stem(word) for word in z if (word not in stop_words)]
        z=' '.join(z)    
        testimonial=TextBlob(z)
        p=testimonial.sentiment.polarity
        if p==0:
            neutral = neutral+1
        elif p>0:
            positive = positive+1
        else:
            negative = negative+1

    print("Positive:{}, Neutral:{}, Negative:{}".format(positive,neutral,negative))
    
    total = positive+neutral+negative
    positive = positive/total * 100
    neutral  = neutral/total  * 100
    negative = negative/total * 100
    
    return pd.DataFrame({
        'Sentiment': ['Negative', 'Neutral', 'Positive'], 
        'Sentiment Percentage': np.around([negative, neutral, positive]),
        'Tweet Set': [name, name, name]
    })

frames = [
    analyseTweets("tweets_1589390597798125568.csv", "A (07.11.2022)"),
    analyseTweets("tweets_1590383937284870145.csv", "B (09.11.2022)"),
    analyseTweets("tweets_1590785323105423360.csv", "C (11.11.2022)"),
    analyseTweets("tweets_1591842546216763399.csv", "D (13.11.2022)"),
    analyseTweets("tweets_1592447141720780803.csv", "E (15.11.2022)")  
]

dfx = pd.concat(frames)

fig = px.bar(dfx,  
             x="Tweet Set", 
             y="Sentiment Percentage", 
             color="Sentiment", 
             title="Sentiment on Twitter", 
             text_auto=True,
             color_discrete_map={
                'Negative': '#EF553B',
                'Neutral': '#FECB52',
                'Positive': '#00CC96'
             })
fig.show()
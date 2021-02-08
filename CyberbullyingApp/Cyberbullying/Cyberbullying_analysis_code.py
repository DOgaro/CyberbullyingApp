import pandas as pd
import numpy as np
import nltk
import re
import pickle
import itertools
import joblib
from nltk.stem.wordnet import WordNetLemmatizer 
from django.conf import settings
import os

# tweet = 'Layin n bed with a headache  ughhhh...waitin on your call...'

class Cyberbullying_analysis_code():

    lem = WordNetLemmatizer()

    def cleaning(self, text):
        txt = str(text)
        txt = re.sub(r"http\S+", "", txt)
        if len(txt) == 0:
            return 'no text'
        else:
            txt = txt.split()
            index = 0
            for j in range(len(txt)):
                if txt[j][0] == '@':
                    index = j
            txt = np.delete(txt, index)
            if len(txt) == 0:
                return 'no text'
            else:
                words = txt[0]
                for k in range(len(txt)-1):
                    words+= " " + txt[k+1]
                txt = words
                txt = re.sub(r'[^\w]', ' ', txt)
                if len(txt) == 0:
                    return 'no text'
                else:
                    txt = ''.join(''.join(s)[:2] for _, s in itertools.groupby(txt))
                    txt = txt.replace("'", "")
                    txt = nltk.tokenize.word_tokenize(txt)
                    #data.content[i] = [w for w in data.content[i] if not w in stopset]
                    for j in range(len(txt)):
                        txt[j] = self.lem.lemmatize(txt[j], "v")
                    if len(txt) == 0:
                        return 'no text'
                    else:
                        return txt

    def predict_Cyberbullying(self, tweet):

        tweet_in_pandas = pd.Series(' '.join(self.cleaning(tweet)))

        path_vec = os.path.join(settings.MODELS, 'finalmodel.pkl')
        path_model = os.path.join(settings.MODELS, 'finalized_model.sav')

        # load vectorizer
        # vec_file = 'vectorizer.pickle'
        vectorizer = joblib.load(open(path_vec, 'rb'))

        # load trained model
        # filename = 'finalized_model.sav'
        model = joblib.load(open(path_model, 'rb'))




        test = joblib.transform(tweet_in_pandas)
        predicted_sentiment = model.predict(test)
        final_sentiment = (predicted_sentiment[0])
        if final_sentiment == 'Non-Bullying':
            return 'Not Bullying'
        elif final_sentiment == 'Bullying':
            return 'Bullying'

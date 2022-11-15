import pandas as pd
import gensim
from gensim.models import KeyedVectors
import numpy as np
import tqdm
import gzip
from pymagnitudelight import Magnitude

# モデルの読み込み
model_name = 'model.kv'
# model_name = 'cc.ja.300.magnitude'
model = KeyedVectors.load(model_name, mmap='r')
# model = gensim.models.KeyedVectors.load_word2vec_format(model_name,binary=True)
# model = Magnitude(model_name)

def sorayomi(atmo,input_length,a): #明るさ,長さ,単語
    def analyze(df):

        df = df.sort_values(by='length', ascending=False)    
    
        if input_length == 'ながめ':
            df = df.head(int(len(df)//3))

        if input_length == 'ふつう':
            df = df[(int(len(df)//3)):(int(len(df)//3*2))]

        if input_length == 'みじかめ':
            df = df.tail(int(len(df)//3))

        point_score= []

        for w,t in tqdm.tqdm(zip(df['words'], df['title']),total=len(df),leave=False):
            words = str(w).split(',')
            point = 0
            count = 0

            for b in words:
                try:
                    c = model.similarity(a, b)
                    c = round(c,3)
                    point += c
                    count += 1
                    if a in b:
                        point += 15
                    
                except KeyError:
                    pass

            point = point/count

            if a in t:
                point += 15

            point_score.append(point)

        df['point'] = point_score

        df = df.sort_values(by='point', ascending=False)
        drop_col = ['words','point']
        df.drop(drop_col,inplace=True,axis=1)
        df = df.head(10)

        return(df)
    
    if atmo < 10:
        atmo = 10
    else:
        pass

    atmo = (atmo//10)*10
    path = "./static/dataframe/df_" + str(atmo) + ".csv"
    usecols = ['title','author','length','words']
    df = pd.read_csv(path, usecols=usecols)
    df = analyze(df)
    author = df.iloc[0]['author']
    title = df.iloc[0]['title']
    table = df[1:].to_html()

    return(author,title,table)


import json
import numpy as np
filename="covid_tweets.csv"

def load_R_model(filename)
    with open(filename, 'r') as j:
        data_input=json.load(j)
    data={'topic_term_dists':data_input['phi'],
          'doc_topic_dists':data_input['theta'],
          'doc_lengths':data_input['doc.length'],
          'vocab':data_input['vocab'],
          'term_frequency'data_input['term.frequency']}
    return data
movies_model_data=load_R_model((''))
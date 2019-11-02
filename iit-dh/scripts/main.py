import pandas
import gensim
import pyLDAvis.gensim
import numpy as np
import pandas as pd
from pprint import pprint
from gensim.test.utils import datapath

from tokenization import preprocessed_data
from lemmatization import processed_data


df = pandas.read_json('../data/processed_iitdh_broadcast-3.json')
data = df.content.values.tolist()
tokenized_data = preprocessed_data(data)
lemmatized_data = processed_data(tokenized_data)

id2word = gensim.corpora.Dictionary(lemmatized_data)
corpus = [id2word.doc2bow(text) for text in lemmatized_data]

tfidf = gensim.models.TfidfModel(corpus)
corpus = tfidf[corpus]


def compute_coherence(corpus, k, a, b):
    lda_model = gensim.models.LdaModel(corpus=corpus,
                                       id2word=id2word,
                                       num_topics=k,
                                       random_state=100,
                                       chunksize=100,
                                       passes=10,
                                       alpha=a,
                                       eta=b,
                                       per_word_topics=True)

    coherence_model_lda = gensim.models.CoherenceModel(model=lda_model,
                                                       texts=lemmatized_data,
                                                       dictionary=id2word,
                                                       coherence='c_v')

    return coherence_model_lda.get_coherence()


def tuning():
    topics_range = range(4, 14, 2)

    alpha = list(np.arange(0.01, 1, 0.3))
    alpha.append('symmetric')
    alpha.append('asymmetric')

    beta = list(np.arange(0.01, 1, 0.3))
    beta.append('symmetric')

    corpus_sets = [corpus]
    corpus_title = [r'100% corpus']

    model_results = {'Validation_Set': [],
                     'Topics': [],
                     'Alpha': [],
                     'Beta': [],
                     'Coherence': []}

    for i in range(len(corpus_sets)):
        for k in topics_range:
            for a in alpha:
                for b in beta:
                    cv = compute_coherence(corpus=corpus_sets[i], k=k, a=a, b=b)
                    model_results['Validation_Set'].append(corpus_title[i])
                    model_results['Topics'].append(k)
                    model_results['Alpha'].append(a)
                    model_results['Beta'].append(b)
                    model_results['Coherence'].append(cv)
                    pprint(model_results)
    pd.DataFrame(model_results).to_csv('tfidf_results.csv', index=False)


model_parameters = [[10, 0.01, 0.61],
                    [12, 'symmetric', 0.91],
                    [10, 'symmetric', 0.61],
                    [12, 0.31, 0.91],
                    [12, 0.01, 0.91],
                    [8, 'symmetric', 0.91]]


for param in model_parameters:
    lda_model = gensim.models.LdaModel(corpus=corpus,
                                       id2word=id2word,
                                       num_topics=param[0],
                                       random_state=100,
                                       chunksize=100,
                                       passes=10,
                                       alpha=param[1],
                                       eta=param[2],
                                       per_word_topics=True)
    lda_model.save(datapath('iitdh_tfidf_{}_{}_{}'.format(param[0], param[1], param[2])))
    vis = pyLDAvis.gensim.prepare(lda_model, corpus, id2word)
    pyLDAvis.save_html(vis, 'iitdh_tfidf_{}_{}_{}.html'.format(param[0], param[1], param[2]))

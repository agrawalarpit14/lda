import pandas
import gensim
import pyLDAvis.gensim
from gensim.test.utils import datapath

from tokenization import preprocessed_data
from lemmatization import processed_data


df = pandas.read_json('../data/newsgroups.json')
data = df.content.values.tolist()
tokenized_data = preprocessed_data(data)

lemmatized_data = processed_data(tokenized_data)

id2word = gensim.corpora.Dictionary(lemmatized_data)
corpus = [id2word.doc2bow(text) for text in lemmatized_data]

# tfidf = gensim.models.TfidfModel(corpus)
# corpus = tfidf[corpus]

lda_model = gensim.models.LdaModel(corpus=corpus,
                                   id2word=id2word,
                                   num_topics=20,
                                   random_state=100,
                                   chunksize=100,
                                   passes=10,
                                   per_word_topics=True)

lda_model.save(datapath('20newsgroups_bow'))
vis = pyLDAvis.gensim.prepare(lda_model, corpus, id2word)
pyLDAvis.save_html(vis, '20newsgroups_bow.html')

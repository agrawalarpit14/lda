import gensim
import spacy
from stopwords import stopwords_
from nltk.corpus import stopwords


def remove_stopwords(doc, stop_words):
    """
    Removes stopwords from a document
    """
    return [word for word in doc
            if word not in stop_words]


def make_bigrams(doc, bigram_mod):
    """
    Make bigrams of a document
    """
    return bigram_mod[doc]


def lemmatization(doc, nlp):
    """
    Lemmatizes a document
    """
    doc = nlp(" ".join(doc))
    return [token.lemma_ for token in doc]


def processed_doc(doc, nlp, bigram_mod, stop_words):
    """
    Processing a document
    """
    doc = remove_stopwords(doc, stop_words)
    doc = make_bigrams(doc, bigram_mod)
    doc = lemmatization(doc, nlp)
    doc = remove_stopwords(doc, stop_words)
    return doc


def processed_data(data):
    """
    Return lemmatized data
    """
    nlp = spacy.load('en', disable=['parser', 'ner'])
    bigram = gensim.models.Phrases(data, min_count=5, threshold=100)
    bigram_mod = gensim.models.phrases.Phraser(bigram)
    stop_words = stopwords.words('english')
    stop_words.extend(stopwords_)

    return [processed_doc(doc, nlp, bigram_mod, stop_words) for doc in data]

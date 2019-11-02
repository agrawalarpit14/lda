import re
import gensim


remove_lines = []


def tokenizing(doc):
    """
    Convert a document into a list of lowercase tokens, ignoring tokens that are too short or too long.
    """
    return gensim.utils.simple_preprocess(str(doc), deacc=True, min_len=4, max_len=15)


def preprocessed_doc(doc):
    """
    Preprocessing a single document
    """
    for line in remove_lines:
        doc = doc.replace(line, '')

    doc = re.sub(r'https?\S*\s?', '', doc)
    doc = re.sub(r'\s\S*\.edu\S*\s?', ' ', doc)
    doc = re.sub(r'\s\S*\.com\S*\s?', ' ', doc)
    doc = re.sub(r'www\.\S*\s?', '', doc)
    doc = re.sub(r'\S*@\S*\s?', '', doc)
    doc = re.sub(r"\'", "", doc)
    doc = re.sub(r'\s+', ' ', doc)
    doc = tokenizing(doc)

    return doc


def preprocessed_data(data):
    """
    Preprocessing the entire data (list of documents)
    """
    return [preprocessed_doc(doc) for doc in data]

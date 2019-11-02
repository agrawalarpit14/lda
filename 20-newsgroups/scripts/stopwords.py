stopwords_ = ['that', 'from', 'this', 'have', 'with', 'subject', 'they', 'lines', 'organization',
              'what', 'will', 'there', 'would', 'about', 'writes', 'your', 'article', 'some',
              'which', 'were', 'more', 'people', 'like', 'dont', 'when', 'just', 'university',
              'posting', 'their', 'other', 'know', 'only', 'host', 'them', 'nntp', 'than', 'been',
              'think', 'also', 'does', 'time', 'then', 'good', 'these', 'well', 'should', 'could',
              'because', 'even', 'very', 'into', 'first', 'many', 'those', 'make', 'much',
              'most', 'system', 'such', 'distribution', 'right', 'where', 'world', 'want', 'here',
              'reply', 'used', 'being', 'said', 'over', 'anyone', 'after', 'same', 'need', 'work',
              'something', 'problem', 'please', 'really', 'computer', 'since', 'back', 'believe',
              'still', 'going', 'years', 'file', 'information', 'year', 'windows', 'help', 'mail',
              'using', 'state', 'find', 'take', 'question', 'last', 'point', 'thanks', 'space',
              'before', 'must', 'never', 'things', 'while', 'better', 'government', 'cant', 'might',
              'both', 'number', 'read', 'sure', 'another', 'case', 'without', 'program', 'down',
              'through', 'made', 'data', 'drive', 'software', 'long', 'available', 'part', 'under',
              'david', 'thing', 'doesnt', 'someone', 'look', 'power', 'thats', 'between', 'little',
              'version', 'come', 'didnt', 'however', 'each', 'public', 'around', 'anything', 'fact',
              'science', 'best', 'give', 'true', 'every', 'probably', 'again', 'name', 'john',
              'course', 'least', 'line', 'against', 'tell', 'seems', 'group', 'different',
              'systems', 'great', 'enough', 'high', 'research', 'news', 'list', 'hard', 'real',
              'says', 'second', 'jesus', 'possible', 'either', 'life', 'actually', 'game',
              'though', 'support', 'card', 'technology', 'post', 'center', 'called', 'free',
              'rather', 'nothing', 'access', 'next', 'team', 'chip', 'window', 'mean',
              'email', 'internet', 'problems', 'youre', '-PRON-', '_']


with open('stopwords.txt', 'r') as fp:
    for word in fp:
        stopwords_.append(word.strip())

if __name__ == '__main__':
  print(stopwords_)
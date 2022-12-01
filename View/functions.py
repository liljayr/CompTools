from pickle import APPEND
import re
import smart_open
import gensim

def clean_books(words):
    # Remove all the special characters
    words = re.sub("\'", "", words)

    # remove all single characters
    words = re.sub("[^a-zA-Z]"," ",words)

    # Remove single characters from the start
    words = re.sub('\^[a-zA-Z]\s+', ' ', words) 
    
    # Substituting multiple spaces with single space
    words = re.sub('\s+', ' ', words, flags=re.I)
    
    # Converting to Lowercase
    words = words.lower()

    return words


def listToString(s):

# initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

    # return string
    return str1



def read_corpus(fname, tokens_only=False):
    with smart_open.open(fname, encoding="iso-8859-1") as f:
        for i, line in enumerate(f):
            tokens = gensim.utils.simple_preprocess(line)
            if tokens_only:
                yield tokens
        else:
            # For training data, add tags
            yield gensim.models.doc2vec.TaggedDocument(tokens, [i])




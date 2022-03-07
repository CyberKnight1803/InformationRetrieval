import nltk 
from nltk.corpus import stopwords 
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Stop words 
STOP_WORDS = stopwords.words('english')
porter = PorterStemmer()

def lowerCaseText(s):
    """
        Returns lowercased text
    """

    assert type(s) == str, "ERROR: Strings Only!"
    return s.lower()

def tokenize(content):
    """
        Returns list of tokens 
    """

    return word_tokenize(content)

def removeStopWords(tokens, stopwords=STOP_WORDS):
    """
        Returns the filtered tokens
    """ 

    filtered_tokens = [token for token in tokens if token not in stopwords]
    return filtered_tokens

def stemming(tokens):
    stemmed_tokens = [porter.stem(token) for token in tokens]
    return stemmed_tokens

def lemmatization(tokens):
    pass 

def getCleanDocs(docs, remove_stopwords=True, normalization_type="stemming"):
    """
        Pipelined preprocessing
    """

    for docID, docContent in docs.items():
        docs[docID] = lowerCaseText(docContent)
        docs[docID] = word_tokenize(docs[docID])

    if remove_stopwords == True:
        for docID, docTokens in docs.items():
            docs[docID] = removeStopWords(docTokens)
    
    if normalization_type == "stemming":
        for docID, docTokens in docs.items():
            docs[docID] = stemming(docTokens)
    
    else:
        for docID, docTokens in docs.items():
            docs[docID] = lemmatization(docTokens)


    return docs
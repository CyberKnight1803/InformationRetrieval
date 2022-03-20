import re 
from nltk.corpus import stopwords 
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.metrics.distance import edit_distance

# Stop words 
STOP_WORDS = stopwords.words('english')
porter = PorterStemmer()

# docs = {
#   docID: {
#        "zone-1": ["token-1", "token-2", ...] 
#        "zone-2": ["token-1", "token-2", ...]
#        "zone-3": ["token-1", "token-2", ...]
#   }
# }


def lowerCaseText(docContent, zones=["title", "meta", "characters", "body"]):
    """
        Returns lowercased text
    """

    for zone in zones:
        docContent[zone] = docContent[zone].lower()

    return docContent
    

def tokenize(docContent):
    """
        Returns list of tokens 
    """
    docContent["title"] = word_tokenize(docContent["title"])
    docContent["meta"] = word_tokenize(docContent["meta"])
    docContent["characters"] = word_tokenize(docContent["characters"])
    docContent["body"] = word_tokenize(docContent["body"])
    return docContent

def removeStopWords(docContent, zones=["body"], stopwords=STOP_WORDS):
    """
        Returns the filtered tokens
    """ 
    for zone in zones:
        docContent[zone] = [token for token in docContent[zone] if token not in stopwords]

    return docContent

def removePunctuation(docContent, zones=["body"], punctuations="!\"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~"):
    """
        Returns tokens after removing punctuations
    """
    for zone in zones:
        docContent[zone] = [re.sub('[%s]' % re.escape(punctuations), '', token) for token in docContent[zone]]

    return docContent


def stemming(docContent, zones=["body"]):
    """
        Returns the stemmed version of tokens
    """

    for zone in zones:
        docContent[zone] = [porter.stem(token) for token in docContent[zone]]
    
    return zones

def lemmatization(tokens):
    """
        Returns lemmatized version of tokens
    """
    pass 

def getCleanDocs(docs, remove_stopwords=True, remove_puncuation=True, normalization_type="stemming"):
    """
        Pipelined preprocessing
    """

    for docID, docContent in docs.items():
        docs[docID] = lowerCaseText(docContent)
        docs[docID] = word_tokenize(docContent)

    if remove_stopwords:
        for docID, docContent in docs.items():
            docs[docID] = removeStopWords(docContent)
    
    if remove_puncuation:
        for docID, docContent in docs.items():
            docs[docID] = removePunctuation(docContent)

    if normalization_type == "stemming":
        for docID, docContent in docs.items():
            docs[docID] = stemming(docContent)
    
    else:
        for docID, docContent in docs.items():
            docs[docID] = lemmatization(docContent)


    return docs


def getCleanQuery():
    pass

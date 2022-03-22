import re 
from nltk.corpus import stopwords 
from nltk.stem import PorterStemmer, WordNetLemmatizer

from nltk.tokenize import word_tokenize
from nltk.metrics.distance import edit_distance

# Stop words 
STOP_WORDS = stopwords.words('english')
porter = PorterStemmer()
lemmatizer = WordNetLemmatizer()

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

def removeStopWords(docContent, zones=["title", "meta", "characters", "body"], stop_words=STOP_WORDS):
    """
        Returns the filtered tokens
    """ 
    for zone in zones:
        docContent[zone] = [token for token in docContent[zone] if token not in stop_words]

    return docContent

def removePunctuation(docContent, zones=["title", "meta", "characters", "body"], punctuations="!\"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~="):
    """
        Returns tokens after removing punctuations
    """
    for zone in zones:
        docContent[zone] = re.sub('[%s]' % re.escape(punctuations), ' ', docContent[zone])

    return docContent


def stemming(docContent, zones=["title", "meta", "characters", "body"]):
    """
        Returns the stemmed version of tokens
    """

    for zone in zones:
        docContent[zone] = [porter.stem(token) for token in docContent[zone]]
    
    return docContent

def lemmatization(docContent, zones=["title", "meta", "characters", "body"]):
    """
        Returns lemmatized version of tokens
    """
    for zone in zones:
        docContent[zone] = [lemmatizer.lemmatize(token) for token in docContent[zone]]

    return docContent

def getCleanDocs(docs, remove_stopwords=True, remove_puncuation=True, normalization_type="stemming"):
    """
        Pipelined preprocessing
    """

    if remove_puncuation:
        for docID, docContent in docs.items():
            docs[docID] = removePunctuation(docContent)

    for docID, docContent in docs.items():
        docs[docID] = lowerCaseText(docContent)
        docs[docID] = tokenize(docContent)

    if remove_stopwords:
        for docID, docContent in docs.items():
            docs[docID] = removeStopWords(docContent)

    if normalization_type == "stemming":
        for docID, docContent in docs.items():
            docs[docID] = stemming(docContent)
    
    elif normalization_type == "lemmatization":
        for docID, docContent in docs.items():
            docs[docID] = lemmatization(docContent)
        
    
    for docID, docContent in docs.items():
        if "" in docContent["title"]:
            docContent["title"].remove("")
        
        if "" in docContent["meta"]:
            docContent["meta"].remove("")
        
        if "" in docContent["characters"]:
            docContent["characters"].remove("")

        if "" in docContent["body"]:
            docContent["body"].remove("")

    return docs

def getCleanQueryToken(token, normalization_type="stemming"):
    
    token = token.lower()
    
    # TODO -> spelling correction

    if normalization_type == "stemming":
        token = porter.stem(token)
    
    else:
        token = lemmatizer.lemmatize(token)

    return token


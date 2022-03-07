from utils.posting import Posting

def createInvertedIndex(docs):
    inverted_index = {}
    for docID, docTokens in docs.items():
        for token in docTokens:
            if token in inverted_index:  
                inverted_index[token].freq += 1
                if inverted_index[token].list[-1] != docID:
                    inverted_index[token].list.append(docID)
            
            else:
                inverted_index.update({token: Posting()})
                inverted_index[token].list.append(docID)

    return inverted_index

def printInvertedIndex(inverted_index):
    """
        Prints inverted index on console for visualization!
    """
    for token, posting in inverted_index.items():
        print(f"{token}:{posting.freq}:={posting.list}")


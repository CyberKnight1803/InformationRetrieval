import os 

# docs = {
#     0: {
#         "title": "string",
#         "meta": "", 
#         "characters": "", 
#         "body": ""
#     } 
# }

def getFileNames(path_dataset):
    """
        Returns list of file-names
    """
    return os.listdir(path_dataset)

def getDocs():
    """
     Returns a dictionary with docID keys
    """

    docs = {
        
    }

    return docs

import os 

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
        0: "Hello my name is Omkar",
        1: "Omkar studies in BITS Pilani", 
        2: "Famous slang of our campus is BITS Pilani its Magic", 
        3: "Fee Hike BITS Pilani", 
        4: "BITS Pilani Hyderabad campus has the latest infrastructure"
    }

    return docs

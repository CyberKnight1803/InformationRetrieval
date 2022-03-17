class Posting:
    """
        Posting list for each token 
    """
    
    def __init__(self, zones = ["title", "meta", "characters", "body"]):
        self.freq = 1
        self.list = {
            "title": [], 
            "meta": [], 
            "characters": [], 
            "body": []
        }

    def __str__(self) -> str:
        return "Posting list for each token"



# Posting Utils  


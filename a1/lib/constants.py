import os 

PATH_DATASET = os.environ.get("PATH_DATASET", "./dataset")


dummy_zone_index = {
    "hello": {
        "title": [3, 5],
        "meta": [],
        "characters": [], 
        "body": [3, 5, 9, 11, 13]
    }, 

    "machine": {
        "title": [5, 9, 11], 
        "meta": [5, 9, 11, 14], 
        "characters": [],
        "body": [5, 9, 11, 14, 21]
    }, 
    
    "learning": {
        "title": [5, 9, 11, 15], 
        "meta": [9, 11, 17], 
        "characters": [], 
        "body": [5, 9, 11, 15, 21]
    }
}
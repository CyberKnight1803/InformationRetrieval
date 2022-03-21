from posting import Posting

# INVERTED INDEX VISUALIZATION
#
# zone_index = {
#     token: {
#         "freq": 1
#         "zone-1": [docID_1, docID_2, ....],
#         "zone-2": [docID_1, docID_2, ....]
#         ...
#     }
# }

def createZoneIndex(docs):
    """
        Constructs a zone indexing for the preprocessed docs
    """
    
    zone_index = {}

    for docID, docContent in docs.items():
        for zone in docContent.keys():
            for token in docContent[zone]:
                if token in zone_index.keys():
                    zone_index[token].freq += 1
                    if zone_index[token].list[zone][-1] != docID:
                        zone_index[token].list[zone].append(docID)
                
                else:
                    zone_index.update({token: Posting()})
                    zone_index[token].list[zone].append(docID)

    return zone_index

def printZoneIndex(zone_index):
    """
        Prints zone index on console for visualization!
    """
    print("ZONE-INDEX")

    for token, posting in zone_index.items():
        for zone in posting.list.keys():
            print("{token}.{zone:<20}{list:<10}".format(token=token, zone=zone, list=str(posting.list[zone])))
        print("\n")

def dummy_index():
    tokens = ["token_1", "token_2", "token_3"]
    zone_index = {}

    for token in tokens:
        a_post = Posting()
        a_post.list["title"] = [1, 7, 12, 13, 25]
        a_post.list["meta"] = [3, 10]
        a_post.list["characters"] = []
        a_post.list["body"] = [10, 14, 21]

        zone_index.update({token: a_post})
    
    return zone_index

if __name__=="__main__":
    printZoneIndex(dummy_index())

    
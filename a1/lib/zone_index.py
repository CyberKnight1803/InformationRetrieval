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
                    zone_index[token]["freq"] += 1
                    
                    if len(zone_index[token][zone]) == 0:
                        zone_index[token][zone].append(docID)
                        
                    elif zone_index[token][zone][-1] != docID:
                        zone_index[token][zone].append(docID)
                
                else:
                    zone_index.update({token: {
                        "freq": 1, 
                        "title": [], 
                        "meta": [], 
                        "characters": [],
                        "body": []
                    }})

                    zone_index[token][zone].append(docID)
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

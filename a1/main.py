import os 
import argparse

from utils.utils import getDocs
from utils.preprocess import getCleanDocs 

from lib.zone_index import createZoneIndex
from lib.model import BooleanModel

from lib.constants import (
    PATH_DATASET
)

def main(args):
    docs = getDocs(PATH_DATASET)
    clean_docs = getCleanDocs(docs)
    zone_index = createZoneIndex(clean_docs)

    model = BooleanModel(corpus_size=len(clean_docs), inverted_index=zone_index)

    result = model.process_query(args.query)

    print(result)


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-q", "--query", type=str, required=True, help="Enter query")
    
    args = parser.parse_args()

    main(args)



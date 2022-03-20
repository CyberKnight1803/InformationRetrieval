import os 
import argparse

from parso import parse

from lib.constants import (
    PATH_DATASET
)

def main(args):
    pass

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-q", "--query", type=str, required=True, help="Enter query")
    
    args = parser.parse_args()

    main(args)

    
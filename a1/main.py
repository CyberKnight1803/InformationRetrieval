import os 
import argparse

from parso import parse

from lib.constants import (
    PATH_DATASET
)

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    # parser.add_argument()
    args = parser.parse_args()

    print(os.listdir(PATH_DATASET))

    
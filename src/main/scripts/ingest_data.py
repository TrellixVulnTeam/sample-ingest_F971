#!/usr/bin/env python

import logging
import os


from scotia.args import get_args
from scotia.data_extracter import DataExtractor


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)


    ingest_args = get_args()
    try:
        print("test")
        extractor = DataExtractor(ingest_args)
        extractor.processExtracts()
    finally:
        print("completed")
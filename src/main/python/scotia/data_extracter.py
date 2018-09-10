import abc
import logging
import os
import pickle
import time
import json
from collections import OrderedDict
from datetime import datetime
from enum import Enum
import subprocess
import datetime, time

class DataExtractor(object):
    def __init__(self):

        logging.info('Keeping state in %s', self)


    def processExtracts(self):
        """

        """
        config = json.loads(open(r'../python/conf/extracts.json').read())
        hdfsCmd = "hdfs dfs -copyToLocal "
        edgeNodeExtractDir = config['edgeNodeExtractDir']
        print('edgeNodeExtractDir ' + edgeNodeExtractDir)

        for exts in config['extracts']:
            print('Processing ' + exts['dataSetName'] + '.' + exts['dataSetName'])
            source_dir = exts['hdfs_source_path'] + '/' + exts['partition_col'] #+ '=' + args.part
            tgt_dir = edgeNodeExtractDir + '/' + exts['dataSetName']
            print(source_dir)
            rc = subprocess.call(hdfsCmd + " " + source_dir + " " + tgt_dir, shell=True)



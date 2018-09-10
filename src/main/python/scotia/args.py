import argparse



def get_args():
    parser = argparse.ArgumentParser(description='Scotia Ingestion ')

   # parser.add_argument('consumer_type',
   #                     type=lambda consumer_type: ZendeskConsumerType[consumer_type],
   #                     choices=list(ZendeskConsumerType))
   # parser.add_argument('-a', '--account', type=str, required=True, help='API account username')
   # parser.add_argument('-t', '--token', type=str, required=True, help='API token')
   # parser.add_argument('-d', '--data_url', type=str, required=True, help='Data URL')
   # parser.add_argument('-c', '--configuration_url', type=str, required=True, help='Configuration URL')

    args = parser.parse_args()
    return args

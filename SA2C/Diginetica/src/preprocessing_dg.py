import os

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder



if __name__ == '__main__':
    data_directory = 'data'
    view = pd.read_csv(os.path.join(data_directory, 'train-item-views.csv'), sep = ';')
    purchase = pd.read_csv(os.path.join(data_directory, 'train-purchases.csv'), sep = ';')
    ### select only view data with valid user id 
    only_view = view[view['userId'].notnull()]
    # change the date to unix timestamp 
    only_view['eventdate']= pd.to_datetime(only_view['eventdate'])
    only_view['eventdate_unix'] = only_view['eventdate'].apply(lambda x: pd.Timestamp(x).timestamp())
    # drop the columns we don't need 
    only_view = only_view.copy().drop(['timeframe', 'eventdate', 'sessionId'], axis = 1)
    # mark that the customer didn't buy 
    only_view['is_buy'] = 0 
    ### select only purchase data with valid user id
    only_purchase= purchase[purchase['userId'].notnull()]
    # change the date to unix timestamp 
    only_purchase['eventdate']= pd.to_datetime(only_purchase['eventdate'])
    only_purchase['eventdate_unix'] = only_purchase['eventdate'].copy().apply(lambda x: pd.Timestamp(x).timestamp())
    # drop the columns we don't need 
    only_purchase = only_purchase.copy().drop(['timeframe', 'eventdate', 'ordernumber', 'sessionId'], axis = 1)
    only_purchase['is_buy'] = 1
    ### combine both data 
    all_event = pd.concat([only_purchase, only_view], ignore_index=True, axis=0)
    # check the data is correctly merged 
    assert(only_purchase.shape[0] + only_view.shape[0] == all_event.shape[0])

    ######## transform to ids
    item_encoder = LabelEncoder()
    user_encoder= LabelEncoder()
    all_event['itemId'] = item_encoder.fit_transform(all_event.itemId)
    all_event['userId'] = user_encoder.fit_transform(all_event.userId)

    ###########sorted by user and timestamp
    #rename column to be consistent with retail rocket dataset 
    all_event.rename(columns = {'userId':'session_id', 'itemId':'item_id', 'eventdate_unix':'timestamp'}, inplace = True)
    sorted_events = all_event.sort_values(by=['session_id', 'timestamp'])

    # save as df file 
    sorted_events.to_pickle(os.path.join(data_directory, 'diginetica_sorted_events.df'))



import sys
import pandas as pd
import ECAUGT
import time
import multiprocessing
import numpy as np

# set parameters
endpoint = "https://HCAd-Datasets.cn-beijing.ots.aliyuncs.com"
access_id = "LTAI5t7t216W9amUD1crMVos" #enter your id and keys
access_key = "ZJPlUbpLCij5qUPjbsU8GnQHm97IxJ"
instance_name = "HCAd-Datasets"
table_name = 'HCA_d'

ECAUGT.Setup_Client(endpoint, access_id, access_key, instance_name, table_name)
rows_to_get = ECAUGT.search_metadata("cell_type ==Neuron", include_children=True)

for i in range((len(rows_to_get)//10000)+1):
    st = i*10000
    ed = (i+1)*10000
    print(f'start to download cells from id {st} to {ed}')
    result = ECAUGT.get_columnsbycell_para(rows_to_get = rows_to_get[st:ed],
                                            do_transfer = True,
                                           thread_num = 95)
    print(f'saving cells from id {st} to {ed}')
    genes = result.columns[:43878]
    metaCols = result.columns[43878:43878+18]
    expr = result.loc[:,genes]
    meta = result.loc[:,metaCols]
    expr.to_csv(f"hECA_exprs_{i}.csv", index=True)
    meta.to_csv(f"hECA_metadata_{i}.csv", index=True)

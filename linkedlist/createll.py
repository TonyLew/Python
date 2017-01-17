#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Tony Lew

# Read, process and save the linked list dataset
python createll.py 

"""


import pandas as pd

column_names        = ['event_id','collector_tstamp','domain_userid','page_urlpath']
column_names_x      = ['event_idx','collector_tstampx','domain_useridx','page_urlpathx','joincol']
column_names_y      = ['event_idy','collector_tstampy','domain_useridy','page_urlpathy','joincol']
pdpv                = pd.read_csv('./pageViews.csv.gz', compression='gzip', names=column_names, sep=',', quotechar='"', error_bad_lines=False)
pdpvx               = pdpv.sort_values(["domain_userid","collector_tstamp"], ascending=[1,1])

# in cases of large files, clean up the dataframes
pdpv                = None

pdpvx['joincol']    = range(1,len(pdpvx) + 1)
pdpvy               = pdpvx.copy()
pdpvx.columns       = column_names_x
pdpvy.columns       = column_names_y

# increment the joincol of the "x" table to point to the next record
# of the "y" table
pdpvx['joincol']    = pdpvx['joincol'] + 1

# "left join" the dataframes on "joincol"
mergeresult         = pd.merge(pdpvx, pdpvy[['event_idy','domain_useridy','joincol']], on=['joincol'], how='left')

# in cases of large files, clean up the dataframes
pdpvx               = None
pdpvy               = None

# add a "next_event_id" column to the merged dataframe
mergeresult['next_event_id'] = mergeresult['event_idy'][(mergeresult['domain_useridx'] == mergeresult['domain_useridy'])]

column_names        = ['event_id','collector_tstamp','domain_userid','page_urlpath','next_event_id']
finalresult         = mergeresult[['event_idx','collector_tstampx','domain_useridx','page_urlpathx','next_event_id']]
finalresult.columns = column_names

# finally, write the dataset to file
finalresult.to_csv('./linkedlistpageViews.csv', index=False, sep=',', encoding='utf-8')



# END

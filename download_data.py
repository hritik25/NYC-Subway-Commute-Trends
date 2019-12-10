import pandas as pd
import datetime
from datetime import timedelta
import urllib.request
import os

# create a directory to download all the turnstile data
os.mkdir("turnstile_data")

# MTA has made the data public at "http://web.mta.info/developers/data/nyct/turnstile/"
 
base_url = "http://web.mta.info/developers/data/nyct/turnstile/turnstile_"
d = datetime.date(2019, 11, 16)
for i in range(104,-1,-1)[1:]: # using past two years of data (52 x 2 weeks)
    s = d.strftime('%Y%m%d')
    download_url = base_url + s[2:] + ".txt"
    urllib.request.urlretrieve(download_url, "./turnstile_data/" + s+".csv")
    d = d - timedelta(days=7)

import os

import random
import datetime as dt
import schedule
import time
import pandas as pd
import numpy as np
import tweepy as tw
from climata.snotel import StationDailyDataIO


def job():
    # Authenticate to twitter
    auth = tw.OAuthHandler('apikey','apisecret')
    auth.set_access_token('tokenkey', 'tokensecret')

    # Create API Object
    api = tw.API(auth)

    # Retrieve station daily data for Banner Summit SNOTEL
    # Calling for today's data and yesterday's to see if it snowed
    banner = StationDailyDataIO(station = '312:ID:SNTL',
                start_date = dt.date.today() - dt.timedelta(days=1),
                end_date = dt.date.today())
    print('[INFO] Banner Summit data loaded for date:',dt.date.today())
    
    # Looking through the nested loop and saving data (PRECIP)
    temp = []
    for param in banner:
        if param.element_name == 'PRECIPITATION ACCUMULATION':
            for row in param.data:
                temp.append(row.value)
            
    # Calculate the change in precip between days
    prec_diff = temp[1] - temp[0]
    print('[INFO] Precip data reformatted, dPrecip=',prec_diff)

    # Looking through the nested loop and saving data (SD)
    temp = []
    for param in banner:
        if param.element_name == 'SNOW DEPTH':
            for row in param.data:
                temp.append(row.value)

    # Calculate the change in sd between days
    snow_diff = temp[1] - temp[0]
    print('[INFO] SD data reformatted, dSD=',snow_diff)

    # Load a GIF saved locally on my machine and pass to twitter api
    snow_gif = random.choice(os.listdir('./gif/'))
    media = api.media_upload('./gif/'+ snow_gif)
    print('[INFO] GIF selected')
    
    # Prep the tweet text
    prec_diff_si = np.round((prec_diff*2.54), 2)
    tweet = f"It snowed {prec_diff_si} cm at Banner Summit on {dt.date.today()}."
    print('[INFO] Tweet written')

    # Check to make sure there was precip
    if prec_diff >= 1.0:
        # Make sure this precip was snow
        if snow_diff >= 1.0:
            # Create a tweet
            api.update_status(status=tweet, media_ids=[media.media_id])
            print('[INFO] Tweet posted!')
        else:
            print('[INFO] No substantial snowfall to report!')
    else:
        print('[INFO] No substantial snowfall to report!')

# Schedule the function once per day
schedule.every().day.at('23:55').do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

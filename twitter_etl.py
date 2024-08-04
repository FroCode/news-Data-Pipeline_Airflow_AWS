import tweepy as tw
import pandas as pd
import json
from datetime import datetime
import s3fs

access_key = "ooVUGR8NK0oFyoWZwZCZxMcxB"
access_secret = "Gcf9L1cmajm1HPYcLUv7vrMoy7ZA2BmEWu8xrdBbSvzljU2tCw"
consumer_key = "791691396826689536-ZWF7vGci8v49Y0gbs301PYk7vBt6Bd5"
cosumer_secret= "0VI2e3y9FpIscCkND123W0c5N4ZtbJOUcCRgM4pqSRryi"

aut = tw.OAuthHandler(consumer_key, cosumer_secret)
aut.set_access_token(access_key, access_secret)
api = tw.API(aut)

tweets = api.user_timeline(
    screen_name='@elonmusk', 
    count=200, 
    tweet_mode='extended'
    )
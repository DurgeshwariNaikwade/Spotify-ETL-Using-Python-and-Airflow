import spotipy.util as util
import base64
from requests import post, get
import json
import pandas as pd 
import requests
from datetime import datetime
import datetime

username = 'Your_User_name'
client_id ='Your_clientID'
client_secret = 'Your Client secret'
redirect_uri = 'http://localhost:8000/callback'
scope = 'user-read-recently-played'

token = util.prompt_for_user_token(username=username, 
                                   scope=scope, 
                                   client_id=client_id,   
                                   client_secret=client_secret,     
                                   redirect_uri=redirect_uri)


print(token)



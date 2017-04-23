from twitter import Twitter, OAuth2
import json
import keys
from tempfile import mkstemp
from shutil import move
from os import remove, close
from re import sub

##################################################################################
# Requires file keys.py to be in the same folder. Writes Twitter Bearer to keys,
# replacing the variable (variable must exist in file as program looks for word 'twitter_bearer' + anything after it (regex)
##################################################################################


# if accessing json file with values
# with open(path) as f:
#     keys = json.load(f)

CONSUMER_KEY = keys.consumer_key #keys['consumer_key'] if keys is json file
CONSUMER_SECRET = keys.consumer_secret #keys['consumer_secret'] if keys is json file

twitter = Twitter(
        auth=OAuth2(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET),
        format="",
        api_version="")

token = json.loads(twitter.oauth2.token(grant_type="client_credentials"))["access_token"]

# print(token)

def replace(file_path, pattern, subst):
    #Create temp file
    fh, abs_path = mkstemp()
    with open(abs_path,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                new_file.write(sub(pattern, subst, line))
    close(fh)
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)

replace("keys.py", "(twitter_bearer).*", "twitter_bearer = '" + str(token) + "'") #regex for twitter_bearer line

########################## PYTHON 2 CODE ##################################
# import urllib3, json, base64, certifi

# # Create a HTTP connection pool manager
# manager = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())

# # Set the variable to Twitter OAuth 2 endpoint
# oauth_url = 'https://api.twitter.com/oauth2/token' 

# credentials = CONSUMER_KEY + ':' + CONSUMER_SECRET
# # Set the HTTP request headers, including consumer key and secret
# http_headers={'Authorization': "Basic %s" % base64.b64encode(credentials.encode()).decode(), 'Content-Type': 'application/x-www-form-urlencoded'} 

# # Set the payload to the required OAuth grant type, in this case client credentials
# request_body="grant_type=client_credentials" 

# # Send the request
# response = manager.urlopen("POST", oauth_url, headers=http_headers, body=request_body)

# raw_data = response.read().decode('utf-8')

# # Read the response as JSON
# app_token = json.loads(raw_data)
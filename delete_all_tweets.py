# -*- coding: utf-8 -*-
"""
Added support for a json config file
@author: 0x7067
----------------------------------------------------------------------------
This script is forked originally from Dave Jeffery. The original implementation
was very slow and deleted around 2 tweets per second. Making it multithreaded I 
am able to delete 30-50 tweets per second. 
@author: vik-y
----------------------------------------------------------------------------
This script will delete all of the tweets in the specified account.
You may need to hit the "more" button on the bottom of your twitter profile
page every now and then as the script runs, this is due to a bug in twitter.
You will need to get a consumer key and consumer secret token to use this
script, you can do so by registering a twitter application at https://dev.twitter.com/apps
@requirements: Python 2.5+, Tweepy (http://pypi.python.org/pypi/tweepy/1.7.1)
@author: Dave Jeffery
---------------------------------------------------------
"""

import tweepy
import thread
import json

# Importing the config file

with open('config.json') as config_file:
    config = json.load(config_file)

consumer_key = config["twitter"]["consumer_key"]
consumer_secret = config["twitter"]["consumer_secret"]
access_key = config["twitter"]["access_key"]
access_secret = config["twitter"]["access_secret"]


def deleteThread(api, objectId):
    try:
        api.destroy_status(objectId)
        print "Deleted:", objectId
    except:
        print "Failed to delete:", objectId


def oauth_login(consumer_key, consumer_secret):
    """Authenticate with twitter using OAuth"""

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth_url = auth.get_authorization_url()

    verify_code = raw_input(
        "Authenticate at %s and then enter you verification code here > " % auth_url)
    auth.get_access_token(verify_code)

    return tweepy.API(auth)


def batch_delete(api):
    print "You are about to Delete all tweets from the account @%s." % api.verify_credentials().screen_name
    print "Does this sound ok? There is no undo! Type yes to carry out this action."
    do_delete = raw_input("> ")
    if do_delete.lower() == 'yes':
        for status in tweepy.Cursor(api.user_timeline).items():
            try:
                # api.destroy_status(status.id)
                # print "Deleted:", status.id
                thread.start_new_thread(deleteThread, (api, status.id, ))
            except:
                print "Failed to delete:", status.id

if __name__ == "__main__":
    # authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    print "Authenticated as: %s" % api.me().screen_name

    batch_delete(api)

# delete-tweets
A multi-threaded python script to delete all your tweets

# requirements
python 2

# quick and dirty how to
- create a twitter app in https://apps.twitter.com
- authorize your app with your twitter account (the one which you wanna delete all your tweets)
- get your keys
- clone the repository
- run $ pip install -r requirements.txt
- create a config.json file with the following template and inserting your keys:

```
{
    "twitter":{
        "consumer_key":"",
        "consumer_secret":"",
        "access_key":"",
        "access_secret":""
    }
}
```

- run the script with $ python delete_all_tweets.py

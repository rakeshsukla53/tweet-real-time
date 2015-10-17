from django.shortcuts import render
import tweepy
import json

def tweet(request):

    # Authentication details. To  obtain these visit dev.twitter.com
    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_token_secret = ''

    # This is the listener, resposible for receiving data
    class StdOutListener(tweepy.StreamListener):
        def on_data(self, data):
            # Twitter returns data in JSON format - we need to decode it first
            decoded = json.loads(data)

            # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
            print '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
            print ''
            return True

        def on_error(self, status):
            print status


    return render(request, 'index.html')




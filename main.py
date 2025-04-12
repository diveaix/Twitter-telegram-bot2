import os
import time
import requests
from flask import Flask
from threading import Thread
import telegram

# Environment variables from Render Dashboard
TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
TWITTER_BEARER_TOKEN = os.environ['TWITTER_BEARER_TOKEN']
CHAT_ID = os.environ['CHAT_ID']
USERNAMES = ['DiveAi193973', '_Artrenarts_', 'Zun2025', 'mztacat' ]

bot = telegram.Bot(token=TELEGRAM_TOKEN)

# Flask server to keep Render service alive
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_flask():
    app.run(host='0.0.0.0', port=10000)

def get_latest_tweet(username):
    headers = {'Authorization': f'Bearer {TWITTER_BEARER_TOKEN}'}
    user = requests.get(f'https://api.twitter.com/2/users/by/username/{username}', headers=headers).json()
    user_id = user['data']['id']
    tweets = requests.get(f'https://api.twitter.com/2/users/{user_id}/tweets?max_results=5', headers=headers).json()
    return tweets['data'][0]

def bot_loop():
    seen_tweets = {}
def bot_loop():
    seen_tweets = {}
    bot.send_message(chat_id=CHAT_ID, text="👋 Hello from your deployed bot!")  # <--- add here
    while True:
        for user in USERNAMES:
            ...

    while True:
        for user in USERNAMES:
            try:
                tweet = get_latest_tweet(user)
                tweet_id = tweet['id']
                if seen_tweets.get(user) != tweet_id:
                    seen_tweets[user] = tweet_id
                    tweet_url = f"https://twitter.com/{user}/status/{tweet_id}"
                    bot.send_message(chat_id=CHAT_ID, text=f"New tweet from @{user}:\n{tweet_url}")
            except Exception as e:
                print(f"Error with {user}: {e}")
        time.sleep(60)

# Start both Flask and Bot
Thread(target=run_flask).start()
Thread(target=bot_loop).start()

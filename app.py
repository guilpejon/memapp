import praw
import sys
import os
import pprint

from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Load the local source directly
sys.path.insert(1, "./python-slack-sdk")

# Enable debug logging
import logging
logging.basicConfig(level=logging.DEBUG)

from slack_sdk import WebClient

slack_token = os.environ.get("SLACK_TOKEN")
client = WebClient(token=slack_token)

reddit = praw.Reddit(
    client_id=os.environ.get("REDDIT_APP_ID"),
    client_secret=os.environ.get("REDDIT_APP_SECRET"),
    user_agent='MemeApp'
)
subreddit = reddit.subreddit("ProgrammerHumor")

for submission in subreddit.top(limit=1):
    pprint.pprint(vars(submission))
    api_response = client.chat_postMessage(
        channel="random",
        text=submission.url
    )

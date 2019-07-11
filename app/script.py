import praw
import os

reddit = praw.Reddit(user_agent='LittleBrother (by /u/kainzero)',
                     client_id=os.environ['REDDIT_ID'], client_secret=os.environ['REDDIT_SECRET'])

# client_id and client_secret are both environmental variables on my machine for security reasons.
# Feel free to import client_id and client_secret however you wish on your machines.

for submission in reddit.subreddit('learnpython').hot(limit=10):
    print(submission.title)
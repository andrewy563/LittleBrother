import praw
import os

from collections import Counter

print('connecting to reddit...')
reddit = praw.Reddit(user_agent='LittleBrother (by /u/kainzero)',
                     client_id=os.environ['REDDIT_ID'], client_secret=os.environ['REDDIT_SECRET'])
print('connected to reddit!')
# client_id and client_secret are both environmental variables on my machine for security reasons.
# Feel free to import client_id and client_secret however you wish on your machines.

def related_subreddit(subr):
    subreddit_list = []
    visited_profile = set()
    print('gathering subreddits...')
    for submission in reddit.subreddit(subr).hot(limit=10):
        if not submission.comments:
            continue
        for sub_comment in submission.comments:
            redditor = sub_comment.author
            if redditor:
                if redditor.name in visited_profile:
                    print(redditor.name)
            if redditor and redditor.name not in visited_profile:
                visited_profile.add(redditor.name)
                for comment in redditor.comments.new(limit=20):
                    if comment.subreddit.display_name != subr:
                        subreddit_list.append(comment.subreddit.display_name)
    print('converting to counter....')
    subreddit_count = Counter(subreddit_list)
    print(subreddit_count)
    print(sum(subreddit_count.values()))
    print(len(visited_profile))

if __name__=="__main__":
    related_subreddit('learnpython')
import praw
import os
import time

from collections import Counter

print('connecting to reddit...')
reddit = praw.Reddit(user_agent='LittleBrother (by /u/kainzero)',
                     client_id=os.environ['REDDIT_ID'], client_secret=os.environ['REDDIT_SECRET'])
print('connected to reddit!')
# client_id and client_secret are both environmental variables on my machine for security reasons.
# Feel free to import client_id and client_secret however you wish on your machines.

def related_subreddit(subr):
    subreddit_count = Counter()
    comment_authors = set()
    print('gathering comments')
    for submission in reddit.subreddit(subr).hot(limit=10):
        if not submission.comments:
            continue
        for sub_comment in submission.comments:
            if sub_comment.author:
                comment_authors.add(sub_comment.author)
    print('gathering subreddits')
    for redditor in comment_authors:
        for comment in redditor.comments.new(limit=50):
            if comment.subreddit.display_name != subr:
                subreddit_count[comment.subreddit.display_name] += 1
    print(subreddit_count.most_common(10))
    print(sum(subreddit_count.values()))
    print(len(comment_authors))

if __name__=="__main__":
    start = time.time()
    related_subreddit('learnpython')
    print('%s seconds' % (time.time()-start))
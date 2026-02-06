import praw
from datetime import datetime 
import pandas as pd
import re

reddit = praw.Reddit(
    client_id="AFno3KzbBM2cmp5QVa9QdQ",
    client_secret="heV2iJPCHSol_XVO0zaKgXsc9lx41w",
    user_agent="python:my_cool_app:v1.0 (by /u/YOUR_USERNAME)",
    username="Hipodominus",
    password="2zC2yCqLxWVQ3WbKz2fe"
)

# Example: Replying to a specific post
subreddit = reddit.subreddit("freelance_forhire")

data = {
        "title": [],
        'tag': [],
        "author": [],
        "score": [],
        "id": [],
        "url": [],
        "num_comments": [],
        "created_utc": [],
    }
for submission in subreddit.hot(limit=40):
    print(f"--- POST DATA ---")
    print(f"Title:     {submission.title}")
    matches = re.findall(r'\[(.*?)\]', submission.title)[0]
    print(f"Author:    u/{submission.author}")
    print(f"Score:     {submission.score}")
    print(f"ID:        {submission.id}")
    print(f"URL:       {submission.url}")
    print(f"Comments:  {submission.num_comments}")
    date_obj = datetime.fromtimestamp(submission.created_utc)
    data['title'].append(submission.title) 
    data['tag'].append(matches.upper()) 
    data['author'].append(str(submission.author)) 
    data['score'].append(submission.score) 
    data['id'].append( submission.id)
    data['url'].append(submission.url) 
    data['num_comments'].append(submission.num_comments) 
    data['created_utc'].append(submission.created_utc) 

df = pd.DataFrame.from_dict(data)
df.to_csv("reddit.csv")
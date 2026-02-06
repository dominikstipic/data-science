import praw
from datetime import datetime 

reddit = praw.Reddit(
    client_id="AFno3KzbBM2cmp5QVa9QdQ",
    client_secret="heV2iJPCHSol_XVO0zaKgXsc9lx41w",
    user_agent="python:my_cool_app:v1.0 (by /u/YOUR_USERNAME)",
    username="Hipodominus",
    password="2zC2yCqLxWVQ3WbKz2fe"
)

recipient_name = "King-Ina-131" 
try:
    reddit.redditor(recipient_name).message(
        subject="!",
        message="Hello, I'm interested in opportunity which you described in the freelance_forhire channel. \n Could you please share more details. "
    )
    print(f"Message sent successfully to u/{recipient_name}!")
except Exception as e:
    print(f"Failed to send message: {e}")
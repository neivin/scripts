import praw

r = praw.Reddit(user_agent = "Random bot by /u/cruxae")
r.login()

def run_bot():
    subreddit = r.get_subreddit("test")
    comments = subreddit.get_comments(limit = 25)

    for comment in comments:
        
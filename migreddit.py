## Migreddit: v1.0
## Neivin Mathew 
## github.com/neivin

import praw
import sys
import time

USER_AGENT = 'Migreddit:v1.0 (by /u/fruxzak)'

old_r = praw.Reddit(USER_AGENT)
old_r.login()

print ('Fetching your old subscriptions...', end='')
old_subs = old_r.get_my_subreddits(limit = None)
print ('\t [DONE]')

print ('Exporting your subscriptions...', end='')
i = 0
subs_list = []
for sub in old_subs:
    subs_list.append(sub.display_name)
    i += 1
print ('\t [DONE]')

print ('Login to your new account: ', end='')
new_r = praw.Reddit(USER_AGENT)
new_r.login()

print ('Fetching subscriptions...', end='')
new_subs = new_r.get_my_subreddits(limit = None)
print ('\t [DONE]')


print ('Erasing subscriptions...')
print ('Unsubscribing from: ')
for sub in new_subs:
    print ('r/' + sub.display_name +' ', end='')
    new_r.get_subreddit(sub.display_name).unsubscribe()
print('')
print ('\n Finished erasing subscriptions. \n')


print ('Adding your old account\'s subscriptions...')
print ('Subscribing to: ')
for sub in subs_list:
    print ('r/' + sub + ' ', end='')
    new_r.get_subreddit(sub).subscribe()
print('')
print ('\n Finished adding subscriptions. \n')

print ('Account migration complete.')

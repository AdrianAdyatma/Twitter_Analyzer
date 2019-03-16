from dateutil import parser
import re

import credentials_var as cred

count_user = 0
count_tweet = 0
count_hashtag = 0
count_url = 0
count_mention = 0

for element in list(cred.raw_findAll):

    # TWEET DATA
    text = element['extended_tweet']['full_text'] if element['truncated'] is True else element['text']
    tweet_id = element['id_str']
    tweet_created_at = parser.parse(element['created_at'])
    quote_count = element['quote_count']
    reply_count = element['reply_count']
    retweet_count = element['retweet_count']
    favorite_count = element['favorite_count']

    # USER DATA
    user_id = element['user']['id_str']
    user_name = element['user']['name']
    user_screen_name = element['user']['screen_name']
    user_created_at = parser.parse(element['user']['created_at'])

    # HASHTAG DATA
    hashtag = re.findall(r'#\w+', text)

    # URL DATA
    url = re.findall(r'[!-\-/-~]+\.[!-\-/-~]+', text)

    # MENTION DATA
    mention = re.findall(r'@\w+', text)

    # INSERT TABLE USER
    try:
        sql = 'INSERT INTO tb_user (user_id, user_name, user_screen_name, user_created_at) VALUES (%s, %s, %s, %s)'
        val = (user_id, user_name, user_screen_name, user_created_at)
        cred.sqlCursor.execute(sql, val)
        cred.sqlDb.commit()
    except:
        print(user_id, user_screen_name, "export user to sql error")
    else:
        count_user += 1

    # INSERT TABLE TWEET
    try:
        sql = 'INSERT INTO tb_tweet (user_id, tweet_id, text, tweet_created_at, quote_count, reply_count, retweet_count, favorite_count) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
        val = (user_id, tweet_id, text, tweet_created_at, quote_count, reply_count, retweet_count, favorite_count)
        cred.sqlCursor.execute(sql, val)
        cred.sqlDb.commit()
    except:
        print(user_id, tweet_id, user_screen_name, "export tweet to sql error")
    else:
        count_tweet += 1

    # INSERT TABLE HASHTAG
    try:
        for item in hashtag:
            sql = 'INSERT INTO tb_hashtag (user_id, tweet_id, hashtag) VALUES (%s, %s, %s)'
            val = (user_id, tweet_id, item)
            cred.sqlCursor.execute(sql, val)
            cred.sqlDb.commit()
    except:
        print(user_id, tweet_id, hashtag, "export hashtag to sql error")
    else:
        for item in hashtag:
            count_hashtag += 1

    # INSERT TABLE URL
    try:
        for item in url:
            sql = 'INSERT INTO tb_url (user_id, tweet_id, url) VALUES (%s, %s, %s)'
            val = (user_id, tweet_id, item)
            cred.sqlCursor.execute(sql, val)
            cred.sqlDb.commit()
    except:
        print(user_id, tweet_id, url, "export tweet to sql error")
    else:
        for item in url:
            count_url += 1

    # INSERT TABLE MENTION
    try:
        for item in mention:
            sql = 'INSERT INTO tb_mention (user_id, tweet_id, mention) VALUES (%s, %s, %s)'
            val = (user_id, tweet_id, item)
            cred.sqlCursor.execute(sql, val)
            cred.sqlDb.commit()
    except:
        print(user_id, tweet_id, mention, "export tweet to sql error")
    else:
        for item in mention:
            count_mention += 1

print(count_user, "user", count_tweet, "tweet", count_hashtag, "hashtag", count_url, "url", count_mention, "mention")
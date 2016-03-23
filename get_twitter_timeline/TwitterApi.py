# encoding: utf-8

c_key = 'nC43UrHk0szmLyw3y7rZeduzM'
c_secret = '1LxTR2IxVBxuEXyJio5Qy6r4JvSYBUiGvhjlrp2tYUgVBtwH4v'
a_key = '711848614390173697-JBq404BWISFbyOZgTIr3VnxOAXFpbCa'
a_secret = 'F3AunhAss3NefnH1icuIA0V5zO9ASynrX1TuupfjpQXL8'

import datetime
import traceback

import MySQLdb
import twitter
from MySQLdb.cursors import DictCursor

api = twitter.Api(consumer_key=c_key,
                  consumer_secret=c_secret,
                  access_token_key=a_key,
                  access_token_secret=a_secret)


def save_user(tw_user_id=None, name=None, screen_name=None, location=None, language=None,
              description=None, profile_image_url=None, rcmd_user_ids=None, since_id=None, max_id=None):
    db = MySQLdb.connect(user="root", passwd="19940218aA", db="firends_recommend", host="localhost",
                         cursorclass=DictCursor)
    cursor = db.cursor()
    print tw_user_id
    try:
        cursor.execute(
            """INSERT INTO User(tw_user_id, name, screen_name, location, language,
               description, profile_image_url, rcmd_user_ids, since_id, max_id)
               VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
            (tw_user_id, name, screen_name, location, language, description,
             profile_image_url, rcmd_user_ids, since_id, max_id))
        db.commit()
    except Exception, e:
        exstr = traceback.format_exc()
        print exstr
        db.rollback()

    db.close


def get_users_show():
    users = api.GetFriends()

    for user in users:
        save_user(tw_user_id=user.id, name=user.name.encode('utf8'),
                  screen_name=user.screen_name.encode('utf8'), location=user.location.encode('utf8'),
                  description=user.description.encode('utf8'),
                  profile_image_url=user.profile_image_url)


def save_tweet(tw_tweet_id=None, text=None, user_id=None, created_at=None, lang=None, coordinates=None):
    db = MySQLdb.connect(user="root", passwd="19940218aA", db="firends_recommend", host="localhost",
                         cursorclass=DictCursor)
    cursor = db.cursor()
    print tw_tweet_id
    try:
        cursor.execute(
            """INSERT INTO Tweet(tw_tweet_id, text, user_id, created_at, lang, coordinates)
               VALUES (%s,%s,%s,%s,%s,%s)""",
            (tw_tweet_id, text, user_id, created_at, lang, coordinates))
        db.commit()
    except Exception, e:
        exstr = traceback.format_exc()
        print exstr
        db.rollback()

    db.close


status = api.GetUserTimeline(user_id='123780906')
date = status[0].created_at
# Not fix %z instead of +0000 with Python 2.7
date = datetime.datetime.strptime(date, "%a %b %d %H:%M:%S +0000 %Y")
n_date = date.strftime('%Y-%m-%d %H:%M:%S')

save_tweet(tw_tweet_id=12345, user_id=24, created_at=n_date)

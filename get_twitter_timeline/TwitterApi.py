# encoding: utf-8

c_key = ''
c_secret = ''
a_key = ''
a_secret = ''

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
    db = MySQLdb.connect(user="root", passwd="133433", db="firends_recommend", host="localhost",
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
    finally:
        db.close


def get_users_show():
    users = api.GetFriends()

    for user in users:
        # user = users[0]
        save_user(tw_user_id=user.id, name=user.name.encode('utf8'),
                  screen_name=user.screen_name.encode('utf8'), location=user.location.encode('utf8'),
                  description=user.description.encode('utf8'),
                  profile_image_url=user.profile_image_url)

    for user in users:
        fetch_tweets(tw_user_id=user.id)


def save_tweet(tw_tweet_id=None, text=None, user_id=None, created_at=None, lang=None, coordinates_x=None,
               coordinates_y=None):
    db = MySQLdb.connect(user="root", passwd="133433", db="firends_recommend", host="localhost",
                         cursorclass=DictCursor)
    cursor = db.cursor()
    print tw_tweet_id
    try:
        cursor.execute(
            """INSERT INTO Tweet(tw_tweet_id, text, user_id, created_at, lang, coordinates_x, coordinates_y)
               VALUES (%s,%s,%s,%s,%s,%s,%s)""",
            (tw_tweet_id, text, user_id, created_at, lang, coordinates_x, coordinates_y))
        db.commit()
    except Exception, e:
        exstr = traceback.format_exc()
        print exstr
        db.rollback()
    finally:
        db.close


def get_user(tw_user_id):
    db = MySQLdb.connect(user="root", passwd="133433", db="firends_recommend", host="localhost",
                         cursorclass=DictCursor)
    cursor = db.cursor()
    try:
        cursor.execute(
            " SELECT * FROM User WHERE tw_user_id = %s " % (tw_user_id,))
        user = cursor.fetchone()
        return user
    except Exception, e:
        exstr = traceback.format_exc()
        print exstr
        db.rollback()
    finally:
        db.close


def save_user_since_id(since_id, user_id):
    db = MySQLdb.connect(user="root", passwd="133433", db="firends_recommend", host="localhost",
                         cursorclass=DictCursor)
    cursor = db.cursor()
    try:
        cursor.execute(
            " UPDATE User SET since_id = %s WHERE user_id = %s " % (since_id, user_id))
        db.commit()
    except Exception, e:
        exstr = traceback.format_exc()
        print exstr
        db.rollback()
    finally:
        db.close


def fetch_tweets(tw_user_id):
    _tw_user_id = tw_user_id
    _user = get_user(_tw_user_id)

    _since_id = '912455436390150100'

    if _user['since_id'] is not None:
        _since_id = _user['since_id']

    print _since_id

    # 往前爬数据
    status = api.GetUserTimeline(user_id=tw_user_id, count='200', max_id=_since_id)

    try:
        for statu in status:
            _since_id = statu.id

            date = statu.created_at
            # Not fix %z instead of +0000 with Python 2.7
            date = datetime.datetime.strptime(date, "%a %b %d %H:%M:%S +0000 %Y")
            n_date = date.strftime('%Y-%m-%d %H:%M:%S')

            _coordinates_x = None
            _coordinates_y = None

            if statu.coordinates is not None:
                _coordinates_x = statu.coordinates['coordinates'][0]
                _coordinates_y = statu.coordinates['coordinates'][1]

            save_tweet(tw_tweet_id=statu.id, text=statu.text.encode('utf8'), user_id=_user['user_id'],
                       created_at=n_date, lang=_user['language'], coordinates_x=_coordinates_x,
                       coordinates_y=_coordinates_y)
    except Exception, e:
        exstr = traceback.format_exc()
        print exstr
    finally:
        print _since_id
        save_user_since_id(since_id=_since_id, user_id=_user['user_id'])


# get_users_show()

db = MySQLdb.connect(user="root", passwd="133433", db="firends_recommend", host="localhost",
                     cursorclass=DictCursor)
cursor = db.cursor()
try:
    cursor.execute(
        " SELECT * FROM User ")
    t_users = cursor.fetchall()
    for t_user in t_users:
        if t_user['since_id'] is None:
            print t_user['tw_user_id']
            fetch_tweets(t_user['tw_user_id'])

except Exception, e:
    exstr = traceback.format_exc()
    print exstr
    db.rollback()
finally:
    db.close
#
# stat = api.GetStatus(id='712821748031336448')
# print stat.coordinates['coordinates'][0]

"""
Posting content and allowing voting on it through Redis.
"""
import time

from connection import *


ONE_WEEK_IN_SECONDS = 7 * 86400
VOTE_SCORE = 432
ARTICLES_PER_PAGE = 25


def article_vote(user, article, type='up'):
    """
    Process a vote on an article
    """
    cutoff = time.time() - ONE_WEEK_IN_SECONDS

    # Checks if article is still able to be voted on
    if conn.zscore('time:', article) < cutoff:
        return

    # Break the actual article key apart to get ID
    article_id = article.partition(':')[-1]

    # Attempt to add vote to set and if it works, increment the score in the
    # zset collection and the hash representation.
    if conn.sadd('voted:' + article_id, user):
        if type == 'up':
            conn.zincrby('score:', article, VOTE_SCORE)
            conn.hincrby(article, 'votes', 1)
        else:
            conn.zincrby('score:', article, -VOTE_SCORE)
            conn.hincrby(article, 'votes', -1)


def post_article(user, title, link):
    """
    Manage posting an article
    """
    # This will create a new key if it doesn't exist and get the next ID.
    article_id = str(conn.incr('article:'))

    # Create a new voted record with an expiration in a week so we save memory
    voted = 'voted:' + article_id
    conn.sadd(voted, user)
    conn.expire(voted, ONE_WEEK_IN_SECONDS)

    now = time.time()
    article = 'article:' + article_id
    # Create a new article hash with the article information
    conn.hmset(article, {
        'title': title,
        'link': link,
        'poster': user,
        'time': now,
        'votes': 1,
    })

    # Create score and time records for easy sorting later
    conn.zadd('score:', article, now + VOTE_SCORE)
    conn.zadd('time:', article, now)

    return article_id


def get_articles(page, order='score:'):
    """
    Get a page of articles based on score or time
    """
    # This will get the proper offsets
    start = (page - 1) * ARTICLES_PER_PAGE
    end = start + ARTICLES_PER_PAGE - 1

    # We get all of the article ids from the set based on order
    ids = conn.zrevrange(order, start, end)
    # We get all of the article information for each ID
    articles = []
    for id in ids:
        article_data = conn.hgetall(id)
        article_data['id'] = id
        articles.append(article_data)

    return articles


def add_remove_groups(article_id, to_add=None, to_remove=None):
    """
    Add and remove articles from groups
    """
    if not to_add:
        to_add = []

    if not to_remove:
        to_remove = []

    article = 'article:' + article_id
    for group in to_add:
        conn.sadd('group:' + group, article)

    for group in to_remove:
        conn.srem('group:' + group, article)


def get_group_articles(group, page, order='score:'):
    """
    Get the articles for a specific group
    """
    key = order + group
    # If there is not a group ordering, create the group
    if not conn.exists(key):
        # We create a group ordering based on group articles and the master score
        conn.zinterstore(key, ['group:' + group, order], aggregate='max',)
        conn.expire(key, 60)

    return get_articles(page, key)

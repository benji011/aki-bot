import datetime
import os
import random

import requests

from discord import RequestsWebhookAdapter, Webhook

NEWS_API_KEY = os.environ['USEFUL_TREVOR_API_KEY']

BENJI = os.environ['BENJI']
ANDO = os.environ['ANDO']
DANNY = os.environ['DANNY']
DARREN = os.environ['DARREN']

DISCORD_TOKEN_ID = os.environ['DISCORD_TOKEN_ID']
DISCORD_TOKEN = os.environ['DISCORD_TOKEN']
GITHUB_LINK = "https://github.com/benji011/aki-bot/blob/master/aki_bot.py"


def get_random_inaka_boisss():
    """Get a random person to send a random article to."""
    inaka_boisss = [BENJI, ANDO, DANNY, DARREN]
    return random.choice(inaka_boisss)


def compose_msg_with_news():
    """Get random news article from the BBC."""
    domain = 'https://newsapi.org/'
    path = 'v2/top-headlines'
    args = '?sources=bbc-news&apiKey='
    url = domain + path + args + NEWS_API_KEY

    r = requests.get(url)
    response_data = r.json()
    if response_data['status'] == "ok":
        articles = response_data['articles']

        random_news_article = random.choice(articles)

        recipent = "<@{user_id}>".format(
            user_id=get_random_inaka_boisss()
        )
        greeting = "ハロー "
        message = (
            "今日のニュースはこれ「{title}」！ \n"
            "詳細はこちら {url} \n"
        ).format(
            title=random_news_article['title'],
            url=random_news_article['url']
        )
    return (
        greeting + " " +
        recipent + " ! " +
        message + "\n"
    )


def get_kitty():
    """Get a random cat gif."""
    domain = 'https://api.thecatapi.com/'
    path = 'v1/images/search'
    args = '?mime_types=gif'
    url = domain + path + args
    r = requests.get(url)
    response_data = r.json()
    if response_data:
        cat_img = response_data[0]['url']
        return cat_img


def compose_msg_with_kitty(img):
    """Send kitty."""
    recipent = "<@{user_id}>".format(
        user_id=get_random_inaka_boisss()
    )
    greeting = "ねぇねぇ。。 "
    message = (
        "かわいいでしょう？ {cat_img}"
    ).format(
        cat_img=img
    )
    return (
        greeting + " " +
        recipent + " ! " +
        message + "\n"
    )


def send_message(msg):
    """Send message."""
    webhook = Webhook.partial(
        DISCORD_TOKEN_ID,
        DISCORD_TOKEN,
        adapter=RequestsWebhookAdapter()
    )
    webhook.send(msg)


def main():
    """The main function."""
    now = datetime.datetime.now()
    day_is_even = (now.day % 2 == 0)
    msg = (
        compose_msg_with_kitty(get_kitty())
        if day_is_even else compose_msg_with_news()
    )
    github_url_msg = (
        "beep bop I'm a bot\n"
        "My source code is here - {github_link}"
    ).format(
        github_link=GITHUB_LINK
    )
    content = msg + github_url_msg
    send_message(content)


if __name__ == "__main__":
    main()

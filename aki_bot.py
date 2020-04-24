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


def get_random_inaka_boisss():
    """Get a random person to send a random article to."""
    inaka_boisss = [BENJI, ANDO, DANNY, DARREN]
    return random.choice(inaka_boisss)


def get_uncomfortable_play_name():
    """Get uncomfortable play name."""
    play_name_one = [
        "spicy",
        "salty",
        "wacky",
        "flippy flappy",
        "Mmmmmmmmmmm",
        "stale",
        "vaginal discharged"
    ]

    play_name_two = [
        "hunk",
        "spunk master",
        "potato",
        "smashy washlet",
        "banana lips",
        "sexual sausage",
        "ass cruncher"
    ]

    return "{play_name_one} {play_name_two}".format(
        play_name_one=random.choice(play_name_one),
        play_name_two=random.choice(play_name_two)
    )


def get_random_news():
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
        final_greeting = (
            "じゃまた明日 my {play_name}"
        ).format(
            play_name=get_uncomfortable_play_name()
        )
        return (
            greeting + " " +
            recipent + " ! " +
            message + "\n" +
            final_greeting
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


def send_kitty(img):
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
    final_greeting = (
        "じゃまた明日 my {play_name}"
    ).format(
        play_name=get_uncomfortable_play_name()
    )
    return (
        greeting + " " +
        recipent + " ! " +
        message + "\n" +
        final_greeting
    )


def main():
    """The main function."""
    webhook = Webhook.partial(
        DISCORD_TOKEN_ID,
        DISCORD_TOKEN,
        adapter=RequestsWebhookAdapter()
    )

    now = datetime.datetime.now()
    if (now.day % 2 == 0):
        img = get_kitty()
        msg = send_kitty(img)
    else:
        msg = get_random_news()

    webhook.send(msg)


if __name__ == "__main__":
    main()

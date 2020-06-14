import json
import logging
import os

from aiotg import Bot, Chat
from telegram import ReplyKeyboardMarkup, KeyboardButton

from photo import make_photo

logging.basicConfig(
    level=getattr(logging, os.environ.get("BOT_LOGGING_LEVEL", "DEBUG")),
    format="%(asctime)s | %(name)s | %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)
ch = logging.StreamHandler()
logger.addHandler(ch)


bot = Bot(api_token=os.environ["BOT_TOKEN"],)


def get_admins():
    return map(int, os.environ.get("BOT_ADMINS", "").split(","))


def is_authorized(sender):
    return sender["id"] in get_admins()


def get_button():
    return json.dumps(
        ReplyKeyboardMarkup(
            [[KeyboardButton(text="Photo")]],
            resize_keyboard=True,
            one_time_keyboard=True,
        ).to_dict()
    )


@bot.command("/?ping")
def ping(chat: Chat, match):
    return chat.send_text("pong")


@bot.command("/start")
def start(chat: Chat, match):
    return chat.send_text("Wellcome", reply_markup=get_button())


@bot.default
async def send_photo(chat: Chat, match):
    if is_authorized(chat.sender):
        await chat.send_chat_action("upload_photo")

        filepath, text = make_photo()
        await chat.send_photo(photo=open(filepath, "rb"), caption=text)


bot.run()

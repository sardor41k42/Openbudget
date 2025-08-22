import telebot
from telebot import types

TOKEN = "SIZNING_BOT_TOKEN"
ADMIN_ID = 6689677013

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    username = message.from_user.username
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Votega qo'shilish"))
    bot.send_message(message.chat.id, f"Salom, {username}! Open Budget botiga xush kelibsiz.", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Votega qo'shilish")
def vote(message):
    bot.send_message(message.chat.id, "Sizning ovozingiz qabul qilindi. Rahmat!")

@bot.message_handler(func=lambda message: message.from_user.id == ADMIN_ID)
def admin_message(message):
    bot.send_message(message.chat.id, "Salom admin, siz xabar yubordingiz!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, "Iltimos, menyudan tanlang.")

bot.infinity_polling()

import telebot
from telebot import types

# Bot token va admin ID
TOKEN = "7418760633:AAHI5nthgJSM817nFmTCTCQWR2rew957e54"
ADMIN_ID = 6689677013

bot = telebot.TeleBot(TOKEN)

# /start komandasi
@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Ovoz berish", "Yordam")
    bot.send_message(
        message.chat.id,
        "Salom! Men OpenBudget botman.\n\nPastdagi menyudan kerakli bo'limni tanlang.",
        reply_markup=markup
    )

# Ovoz berish tugmasi
@bot.message_handler(func=lambda message: message.text == "Ovoz berish")
def vote_menu(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Variant 1", callback_data="vote_1")
    btn2 = types.InlineKeyboardButton("Variant 2", callback_data="vote_2")
    btn3 = types.InlineKeyboardButton("Variant 3", callback_data="vote_3")
    markup.add(btn1, btn2, btn3)
    bot.send_message(
        message.chat.id,
        "Qaysi variantga ovoz berasiz?",
        reply_markup=markup
    )

# Tugmalar bosilganda ishlaydi
@bot.callback_query_handler(func=lambda call: call.data.startswith("vote_"))
def callback_vote(call):
    variant = call.data.split("_")[1]
    bot.answer_callback_query(call.id, f"Ovozingiz qabul qilindi (Variant {variant})")
    bot.send_message(call.message.chat.id, f"Rahmat! Siz Variant {variant} uchun ovoz berdingiz. ✅")

    # Admin/ga xabar yuboramiz
    bot.send_message(
        ADMIN_ID,
        f"{call.from_user.first_name} (@{call.from_user.username}) "
        f"(ID: {call.from_user.id}) Variant {variant} uchun ovoz berdi."
    )

# Yordam bo'limi
@bot.message_handler(func=lambda message: message.text == "Yordam")
def help_message(message):
    bot.send_message(
        message.chat.id,
        "Bu bot orqali Ochiq byudjet loyihalariga ovoz berishingiz mumkin.\n\n"
        "/start - Bosh menyu\n"
        "Ovoz berish - Loyiha uchun ovoz berish"
    )

# Oddiy echo xabarlar
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, f"Siz yozdingiz: {message.text}")

# Botni doimiy ishlashga tushiramiz
print("Bot ishga tushdi...")
bot.polling(none_stop=True)

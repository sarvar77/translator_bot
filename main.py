import telebot
from telebot import types
from translate import Translator
from config import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start_command(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    ru_en = types.InlineKeyboardButton("🇷🇺 RU-EN 🏴󠁧󠁢󠁥󠁮󠁧󠁿", callback_data="ru-en")
    en_ru = types.InlineKeyboardButton("🏴󠁧󠁢󠁥󠁮󠁧󠁿 EN-RU 🇷🇺", callback_data="en-ru")
    uz_ru = types.InlineKeyboardButton("🇺🇿 UZ-RU 🇷🇺", callback_data="uz-ru")
    ru_uz = types.InlineKeyboardButton("🇷🇺 RU-UZ 🇺🇿", callback_data="ru-uz")
    uz_en = types.InlineKeyboardButton("🇺🇿 UZ-EN 🏴󠁧󠁢󠁥󠁮󠁧󠁿", callback_data="uz-en")
    en_uz = types.InlineKeyboardButton("🏴󠁧󠁢󠁥󠁮󠁧󠁿 EN-UZ 🇺🇿", callback_data="en-uz")

    markup.add(ru_en)
    markup.add(en_ru, uz_ru)
    markup.add(ru_uz, uz_en, en_uz)

    name = message.from_user.first_name
    global first
    first = bot.send_message(message.chat.id, f"<b>✋ Привет, {name}\n\n"
                                              f"👇 Я могу переводить слова и предложения на языки, которые стоят внизу.\n\nЖмите на вам нужную кнопку.</b>",
                             reply_markup=markup, parse_mode="html")


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # ru-en
    def translator_1(message):
        user_text = message.text
        translated = translator.translate(user_text)
        bot.send_message(call.message.chat.id, f"<b>Ваш текст:</b> {user_text}\n\n"
                                               f"<b>Перевод:</b> {translated}", parse_mode="html")

    if call.data == "ru-en":
        translator = Translator(from_lang="ru", to_lang="en")
        bot.register_next_step_handler(first, translator_1)
        needed_text = bot.send_message(call.message.chat.id, "<b>Введите слово, которое вам нужен перевод (RU-EN)</b>",
                                       parse_mode="html")
#_______________________________________________________________________________________________________________________________

    def translator_2(message):
        user_text = message.text
        translated = translator.translate(user_text)
        bot.send_message(message.chat.id, f"<b>Ваш текст:</b> {user_text}\n\n"
                                          f"<b>Перевод:</b> {translated}", parse_mode="html")
    if call.data == "en-ru":
        translator = Translator(from_lang="en", to_lang="ru")
        bot.register_next_step_handler(first, translator_2)
        needed_text = bot.send_message(call.message.chat.id, "<b>Введите слово, которое вам нужен перевод (EN-RU)</b>",
                                       parse_mode="html")
#_______________________________________________________________________________________________________________________________

    def translator_3(message):
        user_text = message.text
        translated = translator.translate(user_text)
        bot.send_message(message.chat.id, f"<b>Ваш текст:</b> {user_text}\n\n"
                                          f"<b>Перевод:</b> {translated}", parse_mode="html")

    if call.data == "uz-ru":
        translator = Translator(from_lang="uz", to_lang="ru")
        bot.register_next_step_handler(first, translator_3)
        needed_text = bot.send_message(call.message.chat.id, "<b>Введите слово, которое вам нужен перевод (UZ-RU)</b>",
                                       parse_mode="html")
#_______________________________________________________________________________________________________________________________

    def translator_4(message):
        user_text = message.text
        translated = translator.translate(user_text)
        bot.send_message(message.chat.id, f"<b>Ваш текст:</b> {user_text}\n\n"
                                          f"<b>Перевод:</b> {translated}", parse_mode="html")

    if call.data == "ru-uz":
        translator = Translator(from_lang="ru", to_lang="uz")
        bot.register_next_step_handler(first, translator_4)
        needed_text = bot.send_message(call.message.chat.id, "<b>Введите слово, которое вам нужен перевод (RU-UZ)</b>",
                                       parse_mode="html")
#_______________________________________________________________________________________________________________________________

    def translator_5(message):
        user_text = message.text
        translated = translator.translate(user_text)
        bot.send_message(message.chat.id, f"<b>Ваш текст:</b> {user_text}\n\n"
                                          f"<b>Перевод:</b> {translated}", parse_mode="html")

    if call.data == "uz-en":
        translator = Translator(from_lang="uz", to_lang="en")
        bot.register_next_step_handler(first, translator_5)
        needed_text = bot.send_message(call.message.chat.id, "<b>Введите слово, которое вам нужен перевод (UZ-EN)</b>",
                                       parse_mode="html")
#_______________________________________________________________________________________________________________________________

    def translator_6(message):
        user_text = message.text
        translated = translator.translate(user_text)
        bot.send_message(message.chat.id, f"<b>Ваш текст:</b> {user_text}\n\n"
                                          f"<b>Перевод:</b> {translated}", parse_mode="html")

    if call.data == "en-uz":
        translator = Translator(from_lang="en", to_lang="uz")
        bot.register_next_step_handler(first, translator_6)
        needed_text = bot.send_message(call.message.chat.id, "<b>Введите слово, которое вам нужен перевод (EN-UZ)</b>",
                                       parse_mode="html")


bot.polling(none_stop=True)

# https://t.me/sarrvarr23

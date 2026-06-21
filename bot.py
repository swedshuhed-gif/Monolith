import os
import telebot

TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def update_status(message):
    # Бот берет текст сообщения и перезаписывает файл status.txt
    with open("status.txt", "w", encoding="utf-8") as f:
        f.write(message.text.upper()) # Делает капсом для стиля
    bot.reply_to(message, f"Статус изменен на: {message.text.upper()}")

if __name__ == "__main__":
    bot.infinity_polling()

import datetime
import re
from telegram import Update, ParseMode
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

chat_id = -1001195761916  # Замените на фактический ID вашего чата
duty_schedule = ['Зубакин', 'Есин', 'Леманн', 'Галиев', 'Халиуллин']
corporate_links = [
    'https://t.me/Jeddit1999',
    'https://t.me/reallee7741',
    'https://t.me/GeniusAl',
    'https://t.me/dgFisher',
    'https://t.me/drinkin1water'
]  # Замените на фактические ссылки

def current_duty(update: Update, context: CallbackContext):
    current_date = datetime.date.today()
    current_week = (current_date.day - 1) // 7  # Определение текущей недели
    current_duty_person = duty_schedule[current_week]
    current_duty_link = corporate_links[current_week]

    next_week = (current_week + 1) % len(duty_schedule)  # Определение следующей недели
    next_duty_person = duty_schedule[next_week]
    next_duty_link = corporate_links[next_week]

    chat_type = update.effective_chat.type
    if chat_type == 'private':
        update.message.reply_text(f"Дежурный на этой неделе: [{current_duty_person}]({current_duty_link})",
                                  parse_mode=ParseMode.MARKDOWN)
        update.message.reply_text(f"Дежурный на следующей неделе: [{next_duty_person}]({next_duty_link})",
                                  parse_mode=ParseMode.MARKDOWN)
    elif chat_type == 'group' or chat_type == 'supergroup':
        context.bot.send_message(chat_id=chat_id,
                                 text=f"Дежурный на этой неделе: [{current_duty_person}]({current_duty_link})",
                                 parse_mode=ParseMode.MARKDOWN)
        context.bot.send_message(chat_id=chat_id,
                                 text=f"Дежурный на следующей неделе: [{next_duty_person}]({next_duty_link})",
                                 parse_mode=ParseMode.MARKDOWN)

def handle_text_message(update: Update, context: CallbackContext):
    text = update.message.text.lower()
    if re.search(r'дежурн', text):
        current_duty(update, context)

def main():
    updater = Updater("6324485925:AAFNX1RsgwhXe8zxFbr1DcX3OMJ6MpHYWpU", use_context=True)  # Замените на фактический токен вашего бота
    dispatcher = updater.dispatcher
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

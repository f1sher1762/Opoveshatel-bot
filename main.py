import datetime
import re
from telegram import Update, ParseMode
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

chat_id = -4509208587  # настойщий айди чата
duty_schedule = ['Иванов', 'Иванов', 'Иванов', 'Иванов', 'Иванов']
corporate_links = [
    'https://t.me/Иванов',
    'https://t.me/сидоров',
    'https://t.me/петров',
    'https://t.me/Иванов',
    'https://t.me/Иванов'
]  # Замените на настоящие ссылки

def current_duty(update: Update, context: CallbackContext):
    current_date = datetime.date.today()
    current_week = (current_date.day - 1) // 7  # текущая неделя
    current_duty_person = duty_schedule[current_week]
    current_duty_link = corporate_links[current_week]

    next_week = (current_week + 1) % len(duty_schedule)  
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
    updater = Updater("7539124014:AAGekjZrKUuBCP8-f1nP_aKo_RgO8aNhwXg", use_context=True)  # вставьте токен бота
    dispatcher = updater.dispatcher
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

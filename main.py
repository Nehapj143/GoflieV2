import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests

logging.basicConfig(level=logging.INFO)

TOKEN = '7101601852:AAFg85Y8TLJXGjpW_6T4Cpsx61VT4PrsqNY'  # Replace with your Telegram bot token
GOFILe_API_KEY = 'xdqmdwlfDftnNGxVuDlA2WZncahb14Dv'  # Replace with your GoFile.io API key

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hello! I can upload files to GoFile.io.')

def upload_file(update, context):
    # Get the file from the user
    file_id = update.message.document.file_id
    file_info = context.bot.get_file(file_id)
    file_url = f'https://api.telegram.org/file/bot{TOKEN}/{file_info.file_path}'

    # Upload the file to GoFile.io
    headers = {'Authorization': f'Bearer {GOFILe_API_KEY}'}
    response = requests.post('https://api.gofile.io/uploadFile', headers=headers, files={'file': requests.get(file_url).content})

    # Send the uploaded file link to the user
    if response.status_code == 200:
        file_link = response.json()['data']['link']
        context.bot.send_message(chat_id=update.effective_chat.id, text=f'File uploaded successfully! {file_link}')
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text='Error uploading file.')

def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.document, upload_file))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

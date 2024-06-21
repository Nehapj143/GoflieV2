from gofile_api import upload_file

def upload_file(update, context):
    # Get the file from the user
    file_id = update.message.document.file_id
    file_info = context.bot.get_file(file_id)
    file_url = f'https://api.telegram.org/file/bot{TOKEN}/{file_info.file_path}'

    # Upload the file to GoFile.io
    gofile_api_key = 'YOUR_GOFILe_API_KEY'  # Replace with your GoFile.io API key
    response = upload_file(file_url, gofile_api_key)

    # Send the uploaded file link to the user
    if response['status'] == 'ok':
        file_link = response['data']['link']
        context.bot.send_message(chat_id=update.effective_chat.id, text=f'File uploaded successfully! {file_link}')
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text='Error uploading file.')

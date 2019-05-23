from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def bop(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def repeat(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)

def main():
    updater = Updater('166040199:AAFtjC53koT800qH3xTz-sgm6lvjL3C7hfY')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    dp.add_handler(MessageHandler(Filters.text,repeat))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
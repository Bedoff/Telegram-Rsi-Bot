from time import strftime

from binance.helpers import interval_to_milliseconds
import binanceandrsi
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import datetime
import time


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update, context):
    update.message.reply_text('Hoşgeldin')
    update.message.reply_text('Bu bot sayesinde istediğin coinlerin saatlik olarak rsi hesaplamasını alabileceksin')
    update.message.reply_text('Eğer yardıma ihtiyacın olursa /help yazabilirsin')
    update.message.reply_text('Unutma ki bu bot geliştirilme sürecindedir veriler yatırım tavsiyesi değildir')
    i=0
    while i<1:

        deger1=binanceandrsi.megacal("BTC","USDT")
        update.message.reply_text(deger1)

        deger1=binanceandrsi.megacal("ETH","USDT")
        update.message.reply_text(deger1)

        deger1=binanceandrsi.megacal("CHZ","USDT")
        update.message.reply_text(deger1)

        time.sleep(900)
        
    

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Öncelikle bir coin ve bir parametre seçmen gerekiyor')
    update.message.reply_text('ÖRNEK OLARAK "BTC" "USDT"')
    update.message.reply_text('/TRD1 BTC')
    update.message.reply_text('/TRD2 USDT')
    update.message.reply_text('Yukarıdaki belirtilen şekilde bir girdi girdiğin takdirde saat başı BTC/USDT nin rsi hesaplamasını alıcaksın')


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    updater = Updater("TELEGRAM KEY", use_context=True)
    dp = updater.dispatcher

    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))   
    
    
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

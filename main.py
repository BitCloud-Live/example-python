#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler


def start(bot, update):
    update.message.reply_text(
        'سلام {} جان'.format(update.message.from_user.first_name))


updater = Updater('433604236:AAFh59UsEy4-az17_a1hyAviUqk1nZwZFpc')

updater.dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()
updater.idle()


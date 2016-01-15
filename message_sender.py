#!/usr/bin/env python2 -tt
# -*- coding: utf-8 -*-
import telebot

#set bot token
bot=telebot.TeleBot('your token here')

#send the message to the bot

def send(message):
    chatid=00000000 #your chat id here
    bot.send_message(chatid,message)
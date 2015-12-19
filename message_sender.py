#!/usr/bin/env python2 -tt
# -*- coding: utf-8 -*-
import telebot

#set bot token
bot=telebot.TeleBot('177620498:AAEqcEe5C-33hDFY03GRXhNZbG53rsSa7wU')

#send the message to the bot

def send(message):
    bot.send_message(178301470,message)
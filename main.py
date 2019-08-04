from chatterbot import *
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot("MyChatBot")
trainer = ListTrainer(bot)

for files in os.listdir('/home/sonali/PycharmProjects/chatbot1/english/'):
    data = open('/home/sonali/PycharmProjects/chatbot1/english/' + files , 'r').readlines()
    trainer.train(data)

while True:
    message = input('You: ')
    if message.strip() != 'Bye':
        reply = bot.get_response(message)
        print('Chatbot: ', reply)
    if message.strip() == 'Bye':
        print('ChatBot: Bye')
        break

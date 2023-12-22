from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Test')

conv = open('chat.txt', 'r').readlines()
# bot.set_trainer(ListTrainer)
#
tr = ListTrainer(bot)
tr.train(conv)

while True:
    request = input('You: ')
    response = bot.get_response(request)

    print('Bot:', response)

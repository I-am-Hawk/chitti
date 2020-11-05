# Importing Packages

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Defining The Bot name

chitti = ChatBot(name = 'Chitti', read_only = True,
                 logic_adapters = ['chatterbot.logic.MathematicalEvaluation',
                                   'chatterbot.logic.BestMatch'])



# Importing Packages

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Defining The Bot name

chitti = ChatBot(name = 'Chitti', read_only = True,
                 logic_adapters = ['chatterbot.logic.MathematicalEvaluation',
                                   'chatterbot.logic.BestMatch'])

# Teaching the Bot
# See lakshya here first "hi there!" is what user says and "hi" is what the chitti would reply for it
# We can continue with all the possible greetings by putting in a list with the same syntax
# so the first line is what user will type and the second line is what bot will reply
# do you understand ?
greetings_chitti = ['hi there!',
                    'hi',
                    'hi chitti',
                    'hi user, how are you ?',
                    'i am fine chitti',
                    'i am also fine user']
# You can put as much knowledge as you can
knowledge_science_chitti = ['what are the parts of science ?',
                            'physics , chemistry and biology']

# Putting all the knowledge into the chitti's mind
list_trainer_chitti = ListTrainer(Chitti)

for item in (greetings_chitti,knowledge_science_chitti):
  list_trainer_chitti.train(item)
# Copy paste this code and run in your python
# Temprory your chitti is made try to put as much knowledge you can in the list
# We will make it better tommorrow 
# any problem you have chat with me on telegram
                    

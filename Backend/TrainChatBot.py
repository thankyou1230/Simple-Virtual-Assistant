from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os
class TrainedChatBot(ChatBot):
    def __init__(self, *args, **kwargs):
        super(TrainedChatBot, self).__init__(*args, **kwargs)
        list_trainer = ChatterBotCorpusTrainer(self)
        for corpus in os.listdir('./BackEnd/Source/Corpus'):
            try:
                list_trainer.train('./BackEnd/Source/Corpus/'+corpus)
            except Exception:
                print('Không thể truy cập {}, corpus này sẽ bị bỏ qua'.format(corpus))



from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

def TrainChatBot():
    my_bot = ChatBot(name='Bi', read_only=True, 
                storage_adapter='chatterbot.storage.SQLStorageAdapter',
                database_uri='sqlite:///database.sqlite3',
                 logic_adapters=['chatterbot.logic.MathematicalEvaluation',
                                 'chatterbot.logic.BestMatch']
                )
    list_trainer = ChatterBotCorpusTrainer(my_bot)
    list_trainer.train('D:/Do An Python/Python-Programing-Technique-Project/Backend/Source/Corpus/ai.yml',
                   'D:/Do An Python/Python-Programing-Technique-Project/Backend/Source/Corpus/botprofile.yml',  
                   'D:/Do An Python/Python-Programing-Technique-Project/Backend/Source/Corpus/computers.yml',
                   'D:/Do An Python/Python-Programing-Technique-Project/Backend/Source/Corpus/emotion.yml',
                   'D:/Do An Python/Python-Programing-Technique-Project/Backend/Source/Corpus/greetings.yml',
                   'D:/Do An Python/Python-Programing-Technique-Project/Backend/Source/Corpus/health.yml',
                   'D:/Do An Python/Python-Programing-Technique-Project/Backend/Source/Corpus/humor.yml',
                   'D:/Do An Python/Python-Programing-Technique-Project/Backend/Source/Corpus/science.yml',
                   )


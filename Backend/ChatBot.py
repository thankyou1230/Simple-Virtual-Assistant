from chatterbot import ChatBot, storage, logic
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
from Bi import Bi
import time
my_bot = ChatBot(name='PyBot', read_only=True,
                 logic_adapters=['chatterbot.logic.MathematicalEvaluation',
                                 'chatterbot.logic.BestMatch'])
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
bi=Bi()
while True:
    text=bi.listen()
    if text:
        print(text)
        voice=str(my_bot.get_response(text))
        bi.speak(voice)

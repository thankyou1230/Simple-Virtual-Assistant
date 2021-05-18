from gtts import gTTS
import os
import playsound
import speech_recognition as sr
import smtplib
class Bot():
    
    ##########################
    def speak(self,text):
        tts = gTTS(text=text, lang='vi', slow=False)
        tts.save("sound.mp3")
        playsound.playsound("sound.mp3", True)
        os.remove("sound.mp3")

    ##########################
    def listen(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Tôi: ", end='') 
            audio = r.listen(source, phrase_time_limit=3)
            try:
                text = r.recognize_google(audio, language="vi-VN")
                return text
            except:
                return False
    ##########################
    def send_email(self,destination,content):
        with smtplib.SMTP('smtp.gmail.com', 587) as mail:
            mail.ehlo()
            mail.starttls()
            mail.login('quang0002@gmail.com', '0917787421q')
            #kêu chờ
            mail.sendmail('quang0002@gmail.com',destination, content.encode('utf-8'))
            mail.close()
            #báo đã xong
if __name__=='__main__':
    bot=Bot()
    bot.send_email('18520140@gm.uit.edu.vn','Xin chào')
from gtts import gTTS
import os
import playsound
import speech_recognition as sr
import smtplib
from email.mime.text import MIMEText
import ctypes
import urllib
import urllib.request
import json
import pathlib
import webbrowser
import geocoder
import datetime
import youtube_search

class Bot():
    
    ##########################  1
    def speak(self,text):
        try:
            tts = gTTS(text=text, lang='vi', slow=False)
            tts.save("sound.mp3")
            playsound.playsound("sound.mp3", True)
            os.remove("sound.mp3")
            return True
        except Exception as e:
            #Không nói được thì tức là mạng không có
            return False

    ##########################  2
    def listen(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Tôi: ", end='') 
            audio = r.listen(source, phrase_time_limit=3)
            try:
                text = r.recognize_google(audio, language="vi-VN")
                return text
            except Exception as e:
                return False
   
    ##########################  3
    def send_email(self,destination,subject,content):
        msg = MIMEText(content)
        msg['Subject'] = subject
        msg['From'] = 'admin@example.com'
        msg['To'] = 'info@example.com'
        self.speak('Bạn chờ chút nhé')
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as mail:
                mail.ehlo()
                mail.starttls()
                mail.login('quang0002@gmail.com', '0917787421q')
                mail.sendmail('quang0002@gmail.com',destination, msg.as_string().encode('utf-8'))
                mail.close()
            self.speak('Tôi đã gửi đi thành công rồi nhé')
            return True
        except Exception as e:
            self.speak('Xin lỗi hiện tại không gửi được rồi, hãy thử lại sau nhé')
    
    ########################### 4
    def change_random_walpaper(self):
        api_key = 'lTRwvyGb1vAmzbDCruvqzCR7hdFpa4HfG-gjNZkDbkc'
        url = 'https://api.unsplash.com/photos/random?client_id=' + api_key 
        self.speak('Bạn chờ một chút nhé')
        try:   
            f = urllib.request.urlopen(url)
            json_string = f.read()
            f.close()
            parsed_json = json.loads(json_string)
            photo = parsed_json['urls']['full']
            # Location where we download the image to.
            save_path=os.path.join(pathlib.Path(__file__).parent.absolute(),'Source\img.png')
            urllib.request.urlretrieve(photo, save_path)
            ctypes.windll.user32.SystemParametersInfoW(20,0,save_path,3)
            self.speak('Tôi đã đổi xong rồi đấy, bạn xem thử xem')
            return True
        except Exception as e:
            self.speak('Xin lỗi hiện tại tôi không thể đổi được ảnh nền, xin hãy thử lại sau')
            return False
    
    ############################# 5
    def search_google(self,serch_text):
        url="https://www.google.com.tr/search?q={}".format(serch_text)
        self.speak('Có ngay đây')
        try:
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
            webbrowser.get('chrome').open_new_tab(url)
            return True
        except Exception as e:
            self.speak('Xin lỗi, hiện tại tôi không thể giúp bạn tìm kiếm. Xin thử lại sau')
            return False
    
    ############################# 6
    def wheather_forecast(self):
        self.speak('Chờ một chút để tôi tìm nhé')
        locate = geocoder.ip('me').latlng
        api_key='dd1374e7b62f69d53f6696a829430e76'
        url='http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}&lang=vi&units=metric'.format(locate[0],locate[1],api_key)
        try:  
            f = urllib.request.urlopen(url)
            json_string = f.read()
            f.close()
            data = json.loads(json_string)
            #set data
            city="Thành phố "+str(geocoder.ip('me').city).replace('City','')
            temp=data['main']['feels_like']
            humid=data['main']['humidity']
            wind=data['wind']['speed']
            vision=data['visibility']
            weather=data['weather'][0]['description']
            sunrise=datetime.datetime.fromtimestamp(data['sys']['sunrise'])
            sunset=datetime.datetime.fromtimestamp(data['sys']['sunset'])
            #respone
            forecast_script='Đây rồi. Thời tiết {} hôm nay có {}, nhiệt độ trung bình là {} độ C, độ ẩm là {}%, sức gió {} km trên giờ,\
                        tầm nhìn xa trên {} mét. Hôm nay mặt trời mọc lúc {} giờ {} phút, lặn lúc {} giờ {} phút. Xin hết'.\
                        format(city,weather,temp,humid,wind,vision,sunrise.hour,sunrise.minute,sunset.hour,sunset.minute)
            self.speak(forecast_script)
            return True
        except Exception as e:
            self.speak('Xin lỗi hiện tại tôi không thể truy cập vào dữ liệu thời tiết. Xin thử lại sau')
            return False

    ############################## 7
    def play_youtube(self,video_name):
        self.speak('Chờ chút có ngay')
        try:
            video = youtube_search.YoutubeSearch(video_name, max_results=1).to_dict()
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
            webbrowser.get('chrome').open_new_tab('https://www.youtube.com/watch?v='+video[0]['id'])
            self.speak('Tôi mở rồi đấy nhé')
            return True
        except Exception as e:
            self.speak('Xin lỗi, hiện tại tôi không thể làm được. Xin thử lại sau')
            return False
if __name__=='__main__':
    bot=Bot()
    bot.play_youtube('bac phan')
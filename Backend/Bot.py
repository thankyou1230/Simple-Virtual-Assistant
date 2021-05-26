import os
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
import wikipedia
import time
import pyttsx3
from threading import Thread
from .TrainChatBot import TrainedChatBot
class Bi():
    
    def __init__(self):
        #ChatBot đã được huấn luyện
        self.brain=TrainedChatBot(name='Bi', read_only=True, 
                storage_adapter='chatterbot.storage.SQLStorageAdapter',
                database_uri='sqlite:///database.sqlite3',
                 logic_adapters=['chatterbot.logic.MathematicalEvaluation',
                                 'chatterbot.logic.BestMatch']
                )
        self.talking_speed=130
        #module pyttsx3 giúp chuyển văn bản thành âm thanh
        self.mouth = pyttsx3.init()
        voices=self.mouth.getProperty("voices")
        self.mouth.setProperty("voice",voices[1].id)
        self.mouth.setProperty('rate', self.talking_speed)
        #Lớp Regcognizer giúp chuyển âm thanh thành văn bản
        self.ear = sr.Recognizer()

    # Input: Text
    # Chức năng: Phát ra âm thanh đoạn Text
    # Output: không có
    def speak(self,text):
        try:
            self.mouth.say(text)
            self.mouth.runAndWait()
        except Exception:
            pass


    def multiprocess_speak(self,text):
        thread=Thread(target=self.speak,args=(text,))
        thread.start()
        return text
    # Input: không
    # Chức năng: Nhận âm thanh từ microphone và chuyển thành Text
    # Output: Text nhận dạng được
    def listen(self):
        with sr.Microphone() as source:
            print('listening')
            audio = self.ear.listen(source, phrase_time_limit=3.5)
            try:
                text = self.ear.recognize_google(audio, language="vi-VN")
                return text
            except Exception as e:
                return ''
   
    # Input: địa chỉ mail, tiêu đề, nội dung
    # Chức năng: gửi mail theo những thông số ở trên, nói kết quả thực hiện bằng phương thức speak
    # Output: thông báo kết quả thành công hay thất bại
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
            return self.multiprocess_speak('Tôi đã gửi đi thành công rồi nhé')
        except Exception as e:
            return self.multiprocess_speak('Hình như có trục trặc gì đó, hãy kiểm tra và làm lại nhé')
    
    # Input: Không có
    # Chức năng: Gọi api tải về hình ngẫu nhiên và đặt làm hình nền máy tính
    # Output: thông báo thành công hoặc thất bại
    def change_random_walpaper(self):
        api_key = 'lTRwvyGb1vAmzbDCruvqzCR7hdFpa4HfG-gjNZkDbkc'
        url = 'https://api.unsplash.com/photos/random?client_id=' + api_key 
        self.speak('Ô kê, mất vài giây thôi')
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
            return self.multiprocess_speak('Mình đã đổi xong rồi đấy, bạn coi thử xem')
        except Exception as e:
            return self.multiprocess_speak('Xin lỗi hiện tại mình không thể đổi được ảnh nền giúp bạn, một lát thử lại nhé')

    
    # Input: đoạn text muốn search
    # Chức năng: Tìm kiếm nội dung text trên google và mở kết quả trong tab mới
    # Output: thông báo kết quả thành công hoặc thất bại
    def search_google(self,serch_text):
        url="https://www.google.com.tr/search?q={}".format(serch_text)
        self.speak('Đợi chút nha')
        try:
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
            webbrowser.get('chrome').open_new_tab(url)
            return self.multiprocess_speak('Có rồi nhé')
        except Exception as e:
            return self.multiprocess_speak('Xin lỗi, hiện tại mình không gọi được cho chị gu gồ')
    
    # Input: không có
    # Chức năng: gọi api lấy về dự báo thời tiết của vị trí hiện tại trong hôm nay
    # Output: thành công thì trả về kết quả dự báo, thất bại thì thông báo lỗi
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
            self.speak('đây rồi')
            forecast_script='Thời tiết {}hôm nay có {}, nhiệt độ trung bình là {} độ C, độ ẩm là {}%, sức gió {} km trên giờ,\
                        tầm nhìn xa trên {} mét. Hôm nay mặt trời mọc lúc {} giờ {} phút, lặn lúc {} giờ {} phút. Xin hết'.\
                        format(city,weather,temp,humid,wind,vision,sunrise.hour,sunrise.minute,sunset.hour,sunset.minute)
            return self.multiprocess_speak(forecast_script)
        except Exception as e:
            return self.multiprocess_speak('Bạn ơi hiện tại mình không thể truy cập vào dữ liệu thời tiết, xin lỗi nhé')

    # Input: tên video
    # Chức năng: mở video theo yêu cầu trên youtube trong tab mới, bằng trình duyệt chrome
    # Output: Thông báo kết quả hành công hay thất bại
    def play_youtube(self,video_name):
        self.speak('Chờ chút có ngay')
        try:
            video = youtube_search.YoutubeSearch(video_name, max_results=1).to_dict()
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
            webbrowser.get('chrome').open_new_tab('https://www.youtube.com/watch?v='+video[0]['id'])
            return self.multiprocess_speak('Tôi mở rồi đấy. Mời bạn thưởng thức nhá')
        except Exception as e:
            return self.multiprocess_speak("Hình như hết tiền mạng rồi :D")
    
    # Input: tên cần định nghĩa
    # Chức năng: tìm định nghĩa trên wikipedia
    # Output: trả về đoạn đầu trong định nghĩa nếu thành công, ngược lại thông báo đã xảy ra lỗi
    def define(self,name):
        self.speak('Để mình nhớ xem')
        try:
            wikipedia.set_lang('vi')
            contents = wikipedia.summary(name).split('.')
            return self.multiprocess_speak('Theo mình biết: ' +contents[0])
        except Exception as e:
            return self.multiprocess_speak('Mình cũng không biết nữa. Chị gu gồ chắc sẽ biết đó')
    
    # Input: không có
    # Chức năng: lấy thời gian hiện tại
    # Output: trả về thời gian hiện tại
    def get_time(self):
        t = time.localtime()
        return time.strftime('%H:%M:%S', t)

    # Input: không có
    # Chức năng: lấy thông tin ngày tháng năm hiện tại
    # Output: trả về thông tin ngày tháng năm hiện tại
    def get_date(self):
        t = time.localtime()
        return time.strftime('%d/%m/%Y', t)
    
    # Input: yêu cầu của người dùng
    # Chức năng: phân tích yêu cầu và gọi phương thức phù hợp để thực hiện
    # Output: trả về theo kết quả của chức năng đã thực hiện
    def react_to(self, request):
        request=request.lower()
        if request=='':
            return
        if 'bi ơi' in request:
            return self.multiprocess_speak('Mình đây, bạn cần gì')
        elif "tạm biệt bạn" in request:
            self.multiprocess_speak('Tạm biệt, hãy gọi tôi khi cần nhé')
            #tắt chương trình
            pass
        elif "hiện tại" in request or "mấy giờ" in request or 'bây giờ là' in request:
            response='Bây giờ là '+self.get_time()
            self.multiprocess_speak(response)
            return response
        elif 'hôm nay là' in request or 'ngày mấy' in request:
            response='Hôm nay là '+self.get_date()
            self.multiprocess_speak(response)
            return response
        elif 'tìm' in request:
            if request.split(' ').index('tìm')==0:
                return self.search_google(request.replace('tìm',''))
            return self.search_google(request.split(" tìm ",1)[1])
        elif 'mở' in request or 'phát' in request:
            return self.play_youtube(request)
        elif 'gửi mail' in request or 'gởi mail' in request:
            self.speak('Bạn muốn gửi mail cho ai')
            destination=self.listen()
            self.speak('Bạn muốn đặt tiêu đề là gì')
            subject=self.listen()
            self.speak('Nội dung của mail là gì')
            content=self.listen()
            return self.send_email(destination,subject,content)
        elif 'đổi ảnh' in request or 'thay ảnh' in request or 'đổi hình' in request or 'thay hình' in request or 'đổi nền' in request or 'thay nền' in request:
            return self.change_random_walpaper()
        elif 'thời tiết' in request:
            return self.wheather_forecast()
        elif ('là gì' in request or 'là ai' in request) and 'bạn là ai' not in request:
            return self.define(request.replace('là gì','').replace('là ai',''))
        else:
            return self.multiprocess_speak(str(self.brain.get_response(request)))


if __name__=='__main__':
    bot=Bi()
    bot.react_to('Bi ơi')
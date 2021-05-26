import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from Interface.CustomedElementWidgets import RecordButton, SendButton, MessageEditor, MessageView
import sys
from Backend.Bot import Bi
from threading import Thread,  Timer
import time
class Ui_ChatBot(object):
    
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        #ChatBot
        self.bot=Bi()
        #Main Window
        self.UI = QtWidgets.QMainWindow()
        self.UI.setObjectName("ChatBot")
        self.UI.resize(431, 518)
        self.UI.setMaximumSize(QtCore.QSize(431, 518))
        self.UI.setStyleSheet("QMainWindow{\n"
                                   "background:rgb(255, 255, 255);\n"
                                   "}")
        self.centralwidget = QtWidgets.QWidget(self.UI)
        self.centralwidget.setObjectName("centralwidget")
        QtCore.QMetaObject.connectSlotsByName(self.UI)
        self.UI.setCentralWidget(self.centralwidget)
        #Thread event
        self.flag=0
        #Record button
        self.recordButton = RecordButton(self.centralwidget)
        self.recordButton.pressed.connect(self.send_user_message_from_micro)
        #Send button
        self.sendButton = SendButton(self.centralwidget)
        self.sendButton.pressed.connect(self.send_user_message_from_keyboard)
        #Message Editor
        self.editMessage = MessageEditor(self.centralwidget)
        self.editMessage.returnPressed.connect(self.send_user_message_from_keyboard)
        #Message View
        self.MessageView = MessageView(self.centralwidget)
    #Hiển thị app
    def show(self):
        self.UI.show()
        self.app.exec_()
    
    def pressbutton(self):
        if self.flag==1:
            self.sendButton.pressed.emit()
            self.flag=0
        

    #Gửi tin nhắn nhập từ bán phím và gọi xử lí
    def send_user_message_from_keyboard(self):
        request=self.editMessage.text()
        self.editMessage.setText('')
        self.editMessage.setPlaceholderText('Chờ bi xử lí chút nhé')
        #self.editMessage.setDisabled(True)
        self.MessageView.MessageList.addMessage('user',request )
        QtWidgets.QApplication.processEvents()
        self.bot_processing(request)
        #thread=Thread(target=self.bot_processing,args=(self.editMessage.text(),))
        #thread.setDaemon(True)
        #thread.start()
        self.editMessage.setPlaceholderText('')
        self.MessageView.scrollToBottom()
    
    #Thay đổi icon báo là bot đang nghe
    def on_listening(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Interface/Icon/hear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.recordButton.setIcon(icon)

    #Thay dổi icon báo là bot đã nghe xong
    def has_listened(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Interface/Icon/recordVoice.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.recordButton.setIcon(icon)
    
    def send_user_message_from_micro(self):
        self.editMessage.setDisabled(True)
        self.editMessage.setPlaceholderText('Bi đang nghe bạn nói đấy')
        self.on_listening()
        QtWidgets.QApplication.processEvents()
        request=self.bot.listen()
        self.has_listened()
        QtWidgets.QApplication.processEvents()
        self.editMessage.setPlaceholderText('Chờ Bi xử lí chút nhé')
        self.editMessage.setDisabled(False)
        self.MessageView.MessageList.addMessage('user',request)
        QtWidgets.QApplication.processEvents()
        self.bot_processing(request)
        #thread=Thread(target=self.bot_processing,args=(temp,))
        #thread.setDaemon(True)
        #thread.start()
        #########
        self.MessageView.scrollToBottom()

    #Gửi tin nhắn từ bot 
    def sendBotMessage(self, message=''):
        self.MessageView.MessageList.addMessage('bot', message)
        # self.MessageView.MessageList.addMessage('bot', MessageModel(QtGui.qt))
    
    #Xử lí phía bot
    def bot_processing(self,request):
        self.sendBotMessage(self.bot.react_to(request))

if __name__=='__main__':
    import sys
    ui = Ui_ChatBot()
    ui.sendBotMessage('Chào bạn, mình có thể giúp gì được cho bạn')
    ui.show()
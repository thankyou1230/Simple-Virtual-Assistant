from PyQt5 import QtCore, QtGui, QtWidgets
from Interface.CustomedElementWidgets import RecordButton, SendButton, MessageEditor, MessageView
import sys
from Backend.Bot import Bi
import time
from threading import Thread
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
    
    #Gửi tin nhắn nhập từ bán phím
    def send_user_message_from_keyboard(self):
        self.MessageView.MessageList.addMessage('user', self.editMessage.text())
        self.bot_processing(self.editMessage.text())
        self.MessageView.scrollToBottom()
        self.editMessage.setText('')
    
    def send_user_message_from_micro(self):
        self.editMessage.setDisabled(True)
        #########
        temp=self.bot.listen()
        self.MessageView.MessageList.addMessage('user',temp)
        self.bot_processing(temp)
        #########
        self.MessageView.scrollToBottom()
        self.editMessage.setDisabled(False)

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
    
    # 
    # 
    # 
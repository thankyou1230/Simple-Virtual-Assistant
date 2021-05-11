from PyQt5 import QtCore, QtGui, QtWidgets
from MessageBubble import MessageModel, MessageDelegate
from CustomedElementWidgets import RecordButton, SendButton, MessageEditor, MessageView
class Ui_ChatBot(object):
    
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        #Main Window
        self.ChatBot = QtWidgets.QMainWindow()
        self.ChatBot.setObjectName("ChatBot")
        self.ChatBot.resize(431, 518)
        self.ChatBot.setMaximumSize(QtCore.QSize(431, 518))
        self.ChatBot.setStyleSheet("QMainWindow{\n"
                                   "background:rgb(255, 255, 255);\n"
                                   "}")
        self.centralwidget = QtWidgets.QWidget(self.ChatBot)
        self.centralwidget.setObjectName("centralwidget")
        QtCore.QMetaObject.connectSlotsByName(self.ChatBot)
        self.ChatBot.setCentralWidget(self.centralwidget)
        #Record button
        self.recordButton = RecordButton(self.centralwidget)
        #Send button
        self.sendButton = SendButton(self.centralwidget)
        #Message Editor
        self.editMessage = MessageEditor(self.centralwidget)
        #Message View
        self.MessageView = MessageView(self.centralwidget)
        
        self.sendButton.pressed.connect(self.sendUserMessage,)
    def show(self):
        self.ChatBot.show()
        self.app.exec_()
    

    def sendUserMessage(self):
        self.MessageView.MessageList.addMessage('user', self.editMessage.toPlainText())
        self.MessageView.scrollToBottom()

    def sendBotMessage(self, message=''):
        self.MessageView.MessageList.addMessage('bot', message)
        # self.MessageView.MessageList.addMessage('bot', MessageModel(QtGui.qt))



if __name__=='__main__':
    import sys
    ui = Ui_ChatBot()
    ui.sendBotMessage('Chào bạn, mình có thể giúp gì được cho bạn')
    ui.show()
    
    # 
    # 
    # 
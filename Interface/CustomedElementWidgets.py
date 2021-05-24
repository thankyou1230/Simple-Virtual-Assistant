from PyQt5 import QtCore, QtGui, QtWidgets
from .MessageBubble import MessageDelegate, MessageModel

class RecordButton(QtWidgets.QPushButton):
    def __init__(self, *args, **kwargs):
        super(RecordButton, self).__init__(*args, **kwargs)
        self.setGeometry(QtCore.QRect(10, 460, 41, 41))
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setMouseTracking(True)
        self.setToolTipDuration(1500)
        self.setStyleSheet("QPushButton{\n"
                                        "background: none;\n"
                                        "border:none;\n"
                                        "border-radius:20%\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "background:rgb(166, 200, 255)\n"
                                        "}")
        self.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Interface/Icon/recordVoice.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setIcon(icon)
        self.setIconSize(QtCore.QSize(40, 40))
        self.setObjectName("recordButton")
###################################################################
###################################################################

class SendButton(QtWidgets.QPushButton):
    def __init__(self, *args, **kwargs):
        super(SendButton, self).__init__(*args, **kwargs)
        self.setGeometry(QtCore.QRect(380, 460, 41, 41))
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setMouseTracking(True)
        self.setToolTipDuration(1500)
        self.setStyleSheet("QPushButton{\n"
                                      "background: none;\n"
                                      "border:none;\n"
                                      "border-radius:20%\n"
                                      "}\n"
                                      "QPushButton:Hover{\n"
                                      "background: rgb(160, 196, 255);\n"
                                      "}")
        self.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Interface/Icon/send.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setIcon(icon)
        self.setIconSize(QtCore.QSize(55, 53))
        self.setObjectName("sendButton")

######################################################################
######################################################################

class MessageEditor(QtWidgets.QLineEdit):
    def __init__(self, *args, **kwargs):
        super(MessageEditor, self).__init__(*args, **kwargs)
        self.setGeometry(QtCore.QRect(60, 460, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.setFont(font)
        self.setStyleSheet("QLineEdit{\n"
                                   "border: none;\n"
                                   "border-radius: 20px;\n"
                                   "corlor: rgb(209, 209, 209);\n"
                                   "background: rgb(208, 208, 208);\n"
                                   "padding-top:7%;\n"
                                   "padding-left:10px;\n"
                                   "font-size:10pt;\n"
                                   "padding-right:15px;\n"
                                   "padding-bottom:6%\n"
                                   "}")
        self.setLocale(QtCore.QLocale(QtCore.QLocale.Vietnamese, QtCore.QLocale.Vietnam))
        self.setPlaceholderText("Type here !")
        self.setObjectName("chatBox") 

##########################################################################
##########################################################################

class MessageView(QtWidgets.QListView):
    def __init__(self, *args, **kwargs):
        super(MessageView, self).__init__(*args, *kwargs)
        self.setGeometry(QtCore.QRect(10, 10, 410, 430))
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.setAutoFillBackground(True)
        self.setStyleSheet("QListView{\n"
                                      "border:none;\n"
                                      "background:white;\n"
                                      "}")
        self.setObjectName("MessageView")
        self.setItemDelegate(MessageDelegate())
        self.MessageList = MessageModel()
        self.setModel(self.MessageList)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)


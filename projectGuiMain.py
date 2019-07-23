from stemming import *
from posTagging import *
from textProcessing import *
from FeelingProbablity import *
import nltk
import re

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap


def addPosTagToFinalList(finalTagSentence, posTagSentence, indexSentence):
    for indexToken in range(len(finalTagSentence[indexSentence])):
        finalTagSentence[indexSentence][indexToken].append(posTagSentence[indexToken])


feelingIcon = ("happy.png", "unhappy.png", "angry.png", "confused.png", "disgust.png", "surprised.png")


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(450, 330)
        Dialog.setMouseTracking(True)
        Dialog.setFocusPolicy(QtCore.Qt.WheelFocus)
        Dialog.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        Dialog.setWindowTitle("")
        icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap("C:/Users/Azer/Downloads/th.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(320, 60, 100, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft Uighur")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setLineWidth(3)
        self.label.setMidLineWidth(0)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(220, 170, 91, 31))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(True)
        self.pushButton.setAutoExclusive(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        # action But1
        self.pushButton.clicked.connect(self.B1action)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 170, 91, 31))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setChecked(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.B2action)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(110, 10, 230, 41))
        font = QtGui.QFont()
        font.setFamily("Sakkal Majalla")
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(30, 90, 371, 61))
        self.textEdit.setObjectName("textEdit")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(328, 220, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 250, 370, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setAutoFillBackground(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(175, 220, 120, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(300, 220, 25, 25))

        self.label_6.setObjectName("label_6")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Dialog", "ادخل النص "))
        self.pushButton.setText(_translate("Dialog", "نشر"))
        self.pushButton_2.setText(_translate("Dialog", "الغاء"))
        self.label_2.setText(_translate("Dialog", "   تحليل الشعور"))
        self.label_3.setText(_translate("Dialog", "حــمــاده "))
        self.label_5.setText(_translate("Dialog", ""))

    def B1action(self):
        global lemmaList
        finalTagSentence = []

        print("Welcome to FEELING MINING")
        # محمد يلعب الكره !,سيذهب الى المدرسه
        # ذهب محمد الى المدرسه حزين,ولكن رجع سعيد
        userInput = self.textEdit.toPlainText()

        # list of sentence
        listOfSentence = re.split(",", userInput)
        print(listOfSentence)

        listOfToken = []
        listOfprocess = []

        # Tokenizer
        for sentence in listOfSentence:
            listOfToken.append(nltk.word_tokenize(sentence))
        print("list for each token")
        print(listOfToken)

        # text processing
        for sentenceToken in listOfToken:
            opTextProcess = TextProcessing(sentenceToken)
            listOfprocess.append(opTextProcess.textProcessing())
        print("three element")
        print(listOfprocess)

        # Stemming and lemmatization
        for sentenceProToken in listOfprocess:
            op1 = Stemming(sentenceProToken)
            affixesList, lemmaList = op1.affixesRemoval()
            finalTagSentence.append(lemmaList)
        print("Lemma is : " + str(finalTagSentence))

        # Pos Tagging
        for indexSentence in range(len(finalTagSentence)):
            op2 = posTagging(finalTagSentence[indexSentence])
            addPosTagToFinalList(finalTagSentence, op2.Pos_tagg(), indexSentence)
        print("Output final : " + str(finalTagSentence))

        ######################## Selected Feeling ###################################

        op3 = feelingProbablity(finalTagSentence)
        feelingOutput, feelingIndex = op3.probablityProcessing()

        # output gui
        if feelingIndex != -1:
            pixmap = QPixmap(feelingIcon[feelingIndex])
            self.label_6.setPixmap(pixmap)
            self.label_5.setText("يشعر بـ" + str(feelingOutput))
        else:
            pixmap = QPixmap("nofeeling.png")
            self.label_6.setPixmap(pixmap)
            self.label_5.setText("يشعر بـ" + str(feelingOutput))

        textboxValue = self.textEdit.toPlainText()
        print(textboxValue)
        self.label_4.setText(textboxValue)

    def B2action(self):
        self.textEdit.clear()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

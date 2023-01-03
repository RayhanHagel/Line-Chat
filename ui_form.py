# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QLabel,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_Background(object):
    def setupUi(self, Background):
        if not Background.objectName():
            Background.setObjectName(u"Background")
        Background.resize(275, 458)
        Background.setMinimumSize(QSize(275, 458))
        Background.setMaximumSize(QSize(275, 458))
        icon = QIcon()
        icon.addFile(u"assets/icon.jpg", QSize(), QIcon.Normal, QIcon.Off)
        Background.setWindowIcon(icon)
        Background.setWindowOpacity(1.000000000000000)
        Background.setStyleSheet(u"background-color:#151b1f;")
        self.checkboxMale = QCheckBox(Background)
        self.checkboxMale.setObjectName(u"checkboxMale")
        self.checkboxMale.setGeometry(QRect(40, 90, 78, 22))
        font = QFont()
        font.setFamilies([u"RomanC"])
        self.checkboxMale.setFont(font)
        self.checkboxMale.setCursor(QCursor(Qt.ClosedHandCursor))
        self.checkboxMale.setStyleSheet(u"background-color:#1e2329;\n"
"color:#797979;")
        self.checkboxFemale = QCheckBox(Background)
        self.checkboxFemale.setObjectName(u"checkboxFemale")
        self.checkboxFemale.setGeometry(QRect(150, 90, 101, 22))
        self.checkboxFemale.setFont(font)
        self.checkboxFemale.setCursor(QCursor(Qt.ClosedHandCursor))
        self.checkboxFemale.setStyleSheet(u"background-color:#1e2329;\n"
"color:#797979;")
        self.checkboxMuslim = QCheckBox(Background)
        self.checkboxMuslim.setObjectName(u"checkboxMuslim")
        self.checkboxMuslim.setGeometry(QRect(40, 170, 78, 22))
        self.checkboxMuslim.setFont(font)
        self.checkboxMuslim.setCursor(QCursor(Qt.ClosedHandCursor))
        self.checkboxMuslim.setStyleSheet(u"background-color:#1e2329;\n"
"color:#797979;")
        self.checkboxProtestant = QCheckBox(Background)
        self.checkboxProtestant.setObjectName(u"checkboxProtestant")
        self.checkboxProtestant.setGeometry(QRect(150, 170, 101, 22))
        self.checkboxProtestant.setFont(font)
        self.checkboxProtestant.setCursor(QCursor(Qt.ClosedHandCursor))
        self.checkboxProtestant.setStyleSheet(u"background-color:#1e2329;\n"
"color:#797979;")
        self.checkboxCatholic = QCheckBox(Background)
        self.checkboxCatholic.setObjectName(u"checkboxCatholic")
        self.checkboxCatholic.setGeometry(QRect(40, 210, 78, 22))
        self.checkboxCatholic.setFont(font)
        self.checkboxCatholic.setCursor(QCursor(Qt.ClosedHandCursor))
        self.checkboxCatholic.setStyleSheet(u"background-color:#1e2329;\n"
"color:#797979;")
        self.checkboxHindu = QCheckBox(Background)
        self.checkboxHindu.setObjectName(u"checkboxHindu")
        self.checkboxHindu.setGeometry(QRect(150, 210, 101, 22))
        self.checkboxHindu.setFont(font)
        self.checkboxHindu.setCursor(QCursor(Qt.ClosedHandCursor))
        self.checkboxHindu.setStyleSheet(u"background-color:#1e2329;\n"
"color:#797979;")
        self.background2 = QLabel(Background)
        self.background2.setObjectName(u"background2")
        self.background2.setGeometry(QRect(20, 140, 231, 101))
        self.background2.setStyleSheet(u"background-color:#1e2329;\n"
"border-radius: 8px;")
        self.background1 = QLabel(Background)
        self.background1.setObjectName(u"background1")
        self.background1.setGeometry(QRect(20, 60, 231, 61))
        self.background1.setStyleSheet(u"background-color:#1e2329;\n"
"border-radius: 8px")
        self.labelGender = QLabel(Background)
        self.labelGender.setObjectName(u"labelGender")
        self.labelGender.setGeometry(QRect(50, 65, 171, 21))
        self.labelGender.setFont(font)
        self.labelGender.setStyleSheet(u"background-color:#1e2329;\n"
"color:#797979;")
        self.labelGender.setAlignment(Qt.AlignCenter)
        self.labelReligion = QLabel(Background)
        self.labelReligion.setObjectName(u"labelReligion")
        self.labelReligion.setGeometry(QRect(40, 145, 191, 21))
        self.labelReligion.setFont(font)
        self.labelReligion.setStyleSheet(u"background-color:#1e2329;\n"
"color:#797979;")
        self.labelReligion.setAlignment(Qt.AlignCenter)
        self.labelTitle = QLabel(Background)
        self.labelTitle.setObjectName(u"labelTitle")
        self.labelTitle.setGeometry(QRect(20, 15, 231, 16))
        self.labelTitle.setFont(font)
        self.labelTitle.setStyleSheet(u"color:#797979;")
        self.labelTitle.setAlignment(Qt.AlignCenter)
        self.seperator1 = QLabel(Background)
        self.seperator1.setObjectName(u"seperator1")
        self.seperator1.setGeometry(QRect(0, 40, 275, 2))
        self.seperator1.setStyleSheet(u"background-color:#797979;")
        self.seperator2 = QLabel(Background)
        self.seperator2.setObjectName(u"seperator2")
        self.seperator2.setGeometry(QRect(0, 260, 275, 2))
        self.seperator2.setStyleSheet(u"background-color:#797979;")
        self.background3 = QLabel(Background)
        self.background3.setObjectName(u"background3")
        self.background3.setGeometry(QRect(20, 280, 231, 101))
        self.background3.setStyleSheet(u"background-color:#1e2329;\n"
"border-radius: 8px;")
        self.textInput = QTextEdit(Background)
        self.textInput.setObjectName(u"textInput")
        self.textInput.setGeometry(QRect(30, 290, 211, 51))
        self.textInput.setFont(font)
        self.textInput.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.textInput.setStyleSheet(u"background-color:#2f3237;\n"
"color:#797979;\n"
"border-radius: 5px;")
        self.textInput.setFrameShape(QFrame.NoFrame)
        self.textInput.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textInput.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.startProgram = QPushButton(Background)
        self.startProgram.setObjectName(u"startProgram")
        self.startProgram.setGeometry(QRect(20, 420, 231, 24))
        self.startProgram.setCursor(QCursor(Qt.OpenHandCursor))
        self.startProgram.setStyleSheet(u"background-color:#1e2329;\n"
"color:#797979;\n"
"border-radius: 5px;")
        self.seperator3 = QLabel(Background)
        self.seperator3.setObjectName(u"seperator3")
        self.seperator3.setGeometry(QRect(0, 400, 275, 2))
        self.seperator3.setStyleSheet(u"background-color:#797979;")
        self.selectFile = QPushButton(Background)
        self.selectFile.setObjectName(u"selectFile")
        self.selectFile.setGeometry(QRect(30, 350, 211, 24))
        self.selectFile.setCursor(QCursor(Qt.ClosedHandCursor))
        self.selectFile.setStyleSheet(u"background-color:#2f3237;\n"
"color:#797979;\n"
"border-radius: 5px;")
        self.background1.raise_()
        self.background2.raise_()
        self.checkboxMale.raise_()
        self.checkboxFemale.raise_()
        self.checkboxMuslim.raise_()
        self.checkboxProtestant.raise_()
        self.checkboxCatholic.raise_()
        self.checkboxHindu.raise_()
        self.labelGender.raise_()
        self.labelReligion.raise_()
        self.labelTitle.raise_()
        self.seperator1.raise_()
        self.seperator2.raise_()
        self.background3.raise_()
        self.textInput.raise_()
        self.startProgram.raise_()
        self.seperator3.raise_()
        self.selectFile.raise_()

        self.retranslateUi(Background)

        QMetaObject.connectSlotsByName(Background)
    # setupUi

    def retranslateUi(self, Background):
        Background.setWindowTitle(QCoreApplication.translate("Background", u"Rigeru", None))
        self.checkboxMale.setText(QCoreApplication.translate("Background", u"Male", None))
        self.checkboxFemale.setText(QCoreApplication.translate("Background", u"Female", None))
        self.checkboxMuslim.setText(QCoreApplication.translate("Background", u"Muslim", None))
        self.checkboxProtestant.setText(QCoreApplication.translate("Background", u"Protestant", None))
        self.checkboxCatholic.setText(QCoreApplication.translate("Background", u"Catholic", None))
        self.checkboxHindu.setText(QCoreApplication.translate("Background", u"Hindu", None))
        self.background2.setText("")
        self.background1.setText("")
        self.labelGender.setText(QCoreApplication.translate("Background", u"Gender", None))
        self.labelReligion.setText(QCoreApplication.translate("Background", u"Religion", None))
        self.labelTitle.setText(QCoreApplication.translate("Background", u"DTMM Automated Line ", None))
        self.seperator1.setText("")
        self.seperator2.setText("")
        self.background3.setText("")
        self.textInput.setHtml(QCoreApplication.translate("Background", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'RomanC'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textInput.setPlaceholderText(QCoreApplication.translate("Background", u"Write message here ...  ", None))
        self.startProgram.setText(QCoreApplication.translate("Background", u"Start Program", None))
        self.seperator3.setText("")
        self.selectFile.setText(QCoreApplication.translate("Background", u"Select File", None))
    # retranslateUi


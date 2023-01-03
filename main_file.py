# This Python file uses the following encoding: utf-8
from sys import argv, exit
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog
from ui_form import Ui_Background
import pandas as pd
from time import sleep
import pyautogui as bot
from playsound import playsound
from os import getcwd
from os.path import abspath
from pyperclip import copy


class GUI(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Background()
        self.ui.setupUi(self)
        self.setupWidgets()

    def setupWidgets(self):
        self.male, self.female, self.Muslim, self.Protestant, self.Catholic, self.Hindu = -1, -1, -1, -1, -1, -1
        self.ui.checkboxMale.stateChanged.connect(lambda:self.stateMale())
        self.ui.checkboxFemale.stateChanged.connect(lambda:self.stateFemale())
        self.ui.checkboxMuslim.stateChanged.connect(lambda:self.stateMuslim())
        self.ui.checkboxProtestant.stateChanged.connect(lambda:self.stateProtestant())
        self.ui.checkboxCatholic.stateChanged.connect(lambda:self.stateCatholic())
        self.ui.checkboxHindu.stateChanged.connect(lambda:self.stateHindu())
        self.ui.startProgram.clicked.connect(lambda:self.get_data())
        self.ui.selectFile.clicked.connect(lambda:self.fileExplorer())
    
    def stateMale(self): self.male *= -1
    def stateFemale(self): self.female *= -1
    def stateMuslim(self): self.Muslim *= -1
    def stateProtestant(self): self.Protestant *= -1
    def stateCatholic(self): self.Catholic *= -1
    def stateHindu(self): self.Hindu *= -1
    def fileExplorer(self): self.file_paths = QFileDialog.getOpenFileNames(self, 'Open file', 'C:\\',"Image (*.jpg *.gif *.svg *.png *.jpeg);;Documents (*.txt *.pdf);;All Files (*)")[0]
        
    def get_data(self):
        data = pd.read_excel(f'{getcwd()}\\assets\\database.xlsx')
        data = data[['Name', 'Line ID', 'Gender', 'Religion']].dropna()
        
        # Gender Sort
        if self.male == -1 and self.female == 1: data = data[data['Gender'] == 'P']
        elif self.male == 1 and self.female == -1: data = data[data['Gender'] == 'L']
        elif self.male == -1 and self.female == -1: data = data[data['Gender'] == 'none']
        
        # Religion
        to_sort = []
        if self.Muslim == 1: to_sort.append("Muslim")
        if self.Protestant == 1: to_sort.append("Protestant")
        if self.Catholic == 1: to_sort.append("Catholic")
        if self.Hindu == 1: to_sort.append("Hindu")
        data = data[data['Religion'].isin(to_sort)]
        
        if not data.empty: self.main(data)
        else: playsound(f"{getcwd()}\\assets\\invalid.mp3")
        
    def main(self, data):
        text_to_send = self.ui.textInput.toPlainText()
        if text_to_send != '' or self.file_paths:
            x = []
            for a in range(3):
                sleep(3)
                for i in bot.position(): x.append(i)
                playsound(f"{getcwd()}\\assets\\ping.mp3")
            list_coordinates = x

            for ind in data.index:
                bot.click(list_coordinates[0], list_coordinates[1]) # Write Line ID
                bot.hotkey('ctrl', 'a')
                bot.press('delete')
                bot.write(data['Line ID'][ind])
                bot.write('\n')
                sleep(.1)

                bot.click(list_coordinates[2]-15, list_coordinates[3]) # Select Chat
                bot.click(list_coordinates[2], list_coordinates[3])
                bot.click(list_coordinates[2]+15, list_coordinates[3])
                sleep(.1)
                
                if text_to_send != '':
                    bot.click(list_coordinates[4], list_coordinates[5]) # Write Text
                    copy(text_to_send.replace('[Name]', data['Name'][ind]))
                    bot.hotkey('ctrl', 'v')
                    bot.write('\n')
                    sleep(.1)
                
                if self.file_paths:
                    bot.hotkey('ctrl', 'o') # Send File(s)
                    for i in range(len(self.file_paths)):
                        bot.write(f'"{abspath(self.file_paths[i])}" ')
                    bot.write('\n')
                    sleep(.5)
        else:
            playsound(f"{getcwd()}\\assets\\invalid.mp3")
        

if __name__ == "__main__":
    app = QApplication(argv)
    widget = GUI()
    widget.show()
    exit(app.exec())

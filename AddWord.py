import json
from PyQt5.QtWidgets import QApplication, QLabel, QMessageBox, QRadioButton
from PyQt5.Qt import QWidget, QGridLayout, QPushButton, QLineEdit, QMainWindow

class LLT_AddWord(QMainWindow):

    def __init__(self):
        super(LLT_AddWord, self).__init__()
        self.w = QWidget()
        self.setCentralWidget(self.w)    
        
        self.verbDic = []
        self.nounDic = []
        self.adjDic = []
        self.phraseDic = []
        self.wordList = []


        self.w.setWindowTitle("Add Word")
        self.w.setGeometry(0,0,500, 500)
        
        
        self.vRad = QRadioButton("Verb")
        self.vRad.setChecked(True)
        self.nRad = QRadioButton("Noun")
        self.aRad = QRadioButton("Adjective")
        self.pRad = QRadioButton("Phrase")
        self.okBut = QPushButton("OK")
        self.okBut.clicked.connect(self.OK)
        
        self.entryLab = QLabel("Word: ")
        self.wordEntry = QLineEdit()
        self.wordEntry.setEnabled(False)
        
        self.tranLab = QLabel("Translation: ")
        self.tranEntry = QLineEdit()
        self.tranEntry.setEnabled(False)
        
        self.checkBut = QPushButton("Check")
        self.checkBut.clicked.connect(self.check)
        self.saveBut = QPushButton("Save")
        self.saveBut.clicked.connect(self.save)
        self.clearBut = QPushButton("Clear")
        self.clearBut.clicked.connect(self.clear)
        self.newBut = QPushButton("New word")
        self.newBut.clicked.connect(self.new)
        self.exitBut = QPushButton("Exit")
        self.exitBut.clicked.connect(self.exit)
        
        grid = QGridLayout()
        
        grid.addWidget(self.vRad, 0, 0)
        grid.addWidget(self.nRad, 0, 1)
        grid.addWidget(self.aRad, 0, 2)
        grid.addWidget(self.pRad, 0, 3)
        grid.addWidget(self.okBut, 0, 4)
        
        grid.addWidget(self.entryLab, 1, 0)
        grid.addWidget(self.wordEntry, 1, 1, 1, 3)
        grid.addWidget(self.tranLab, 2, 0)
        grid.addWidget(self.tranEntry, 2, 1, 1, 3)
        
        grid.addWidget(self.checkBut, 3, 0)
        grid.addWidget(self.saveBut, 3, 1)
        grid.addWidget(self.clearBut, 3, 2)
        grid.addWidget(self.newBut, 3, 3)
        grid.addWidget(self.exitBut, 3, 4)
        
        self.getDics()
        self.setLists()
        self.w.setLayout(grid) 
        self.w.show()
        
    def OK(self):
        self.vRad.setEnabled(False)
        self.nRad.setEnabled(False)
        self.aRad.setEnabled(False)
        self.pRad.setEnabled(False)
        self.okBut.setEnabled(False)
        self.wordEntry.setEnabled(True)
        self.tranEntry.setEnabled(True)
        
    def check(self):
        word = self.wordEntry.text().upper()
        if word in self.wordList:
            msgBox = QMessageBox() 
            msgBox.setText(word + ' already in dictionary')
            msgBox.exec_();
        else:
            msgBox = QMessageBox() 
            msgBox.setText(word + ' not in dictionary yet')
            msgBox.exec_();

    def save(self):
        spanWord = self.wordEntry.text().upper()
        tranWord = self.tranEntry.text().upper()
        if spanWord in self.wordList:
            msgBox = QMessageBox() 
            msgBox.setText(spanWord + ' already in dictionary')
            msgBox.exec_();
        else:
            self.wordList.append(spanWord)
            newWord = [spanWord,tranWord]
            self.wordEntry.setEnabled(False)
            self.tranEntry.setEnabled(False)
            if self.vRad.isChecked():
                self.verbDic.append(newWord)
                v = open('verb.txt','w')
                json.dump(self.verbDic, v)
                v.close() 
            elif self.nRad.isChecked():
                self.nounDic.append(newWord)
                n = open('noun.txt','w')
                json.dump(self.nounDic, n)
                n.close()
            elif self.aRad.isChecked():
                self.adjDic.append(newWord)
                a = open('adj.txt','w')
                json.dump(self.adjDic, a)
                a.close()
            elif self.pRad.isChecked():
                self.phraseDic.append(newWord)
                p = open('phrase.txt','w')
                json.dump(self.phraseDic, p)
                p.close()
                
            else:
                msgBox = QMessageBox() 
                msgBox.setText("You must select a dictionary before saving word.")
                msgBox.exec_();
                
    def clear(self):
        self.vRad.setEnabled(True)
        self.nRad.setEnabled(True)
        self.aRad.setEnabled(True)
        self.pRad.setEnabled(True)
        self.okBut.setEnabled(True)
        self.wordEntry.setEnabled(False)
        self.tranEntry.setEnabled(False)
        self.wordEntry.clear()
        self.tranEntry.clear()
    
    def new(self):
        self.vRad.setEnabled(True)
        self.nRad.setEnabled(True)
        self.aRad.setEnabled(True)
        self.pRad.setEnabled(True)
        self.okBut.setEnabled(True)
        self.wordEntry.setEnabled(False)
        self.tranEntry.setEnabled(False)
        self.wordEntry.clear()
        self.tranEntry.clear()

    def exit(self):
        confirm = QMessageBox.question(self.w, 'Quit', 'Are you sure you want to exit?', QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.close()
        else:
            pass

    def getDics(self):
        try:
            v=open('verb.txt','r')
            self.verbDic=json.load(v)
            v.close()
        except:
            self.verbDic = []

        try:
            n=open('noun.txt','r')
            self.nounDic=json.load(n)
            n.close()
        except:
            self.nounDic = []
    
        try:
            p=open('phrase.txt','r')
            self.phraseDic=json.load(p)
            p.close()
        except:
            self.phraseDic = []
                
        try:
            a=open('adj.txt','r')
            self.adjDic=json.load(a)
            a.close()
        except:
            self.phraseDic = []
            
            
    def setLists(self):
        for item in self.verbDic:
            self.wordList.append(item[0])
        for item in self.nounDic:
            self.wordList.append(item[0])
        for item in self.phraseDic:
            self.wordList.append(item[0])
        for item in self.adjDic:
            self.wordList.append(item[0])
            
if __name__ == '__main__':
    app = QApplication([])
    gui = LLT_AddWord()
    gui.show()
    app.exec_()

import json
from PyQt5.QtWidgets import QApplication, QLabel, QMessageBox, QRadioButton
from PyQt5.Qt import QWidget, QGridLayout, QPushButton, QLineEdit, QMainWindow

class LLT_EditWord(QMainWindow):

    def __init__(self):
        super(LLT_EditWord, self).__init__()
        self.w = QWidget()
        self.setCentralWidget(self.w)    
        
        self.verbDic = []
        self.nounDic = []
        self.adjDic = []
        self.phraseDic = []
        self.wordList = []
        self.verbList = []
        self.nounList = []
        self.adjList = []
        self.phraseList = []
        
        self.index = int(0)

        self.w.setWindowTitle("Edit Word")
        self.w.setGeometry(0,0,500, 500)
        
        
        self.vRad = QRadioButton("Verb")
        self.vRad.setChecked(True)
        self.nRad = QRadioButton("Noun")
        self.aRad = QRadioButton("Adjective")        
        self.pRad = QRadioButton("Phrase")
        
        self.okBut = QPushButton("OK")
        self.okBut.clicked.connect(self.OK)
        
        self.lookLab = QLabel("Lookup: ")
        self.lookEntry = QLineEdit()
        self.lookEntry.setEnabled(False)
        self.lookBut = QPushButton("Search")
        self.lookBut.clicked.connect(self.search)
        self.lookBut.setEnabled(False)
        
        self.entryLab = QLabel("Word: ")
        self.wordEntry = QLineEdit()
        self.wordEntry.setEnabled(False)
        
        self.tranLab = QLabel("Translation: ")
        self.tranEntry = QLineEdit()
        self.tranEntry.setEnabled(False)
        
        self.saveBut = QPushButton("Save")
        self.saveBut.clicked.connect(self.save)
        self.clearBut = QPushButton("Reset")
        self.clearBut.clicked.connect(self.reset)
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
        
        grid.addWidget(self.lookLab, 1, 0)
        grid.addWidget(self.lookEntry, 1, 1, 1, 2)
        grid.addWidget(self.lookBut, 1, 4)
        
        grid.addWidget(self.entryLab, 2, 0)
        grid.addWidget(self.wordEntry, 2, 1, 1, 3)
        grid.addWidget(self.tranLab, 3, 0)
        grid.addWidget(self.tranEntry, 3, 1, 1, 3)
        
        grid.addWidget(self.saveBut, 4, 0)
        grid.addWidget(self.clearBut, 4, 1)
        grid.addWidget(self.newBut, 4, 2)
        grid.addWidget(self.exitBut, 4, 3)
        
        self.getDics()
        self.setLists()
        self.w.setLayout(grid) 
        self.w.show()

    def search(self):
        searchWord = self.lookEntry.text().upper()
        currentDic = []
        currentList = []
            
        if self.vRad.isChecked():
            currentDic = self.verbDic
            currentList = self.verbList
        elif self.nRad.isChecked():
            currentDic = self.nounDic
            currentList = self.nounList
        elif self.aRad.isChecked():
            currentDic = self.adjDic
            currentList = self.adjList
        elif self.pRad.isChecked():
            currentDic = self.phraseDic
            currentList = self.phraseList
        else: 
            msgBox = QMessageBox() 
            msgBox.setText("You must select a dictionary before continuing.")
            msgBox.exec_()
            self.vRad.setEnabled(True)
            self.nRad.setEnabled(True)
            self.aRad.setEnabled(True)
            self.pRad.setEnabled(True)
            self.lookEntry.setEnabled(False)
            self.lookBut.setEnabled(False)
            self.wordEntry.setEnabled(False)
            self.tranEntry.setEnabled(False)
        
        if searchWord in self.wordList:
            self.lookEntry.setEnabled(False)
            self.lookBut.setEnabled(False)
            self.wordEntry.setEnabled(True)
            self.tranEntry.setEnabled(True)
            self.index = currentList.index(searchWord)
            oldWord = currentDic[self.index]
            self.wordEntry.setPlaceholderText(oldWord[0])
            self.tranEntry.setPlaceholderText(oldWord[1])
                        
        else:
            msgBox = QMessageBox() 
            msgBox.setText("Word not currently saved in dictionary.")
            msgBox.exec_(); 
        

            
    def OK(self):
        self.vRad.setEnabled(False)
        self.nRad.setEnabled(False)
        self.aRad.setEnabled(False)
        self.pRad.setEnabled(False)
        self.lookEntry.setEnabled(True)
        self.lookBut.setEnabled(True)

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
                self.verbDic[self.index]= newWord
                v = open('verb.txt','w')
                json.dump(self.verbDic, v)
                v.close() 
            elif self.nRad.isChecked():
                self.nounDic[self.index]= newWord
                n = open('noun.txt','w')
                json.dump(self.nounDic, n)
                n.close()
            elif self.aRad.isChecked():
                self.adjDic[self.index]= newWord
                a = open('adj.txt','w')
                json.dump(self.adjDic, a)
                a.close()
            elif self.pRad.isChecked():
                self.phraseDic[self.index]= newWord
                p = open('phrase.txt','w')
                json.dump(self.phraseDic, p)
                p.close()
                
            else:
                msgBox = QMessageBox() 
                msgBox.setText("You must select a dictionary before saving word.")
                msgBox.exec_();
                
    def reset(self):
        self.vRad.setEnabled(True)
        self.nRad.setEnabled(True)
        self.aRad.setEnabled(True)
        self.pRad.setEnabled(True)
        self.lookEntry.setEnabled(False)
        self.lookBut.setEnabled(False)
        self.wordEntry.setEnabled(False)
        self.tranEntry.setEnabled(False)
        self.wordEntry.clear()
        self.tranEntry.clear()
        self.lookEntry.setPlaceholderText('')
        self.wordEntry.setPlaceholderText('')
        self.tranEntry.setPlaceholderText('')    
    
    def new(self):
        self.vRad.setEnabled(True)
        self.nRad.setEnabled(True)
        self.aRad.setEnabled(True)
        self.pRad.setEnabled(True)
        self.wordEntry.setEnabled(False)
        self.tranEntry.setEnabled(False)
        self.wordEntry.clear()
        self.tranEntry.clear()
        self.lookEntry.setPlaceholderText('')
        self.wordEntry.setPlaceholderText('')
        self.tranEntry.setPlaceholderText('')

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
            self.verbList.append(item[0])
        for item in self.nounDic:
            self.wordList.append(item[0])
            self.nounList.append(item[0])
        for item in self.adjDic:
            self.wordList.append(item[0])
            self.adjList.append(item[0])
        for item in self.phraseDic:
            self.wordList.append(item[0])
            self.phraseList.append(item[0])
        
if __name__ == '__main__':
    app = QApplication([])
    gui = LLT_EditWord()
    gui.show()
    app.exec_()
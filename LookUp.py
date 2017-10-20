import json
from PyQt5.QtWidgets import QApplication, QLabel, QMessageBox
from PyQt5.Qt import QWidget, QGridLayout, QPushButton, QLineEdit, QMainWindow

class LLT_Lookup(QMainWindow):

    def __init__(self):
        super(LLT_Lookup, self).__init__()
        self.w = QWidget()
        self.setCentralWidget(self.w)    
        
        self.verbDic = []
        self.nounDic = []
        self.adjDic = []
        self.phraseDic = []
        self.wordList = []
        self.wordDic = []
        self.index = int(0)

        self.w.setWindowTitle("Word Lookup")
        self.w.setGeometry(0,0,500, 500)
             
        self.lookLab = QLabel("Lookup: ")
        self.lookEntry = QLineEdit()
        self.lookBut = QPushButton("Search")
        self.lookBut.clicked.connect(self.search)
        
        self.wordLab = QLabel("Word: ")
        self.resultWord = QLabel() 
        self.tranLab = QLabel("Translation: ")
        self.resultTran = QLabel()
        
        self.newBut = QPushButton("New Search")
        self.newBut.clicked.connect(self.new)
        self.exitBut = QPushButton("Exit")
        self.exitBut.clicked.connect(self.exit)
        
        grid = QGridLayout()
        
        grid.addWidget(self.lookLab, 0, 0)
        grid.addWidget(self.lookEntry, 0, 1, 1, 2)
        grid.addWidget(self.lookBut, 0, 3)
        
        grid.addWidget(self.wordLab, 1, 0)
        grid.addWidget(self.resultWord, 1, 1, 1, 3)
        grid.addWidget(self.tranLab, 2, 0)
        grid.addWidget(self.resultTran, 2, 1, 1, 3)
        
        grid.addWidget(self.newBut, 3, 0)
        grid.addWidget(self.exitBut, 3, 3)
        
        self.getDics()
        self.setLists()
        self.w.setLayout(grid) 
        self.w.show()

    def search(self):
        searchWord = self.lookEntry.text().upper().strip()
        
        if searchWord in self.wordList:
            self.lookEntry.setEnabled(False)
            self.lookBut.setEnabled(False)
            
            self.index = self.wordList.index(searchWord)
            foundWord = self.wordDic[self.index]
            self.resultWord.setText(foundWord[0])
            self.resultTran.setText(foundWord[1])
                        
        else:
            msgBox = QMessageBox() 
            msgBox.setText("Word not currently saved in dictionary.")
            msgBox.exec_(); 
    
    
    def new(self):
        self.lookEntry.setEnabled(True)
        self.lookBut.setEnabled(True)
        self.resultWord.setText('')
        self.resultTran.setText('')
        self.lookEntry.clear()
        
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
            self.wordDic.append(item)
        for item in self.nounDic:
            self.wordList.append(item[0])
            self.wordDic.append(item)
        for item in self.adjDic:
            self.wordList.append(item[0])
            self.wordDic.append(item)
        for item in self.phraseDic:
            self.wordList.append(item[0])
            self.wordDic.append(item)
        
if __name__ == '__main__':
    app = QApplication([])
    gui = LLT_Lookup()
    gui.show()
    app.exec_()
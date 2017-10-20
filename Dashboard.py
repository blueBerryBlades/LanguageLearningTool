import json
from PyQt5.QtWidgets import QApplication, QLabel, QMessageBox
from PyQt5.Qt import QWidget, QGridLayout, QPushButton, QMainWindow
from Flash import LLT_Flash
from MC import LLT_MC
from AddWord import LLT_AddWord
from EditWord import LLT_EditWord
from LookUp import LLT_Lookup
from ConjAdd import LLT_ConjAdd
from ConjRev import LLT_ConjRev

class LLT_Dashboard(QMainWindow):

    def __init__(self):
        super(LLT_Dashboard, self).__init__()
        self.w = QWidget()
        self.setCentralWidget(self.w)

        self.setWindowTitle("Emma's LLT")
        self.setGeometry(0,0,500, 500)
        
        self.verbDic = []
        self.nounDic = []
        self.adjDic = []
        self.phraseDic = []
        self.getDics()
        
        self.topLabel = QLabel("LLT Dashboard")
        self.flashLab = QLabel("Flashcards")
        self.MCLab = QLabel("Multiple Choice")
        self.dicLab = QLabel("Dictionary")
        
        self.flashVBut = QPushButton("Verbs")
        self.flashVBut.setMinimumWidth(150)
        self.flashVBut.setMinimumHeight(100)
        self.flashVBut.clicked.connect(lambda: self.flash("Verbs", self.verbDic))
        self.flashNBut = QPushButton("Nouns")
        self.flashNBut.setMinimumWidth(150)
        self.flashNBut.setMinimumHeight(100)
        self.flashNBut.clicked.connect(lambda: self.flash("Nouns", self.nounDic))
        self.flashABut = QPushButton("Adjectives")
        self.flashABut.setMinimumWidth(150)
        self.flashABut.setMinimumHeight(100)
        self.flashABut.clicked.connect(lambda: self.flash("Adjectives", self.adjDic))
        self.flashPBut = QPushButton("Phrases")
        self.flashPBut.setMinimumWidth(150)
        self.flashPBut.setMinimumHeight(100)
        self.flashPBut.clicked.connect(lambda: self.flash("Phrases", self.phraseDic))
        
        self.MCVBut = QPushButton("Verbs")
        self.MCVBut.setMinimumWidth(150)
        self.MCVBut.setMinimumHeight(100)
        self.MCVBut.clicked.connect(lambda: self.MC("Verbs", self.verbDic))
        self.MCNBut = QPushButton("Nouns")
        self.MCNBut.setMinimumWidth(150)
        self.MCNBut.setMinimumHeight(100)
        self.MCNBut.clicked.connect(lambda: self.MC("Nouns", self.nounDic))
        self.MCABut = QPushButton("Adjectives")
        self.MCABut.setMinimumWidth(150)
        self.MCABut.setMinimumHeight(100)
        self.MCABut.clicked.connect(lambda: self.MC("Adjectives", self.adjDic))
        self.MCPBut = QPushButton("Phrases")
        self.MCPBut.setMinimumWidth(150)
        self.MCPBut.setMinimumHeight(100)
        self.MCPBut.clicked.connect(lambda: self.MC("Phrases", self.phraseDic))
        
        self.addWordBut = QPushButton("Add word")
        self.addWordBut.setMinimumWidth(150)
        self.addWordBut.setMinimumHeight(100)
        self.addWordBut.clicked.connect(self.addWord)
        self.editWordBut = QPushButton("Edit word")
        self.editWordBut.setMinimumWidth(150)
        self.editWordBut.setMinimumHeight(100)
        self.editWordBut.clicked.connect(self.editWord)
        self.lookUpWord = QPushButton("Word Lookup")
        self.lookUpWord.setMinimumWidth(150)
        self.lookUpWord.setMinimumHeight(100)
        self.lookUpWord.clicked.connect(self.lookup)
        self.conjAddBut = QPushButton("Add Conjugation \nTable")
        self.conjAddBut.setMinimumWidth(150)
        self.conjAddBut.setMinimumHeight(100)
        self.conjAddBut.clicked.connect(self.conjAdd)
        self.conjRevBut = QPushButton("Review \nConjugation")
        self.conjRevBut.setMinimumWidth(150)
        self.conjRevBut.setMinimumHeight(100)
        self.conjRevBut.clicked.connect(self.conjRev)
        
        self.quitBut = QPushButton("Quit")
        self.quitBut.clicked.connect(self.quit)
        self.quitBut.setMinimumWidth(150)
        self.quitBut.setMinimumHeight(100)
        
        grid = QGridLayout()
        
        grid.addWidget(self.topLabel, 0, 1, 1, 2)
        
        grid.addWidget(self.flashLab, 1, 0, 1, 2)
        grid.addWidget(self.flashVBut, 2, 0)
        grid.addWidget(self.flashNBut, 2, 1)
        grid.addWidget(self.flashABut, 2, 2)
        grid.addWidget(self.flashPBut, 2, 3)
        
        grid.addWidget(self.MCLab, 3, 0, 1, 2)
        grid.addWidget(self.MCVBut, 4, 0)
        grid.addWidget(self.MCNBut, 4, 1)
        grid.addWidget(self.MCABut, 4, 2)
        grid.addWidget(self.MCPBut, 4, 3)
        
        grid.addWidget(self.dicLab, 5, 0, 1, 2)
        grid.addWidget(self.addWordBut, 6, 0)
        grid.addWidget(self.editWordBut, 6, 1)
        grid.addWidget(self.conjAddBut, 6, 2)
        grid.addWidget(self.conjRevBut, 6, 3)
        
        grid.addWidget(self.quitBut, 7, 0)
        grid.addWidget(self.lookUpWord, 7, 1)
        
        self.w.setLayout(grid) 
        
    def quit(self):
        confirm = QMessageBox.question(self.w, 'Quit', 'Are you sure you want to exit?', QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.close()
        else:
            pass
        
    def addWord(self):
        self.addWordGUI = LLT_AddWord()
        self.addWordGUI.show()
        
    def editWord(self):
        self.editWordGUI = LLT_EditWord()
        self.editWordGUI.show()
    
    def flash(self, title, dic):
        self.flashGUI = LLT_Flash(title, dic)
        self.flashGUI.show()    
    
    def MC(self, title, dic):
        self.MCGUI = LLT_MC(title, dic)
        self.MCGUI.show()
    
    def lookup(self):
        self.lookupGUI = LLT_Lookup()
        self.lookupGUI.show()
    
    def conjAdd(self):
        self.conjAddGUI = LLT_ConjAdd()
        self.conjAddGUI.show() 
    
    def conjRev(self):
        self.conjRevGUI = LLT_ConjRev()
        self.conjRevGUI.show()
    
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
        
if __name__ == '__main__':
    app = QApplication([])
    gui = LLT_Dashboard()
    gui.show()
    app.exec_()
    
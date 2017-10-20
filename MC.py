import random
from PyQt5.QtCore import Qt
from PyQt5.Qt import QMainWindow, QWidget, QApplication, QLabel, QRadioButton,\
    QPushButton, QMessageBox, QVBoxLayout, QHBoxLayout, QButtonGroup, QFont

class LLT_MC(QMainWindow):

    def __init__(self, dicTitle, dicList):
        super(LLT_MC, self).__init__()
        self.w = QWidget()
        self.setCentralWidget(self.w)
        
        self.title = dicTitle
        self.wordList = dicList    
        
        self.setWindowTitle("Multiple Choice")
        self.setGeometry(0,0,300, 400)
        
        self.currentWordS = random.sample(self.wordList, 3)
        self.currentQWord = self.currentWordS[0][0]
        self.currentAWord = self.currentWordS[0][1]
        
        self.topLabel = QLabel("Multiple Choice: " + str(dicTitle)) 
        self.wordLabel = QLabel()
        self.wordLabel.setFont(QFont('Times New Roman', 16))
        self.wordLabel.setAlignment(Qt.AlignCenter)
        self.resultLabel = QLabel()
        self.resultLabel.setAlignment(Qt.AlignCenter)
        
        self.aRad = QRadioButton()
        self.bRad = QRadioButton()
        self.cRad = QRadioButton()
        self.group = QButtonGroup()
        self.group.addButton(self.aRad)
        self.group.addButton(self.bRad)
        self.group.addButton(self.cRad)
        
        self.checkBut = QPushButton("Check")
        self.checkBut.setMinimumWidth(100)
        self.checkBut.setMinimumHeight(70)
        self.checkBut.clicked.connect(self.check)
        self.nextBut = QPushButton("Next Word")
        self.nextBut.setMinimumWidth(100)
        self.nextBut.setMinimumHeight(70)
        self.nextBut.clicked.connect(self.next)
        self.exitBut = QPushButton("Exit")
        self.exitBut.setMinimumWidth(130)
        self.exitBut.setMinimumHeight(70)
        self.exitBut.clicked.connect(self.exit)
        
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.checkBut)
        self.hbox.addWidget(self.nextBut)
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.topLabel)
        self.vbox.addWidget(self.wordLabel)
        self.vbox.addWidget(self.aRad)
        self.vbox.addWidget(self.bRad)
        self.vbox.addWidget(self.cRad)
        self.vbox.addWidget(self.resultLabel)
        self.vbox.addLayout(self.hbox)
        self.vbox.addWidget(self.exitBut)
        
        self.w.setLayout(self.vbox)
        self.setWord()
        
    #define methods
    
    def setWord(self):
        newText = []
        for item in self.currentWordS:
            newText.append(item[1])   
        
        random.shuffle(newText)
        
        self.group.setExclusive(False)     
        self.aRad.setText(newText[0])
        self.bRad.setText(newText[1])
        self.cRad.setText(newText[2])
        self.wordLabel.setText(self.currentQWord)
        self.group.setExclusive(True)
        
    def check(self):
        if self.aRad.isChecked() and self.aRad.text() == self.currentAWord:
            self.resultLabel.setText("CORRECT")
        elif self.aRad.isChecked() and self.aRad.text() != self.currentAWord:
            self.resultLabel.setText("Try again")
        if self.bRad.isChecked() and self.bRad.text() == self.currentAWord:
            self.resultLabel.setText("CORRECT")
        elif self.bRad.isChecked() and self.bRad.text() != self.currentAWord:
            self.resultLabel.setText("Try again")
        if self.cRad.isChecked() and self.cRad.text() == self.currentAWord:
            self.resultLabel.setText("CORRECT")
        elif self.cRad.isChecked() and self.cRad.text() != self.currentAWord:
            self.resultLabel.setText("Try again")
        
    def next(self):
        self.currentWordS = random.sample(self.wordList, 3)
        self.currentQWord = self.currentWordS[0][0]
        self.currentAWord = self.currentWordS[0][1]
        
        self.wordLabel.setText(self.currentQWord)
        self.resultLabel.setText('')
        
        self.group.setExclusive(False)
        self.aRad.setChecked(False)
        self.bRad.setChecked(False)
        self.cRad.setChecked(False)
        self.group.setExclusive(True)
        
        newText = []
        for item in self.currentWordS:
            newText.append(item[1])
        random.shuffle(newText)
        self.aRad.setText(newText[0])
        self.bRad.setText(newText[1])
        self.cRad.setText(newText[2])
        
    def exit(self):
        confirm = QMessageBox.question(self.w, 'Quit', 'Are you sure you want to exit?', QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.close()
        else:
            pass
        
if __name__ == '__main__':
    app = QApplication([])
    gui = LLT_MC()
    gui.show()
    app.exec_()
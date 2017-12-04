import random
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMessageBox
from PyQt5.Qt import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QMainWindow,\
    QFont

class LLT_Flash(QMainWindow):

    def __init__(self, dicTitle, dicList):
        super(LLT_Flash, self).__init__()
        self.w = QWidget()
        
        self.setCentralWidget(self.w)
        
        self.setWindowTitle("Flashcards")
        self.setGeometry(0,0,300, 250)
        
        self.title = dicTitle
        self.wordList = dicList
        self.currentWord = random.choice(self.wordList)
        self.currentWord0 = self.currentWord[0]
        self.currentWord1 = self.currentWord[1]
        
        self.titleLab = QLabel("FLashcards: " + str(dicTitle))
        self.wordLab = QLabel()
        self.wordLab.setFont(QFont('Times New Roman', 16))
        self.wordLab.setAlignment(Qt.AlignCenter)
        self.wordLab.setText(self.currentWord[0])
        
        self.flipBut = QPushButton("Flip")
        self.flipBut.setMinimumWidth(100)
        self.flipBut.setMinimumHeight(70)
        self.flipBut.clicked.connect(self.flip)
        
        self.nextBut = QPushButton("Next")
        self.nextBut.setMinimumWidth(100)
        self.nextBut.setMinimumHeight(70)
        self.nextBut.clicked.connect(self.next)
                
        self.exitBut = QPushButton("Exit")
        self.exitBut.setMinimumWidth(100)
        self.exitBut.setMinimumHeight(70)
        self.exitBut.clicked.connect(self.exit)
        
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.flipBut)
        self.hbox.addWidget(self.nextBut)
        self.hbox.addWidget(self.exitBut)
        
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.titleLab)
        self.vbox.addWidget(self.wordLab)
        self.vbox.addLayout(self.hbox)
        
        self.w.setLayout(self.vbox) 
        

    def flip(self):
        if self.wordLab.text() == self.currentWord0:
            self.wordLab.setText(self.currentWord1)
        elif self.wordLab.text() == self.currentWord1:
            self.wordLab.setText(self.currentWord0)
             
    def next(self):
        self.currentWord = random.choice(self.wordList)
        self.currentWord0 = self.currentWord[0]
        self.currentWord1 = self.currentWord[1]
        self.wordLab.setText(self.currentWord0)
        
    
    def exit(self):
        confirm = QMessageBox.question(self.w, 'Quit', 'Are you sure you want to exit?', QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.close()
        else:
            pass

if __name__ == '__main__':
    app = QApplication([])
    flashGUI = LLT_Flash()
    flashGUI.show()
    app.exec_()
        

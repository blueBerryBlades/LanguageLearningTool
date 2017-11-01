from PyQt5.Qt import QMainWindow, QWidget, QApplication, QMessageBox, QLabel,\
    QLineEdit, QGridLayout, QPushButton
from PyQt5.QtCore import Qt
import json

class LLT_ConjAdd(QMainWindow):

    def __init__(self):
        super(LLT_ConjAdd, self).__init__()
        self.w = QWidget()
        self.setCentralWidget(self.w)    
        
        #construct GUI
        self.setWindowTitle("Verb Conjugations")
        self.setGeometry(0,0,900, 600)
        
        self.conjDicList = []
        self.wordList = []
        self.newDic = {'INF':'', 'IND':'', 'SUB':'','IMP':''}
        
        self.headingLab = QLabel("Add New Conjugation Table")
        self.wordInfLab = QLabel("Infinitive")
        self.wordInfLab.setAlignment(Qt.AlignRight)
        self.infEntry = QLineEdit()
        
        #INDICATIVE FORM TABLE
        self.indLab = QLabel("Indicative")
        self.indYoLab = QLabel("Yo")
        self.indYoLab.setAlignment(Qt.AlignRight)
        self.indTuLab = QLabel("Tú")
        self.indTuLab.setAlignment(Qt.AlignRight)
        self.indUstLab = QLabel("Él/la, Ud")
        self.indUstLab.setAlignment(Qt.AlignRight)
        self.indNosLab = QLabel("Nosotros")
        self.indNosLab.setAlignment(Qt.AlignRight)
        self.indUstdsLab = QLabel("Ellos/as, Uds")
        self.indUstdsLab.setAlignment(Qt.AlignRight)
        
        self.indPresLab = QLabel("Present")
        self.indPretLab = QLabel("Preterite")
        self.indImpLab = QLabel("Imperfect")
        self.indFutLab = QLabel("Future")
        self.indCondLab = QLabel("Conditional")
        
        self.entryGridInd = QGridLayout()
        for i in range(5):
            for j in range(5):
                self.entry =  QLineEdit()
                self.entryGridInd.addWidget(self.entry, i, j)
        
        #SUBJUNCTIVE FORM TABLE
        self.subLab = QLabel("Subjunctive")
        self.subYoLab = QLabel("Yo")
        self.subYoLab.setAlignment(Qt.AlignRight)
        self.subTuLab = QLabel("Tú")
        self.subTuLab.setAlignment(Qt.AlignRight)
        self.subUstLab = QLabel("Él/la, Ud")
        self.subUstLab.setAlignment(Qt.AlignRight)
        self.subNosLab = QLabel("Nosotros/as")
        self.subNosLab.setAlignment(Qt.AlignRight)
        self.subUstdsLab = QLabel("Ellos/as, Uds")
        self.subUstdsLab.setAlignment(Qt.AlignRight)
        
        self.subPresLab = QLabel("Present")
        self.subImpLab = QLabel("Imperfect")
        self.subFutLab = QLabel("Future")
        
        self.entryGridSub = QGridLayout()
        for i in range(5):
            for j in range(3):
                self.entry =  QLineEdit()
                self.entryGridSub.addWidget(self.entry, i, j)
                
        #IMPERATIVE FORM TABLE
        self.impvLab = QLabel("Imperative")
        self.impvTu = QLabel("Tú")
        self.impvTu.setAlignment(Qt.AlignRight)
        self.impvUd = QLabel("Usted")
        self.impvUd.setAlignment(Qt.AlignRight)
        self.impvNos = QLabel("Nosotros/as")
        self.impvNos.setAlignment(Qt.AlignRight)
        self.impvUdes = QLabel("Ustedes")
        self.impvUdes.setAlignment(Qt.AlignRight)
        
        self.impvAffLab = QLabel("Affirmative")
        self.impvNegLab = QLabel("Negative")
        
        self.entryGridImpv = QGridLayout()
        for i in range(4):
            for j in range(2):
                self.entry =  QLineEdit()
                self.entryGridImpv.addWidget(self.entry, i, j)
         
        self.saveBut = QPushButton("Save")
        self.saveBut.clicked.connect(self.save)
        self.newBut = QPushButton("New Word")
        self.newBut.clicked.connect(self.new)
        self.clearBut = QPushButton("Clear")
        self.clearBut.clicked.connect(self.clear)
        self.quitBut = QPushButton("Quit")
        self.quitBut.clicked.connect(self.quit)
        
        self.theGrid = QGridLayout()
        
        self.theGrid.addWidget(self.headingLab, 0,0)
        self.theGrid.addWidget(self.wordInfLab, 1, 0)
        self.theGrid.addWidget(self.infEntry, 1, 1)
        
        self.theGrid.addWidget(self.indLab, 3, 0)
        self.theGrid.addWidget(self.indPresLab, 3, 1)
        self.theGrid.addWidget(self.indPretLab, 3, 2)
        self.theGrid.addWidget(self.indImpLab, 3, 3)
        self.theGrid.addWidget(self.indFutLab, 3, 4)
        self.theGrid.addWidget(self.indCondLab, 3, 5)
        self.theGrid.addWidget(self.indYoLab, 4, 0)
        self.theGrid.addWidget(self.indTuLab, 5, 0)
        self.theGrid.addWidget(self.indUstLab, 6, 0)
        self.theGrid.addWidget(self.indNosLab, 7, 0)
        self.theGrid.addWidget(self.indUstdsLab, 8, 0)
        self.theGrid.addLayout(self.entryGridInd, 4, 1, 5, 5)
        
        self.theGrid.addWidget(self.subLab, 11, 0)
        self.theGrid.addWidget(self.subPresLab, 11, 1)
        self.theGrid.addWidget(self.subImpLab, 11, 2)
        self.theGrid.addWidget(self.subFutLab, 11, 3)
        self.theGrid.addWidget(self.subYoLab, 12, 0)
        self.theGrid.addWidget(self.subTuLab, 13, 0)
        self.theGrid.addWidget(self.subUstLab, 14, 0)
        self.theGrid.addWidget(self.subNosLab, 15, 0)
        self.theGrid.addWidget(self.subUstdsLab, 16, 0)
        self.theGrid.addLayout(self.entryGridSub, 12, 1, 5, 3)
       
        self.theGrid.addWidget(self.impvLab, 19, 0)
        self.theGrid.addWidget(self.impvAffLab, 19, 1)
        self.theGrid.addWidget(self.impvNegLab, 19, 2)
        self.theGrid.addWidget(self.impvTu, 20, 0)
        self.theGrid.addWidget(self.impvUd, 21, 0)
        self.theGrid.addWidget(self.impvNos, 22, 0)
        self.theGrid.addWidget(self.impvUdes, 23, 0)
        self.theGrid.addLayout(self.entryGridImpv, 20, 1, 4, 2)
        
        self.theGrid.addWidget(self.saveBut, 20, 5)
        self.theGrid.addWidget(self.clearBut, 21, 5)
        self.theGrid.addWidget(self.newBut, 22, 5)
        self.theGrid.addWidget(self.quitBut, 23, 5)
        
        for i in range(24):
            self.theGrid.setRowStretch(i, 1)
        for j in range(6):
            self.theGrid.setColumnStretch(j, 1)
        self.w.setLayout(self.theGrid)
        self.getDic()
        
    
    def save(self):
        infinitive = self.infEntry.text().upper()
        indList = []
        subList = []
        impList = []
        for i in range(self.entryGridInd.count()):
            item = self.entryGridInd.itemAt(i)
            child =  item.widget()
            indList.append(child.text().upper())
        
        for i in range(self.entryGridSub.count()):
            item = self.entryGridSub.itemAt(i)
            child =  item.widget()
            subList.append(child.text().upper())
        
        for i in range(self.entryGridImpv.count()):
            item = self.entryGridImpv.itemAt(i)
            child =  item.widget()
            impList.append(child.text().upper())
        
        self.newDic['INF'] = infinitive
        self.newDic['IND'] = indList
        self.newDic['SUB'] = subList
        self.newDic['IMP'] = impList
        
        if infinitive in self.wordList:
            msgBox = QMessageBox() 
            msgBox.setText(infinitive + ' already in dictionary')
            msgBox.exec_();
        else:
            self.wordList.append(infinitive)
            self.conjDicList.append(self.newDic)
            c = open('conj.txt','w')
            json.dump(self.conjDicList, c)
            c.close()
        msgBox = QMessageBox() 
        msgBox.setText(infinitive + ' has been saved')
        msgBox.exec_();
    
    def new(self):
          confirm = QMessageBox.question(self.w, 'New Word', 'Are you sure you want to clear all entries \nand start a new word?', QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.infEntry.clear()
            for i in range(self.entryGridInd.count()):
                item = self.entryGridInd.itemAt(i)
                child =  item.widget()
                child.clear()
            for i in range(self.entryGridSub.count()):
                item = self.entryGridSub.itemAt(i)
                child =  item.widget()
                child.clear()
            for i in range(self.entryGridImpv.count()):
                item = self.entryGridImpv.itemAt(i)
                child =  item.widget()
                child.clear()
        else:
            pass
    
    def clear(self):
        confirm = QMessageBox.question(self.w, 'Clear', 'Are you sure you want to clear all entries?', QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.infEntry.clear()
            for i in range(self.entryGridInd.count()):
                item = self.entryGridInd.itemAt(i)
                child =  item.widget()
                child.clear()
            for i in range(self.entryGridSub.count()):
                item = self.entryGridSub.itemAt(i)
                child =  item.widget()
                child.clear()
            for i in range(self.entryGridImpv.count()):
                item = self.entryGridImpv.itemAt(i)
                child =  item.widget()
                child.clear()
        else:
            pass
        
    
    def quit(self):
        confirm = QMessageBox.question(self.w, 'Quit', 'Are you sure you want to exit?', QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.close()
        else:
            pass
    
    def getDic(self):
        try:
            c=open('conj.txt','r')
            self.conjDicList=json.load(c)
            c.close()
        except:
            self.conjDicList = []
        if len(self.conjDicList) > 0:
            for item in self.conjDicList:
                self.wordList.append(item['INF'])
        
        
if __name__ == '__main__':
    app = QApplication([])
    gui = LLT_ConjAdd()
    gui.show()
    app.exec_()
    
    

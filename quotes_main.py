from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtCore import pyqtSlot
import sys
from quotes_ui import Ui_MainWindow

class QuotesApp(QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        
        self.quotes = []
        
        self.add_quote_btn.clicked.connect(self.add_quote)
        self.list_quotes_btn.clicked.connect(self.list_quotes)
        self.save_quotes_btn.clicked.connect(self.save_quotes)
        
        self.actionExit.triggered.connect(self.exit)
          
    def add_quote(self):
        
        self.quotes.append('"{}" - {}'.format(self.quote.toPlainText(),self.author.text()))
         
    def list_quotes(self):
        name = QFileDialog.getOpenFileName(self, 'Open Quotes')
        file = open(name[0],'r')
        self.display_quotes.setText(file.read())
        file.close()
      
    def save_quotes(self):
        name = QFileDialog.getSaveFileName(self, 'Save Quotes')
        file = open(name[0],'a')
        file.write("\n".join(self.quotes))
        file.close()
        
    def exit(self):
        sys.exit()
        
def main():
    app = QApplication(sys.argv)
    quotes_app = QuotesApp()
    quotes_app.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QSpinBox, QTextEdit
from PyQt5.QtGui import QIcon, QIntValidator
from PyQt5.QtCore import pyqtSlot
from gazerbot.cli import run

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Lyric Generator'
        self.left = 200
        self.top = 50
        self.width = 1000
        self.height = 800
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
    
        # Create textbox
        self.username = QLineEdit(self)
        self.username.setText("ZoiAran")
        self.username.move(40, 40)
        self.username.resize(280,40)
        
        self.playlist = QLineEdit(self)
        self.playlist.setText("October 2022")
        self.playlist.move(40, 100)
        self.playlist.resize(280,40)

        self.num_songs = QSpinBox(self)
        self.num_songs.setValue(5)
        self.num_songs.move(40, 160)
        self.num_songs.resize(280,40)

        self.output_file = QLineEdit(self)
        self.output_file.setText("gui.txt")
        self.output_file.move(40, 220)
        self.output_file.resize(280,40)

        self.button = QPushButton('Submit', self)
        self.button.move(40, 280)
        self.button.clicked.connect(self.on_click)



        self.save_button = QPushButton('Save to File', self)
        self.save_button.move(200, 280)
        self.save_button.clicked.connect(self.on_click_save)

        # ave words per song
        # average lines per song
        # full text
        # output goes here
        self.output = QTextEdit(self)
        self.output.setFontPointSize(16)
        self.output.move(360, 10)
        self.output.resize(600, 780)
        self.output.setReadOnly(True)


        self.show()
    
    @pyqtSlot()
    def on_click(self):
        output = run(self.username.text(), self.playlist.text(), self.num_songs.value())
        output_text = "\n_______________________________\n".join([song.title + "\n" + song.lyrics for song in output["songs"]])
        self.output.setPlainText(output_text)
        QMessageBox.question(self, "output", "Success!", QMessageBox.Ok, QMessageBox.Ok)

    @pyqtSlot()
    def on_click_save(self):
        QMessageBox.question(self, "Saved", f"Saved to {self.output_file.text()}", QMessageBox.Ok, QMessageBox.Ok)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

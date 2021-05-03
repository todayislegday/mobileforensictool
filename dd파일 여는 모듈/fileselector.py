import sys
from PyQt5.QtCore import QCoreApplication, QEvent
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QFileDialog, QLabel
 
class QtGUI(QWidget):
 
	def file_select(self): #파일 선택
		FileOpen = QFileDialog.getOpenFileName(self, 'Open file', './')
		self.label1.setText(FileOpen[0])
		global filepath
		filepath = FileOpen[0]
		
	def closeEvent(self, QcloseEvent): # 닫기
		QcloseEvent.accept()

	def ok(self): #
		# 여기에 파일의 경로를 보내 분석할 모듈에 연동!
		print("filepath : %s" %filepath)

	def __init__(self):
		super().__init__()

		self.setWindowTitle("Timmy Room") # 타이틀 바
		self.resize(600, 50) # 창 사이즈
		#그리드 생성
		self.Lgrid = QGridLayout()
		self.setLayout(self.Lgrid)
		#버튼 생성
		self.label1 = QLabel('분석할 모바일의 .dd 파일을 선택해 주세요')
		selectbtn = QPushButton('Select File')
		okbtn = QPushButton('OK')
		closebtn = QPushButton('Cancel')
		#버튼 위치
		self.Lgrid.addWidget(self.label1,0, 0, 1, 5)
		self.Lgrid.addWidget(selectbtn,0, 5)
		self.Lgrid.addWidget(okbtn,1, 0, 1, 3)
		self.Lgrid.addWidget(closebtn,1, 3, 1, 3)
		#버튼 이벤트 처리
		selectbtn.clicked.connect(self.file_select) # 파일 선택
		okbtn.clicked.connect(self.ok) # ok 버튼 클릭 시
		closebtn.clicked.connect(QCoreApplication.instance().quit) # Cancel 버튼 클릭 시

		self.show()

if __name__ == '__main__':
 
	app = QApplication(sys.argv)
	ex = QtGUI()
	app.exec_()

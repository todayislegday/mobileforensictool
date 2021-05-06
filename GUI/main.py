import sys,os
import subprocess #서브 프로세스
import webbrowser #웹브라우저
import asyncio #비동기
import requests #웹 서버에 요청 하는 모듈 
from multiprocessing import Process#멀티 프로세싱
from PyQt5.QtCore import QCoreApplication, QEvent
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QFileDialog, QLabel
from PyQt5 import QtCore





def sub():
    subprocess.run('cd ../was/&&python manage.py runserver',shell=True, text=True,timeout=7)


class QtGUI(QWidget):
 	
	filepath=''#인스턴스 변수로 등록하여 상태공유


	def file_select(self): #파일 선택
		FileOpen = QFileDialog.getOpenFileName(self, 'Open file', './',"datafile(*.dd *.tar *.*)")#해당 확장자만 파일만 고를수 있도록
		print(FileOpen)
		if(FileOpen[0]!=''):
			self.label1.setText(FileOpen[0])
			self.filepath=FileOpen[0]
		
	def closeEvent(self,event): # 닫기
		event.accept() #closeEvent.accept()->event.accept() 변경
    
	def ok(self):
		if self.filepath!='':#파일 경로를 지정하였다면 시스템 명령으로 대시보드를 띄운다.
			try:
				self.label1.setText("127.0.0.1:8000 으로 접속중입니다...기달려 주세요")
				self.label1.repaint()  #객체의 label1을 다시 repaint 해준다.
				subprocess.run('cd ../was/&&python manage.py runserver',shell=True, text=True,timeout=0.5)
			except Exception as e:
				webbrowser.open("http://127.0.0.1:8000",1)#해당 url을 새 창으로 연다.
				sys.exit()
			
			

	def my_exception_hook(exctype, value, traceback):#에러처리 못한부분 있으면 프로그램 종료 하지 않고 
		                                             #print 되도록 처리
		print(exctype, value, traceback)
		sys._excepthook(exctype, value, traceback)

	sys._excepthook = sys.excepthook

	sys.excepthook = my_exception_hook
	
	def __init__(self):
		super().__init__()
		self.filepath=''
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


# 분석할 이미징 파일을 선택하는 창

import sys,os
import subprocess #서브 프로세스
import webbrowser #웹브라우저
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))#상위 경로 함수 사용하기 위해서
from function import read_tar
from PyQt5.QtCore import QCoreApplication, QEvent
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QFileDialog, QLabel
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon

class QtGUI(QWidget):
 	
	filepath=''#인스턴스 변수로 등록하여 상태공유
	outputpath=''
	def file_select(self): #파일 선택
		FileOpen = QFileDialog.getOpenFileName(self, 'Open file', './',"datafile(*.dd *.tar )")#해당 확장자만 파일만 고를수 있도록
		if(FileOpen[0]!=''):
			self.label1.setText(f"입력:{FileOpen[0]}")
			self.filepath=FileOpen[0]

	def out_select(self): #출력 경로 선택
		folder = QFileDialog.getExistingDirectory(self,'select Dir')
		if(folder!=''):
			self.label2.setText(f"출력:{folder}")
			self.outputpath=folder

	def closeEvent(self,event): # 닫기
		event.accept() #closeEvent.accept()->event.accept() 변경
    
	def ok(self):
		if self.filepath!='' and self.outputpath!='':#파일 경로를 지정하였다면 시스템 명령으로 대시보드를 띄운다.
			try:
				path=os.path.dirname(__file__)
				f=open(f"{path}/../경로.txt",'w')
				data = f"{self.filepath}\n{self.outputpath}"  #파일 경로를 기록한다. 추후에 was에서 읽음
				f.write(data)
				f.close()
				
				self.label1.setText("127.0.0.1:8000 으로 접속중입니다...기달려 주세요")
				self.label2.clear()
				self.label2.repaint()
				self.label1.repaint()  #객체의 label1을 다시 repaint 해준다.
				
				subprocess.run(f'python {path}/../was/manage.py runserver',shell=True,timeout=2)
			except Exception as e:
				print(e)
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
		self.setWindowIcon(QIcon('icon.png'))
		self.resize(600,50) # 창 사이즈
		#그리드 생성
		self.Lgrid = QGridLayout()
		self.setLayout(self.Lgrid)
		#버튼 생성
		self.label1 = QLabel('분석할 모바일의 .dd 파일을 선택해 주세요')
		self.label2 = QLabel()
		selectbtn = QPushButton('파일 선택')
		outtbtn = QPushButton('해제 경로')
		okbtn = QPushButton('OK')
		closebtn = QPushButton('Cancel')
		#버튼 위치
		self.Lgrid.addWidget(self.label1,0, 0, 1, 5)
		self.Lgrid.addWidget(self.label2,1, 0, 1, 5)
		self.Lgrid.addWidget(selectbtn,0, 5)
		self.Lgrid.addWidget(outtbtn,1, 5)
		self.Lgrid.addWidget(okbtn,2, 0, 1, 3)
		self.Lgrid.addWidget(closebtn,2, 3, 1, 3)
		#버튼 이벤트 처리
		selectbtn.clicked.connect(self.file_select) # 파일 선택
		outtbtn.clicked.connect(self.out_select) #출력 디렉터리 선택
		okbtn.clicked.connect(self.ok) # ok 버튼 클릭 시
		closebtn.clicked.connect(QCoreApplication.instance().quit) # Cancel 버튼 클릭 시

		self.show()

if __name__ == '__main__':
 
	app = QApplication(sys.argv)
	ex = QtGUI()
	app.exec_()


# 분석할 이미징 파일을 선택하는 창

import sys,os,shutil
import subprocess #서브 프로세스
import webbrowser #웹브라우저
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))#상위 경로 함수 사용하기 위해서
from function import read_tar
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QFileDialog, QLabel, QProgressBar
from PyQt5.QtGui import QIcon

class QtGUI(QWidget):
 	
	tarfilepath=''#인스턴스 변수로 등록하여 상태공유
	buildfilepath=''
	outputpath=''

	def file_select1(self): #파일 선택
		FileOpen = QFileDialog.getOpenFileName(self, 'Open file', './',"datafile(*.dd *.tar )")#해당 확장자만 파일만 고를수 있도록
		if(FileOpen[0]!=''):
			self.label1.setText(f"tar 경로:{FileOpen[0]}")
			self.tarfilepath=FileOpen[0]

	def file_select2(self): #파일 선택
		FileOpen = QFileDialog.getOpenFileName(self, 'Open file', './',"datafile(*.prop)")#해당 확장자만 파일만 고를수 있도록
		if(FileOpen[0]!=''):
			self.label2.setText(f"build.prop 경로:{FileOpen[0]}")
			self.buildfilepath=FileOpen[0]

	def out_select(self): #출력 경로 선택
		folder = QFileDialog.getExistingDirectory(self,'select Dir')
		if(folder!=''):
			self.label3.setText(f"해제 경로:{folder}")
			self.outputpath=folder

	def closeEvent(self,event): # 닫기
		event.accept() #closeEvent.accept()->event.accept() 변경
    
	def ok(self):
		if self.tarfilepath!='' and self.buildfilepath!=''and self.outputpath!='':#파일 경로를 지정하였다면 시스템 명령으로 대시보드를 띄운다.
			try:
				path=os.path.dirname(os.path.abspath(__file__))
				self.progress(self)
				f=open(f"{path}/../경로.txt",'w')
				self.progress(self)
				data = f"{self.tarfilepath}\n{self.outputpath}"  #파일 경로를 기록한다. 추후에 was에서 읽음
				f.write(data)
				f.close()
				self.progress(self)
				shutil.copy(f"{self.buildfilepath}", f"{path}/../was/app/")#build.prop 파일 복사
				self.progress(self)
				self.label1.setText("127.0.0.1:8000 으로 접속중입니다...기다려 주세요")
				self.label2.clear()
				self.label3.clear()
				
				self.label1.repaint()  #객체의 label1을 다시 repaint 해준다.
				self.label2.repaint()
				self.label3.repaint()

				read_tar.decompression(self.tarfilepath,self.outputpath)
				self.progress(self)
				subprocess.run(f'python {path}/../was/manage.py runserver',shell=True,timeout=0.5)
			except Exception as e:
				print(e)
				webbrowser.open("http://127.0.0.1:8000",1)#해당 url을 새 창으로 연다.
				sys.exit()
			
	def progress(self, e):
		self.step = self.step + 20
		self.pbar.setValue(self.step)
		if self.step >= 100:
			self.label4.setText("완료")
			return
		else:
			self.label4.setText("진행중")

	def my_exception_hook(exctype, value, traceback):#에러처리 못한부분 있으면 프로그램 종료 하지 않고 
		                                             #print 되도록 처리
		print(exctype, value, traceback)
		sys._excepthook(exctype, value, traceback)

	sys._excepthook = sys.excepthook

	sys.excepthook = my_exception_hook
	
	def __init__(self):
		super().__init__()
		
		self.setWindowTitle("Timmy Room") # 타이틀 바
		self.setWindowIcon(QIcon(f'{os.path.dirname(os.path.abspath(__file__))}/icon.png'))
		self.resize(600,50) # 창 사이즈
		#그리드 생성
		self.Lgrid = QGridLayout()
		self.setLayout(self.Lgrid)
		#버튼 생성
		self.label1 = QLabel('분석할 모바일의 tar,build.prop 파일을 넣어주세요')
		self.label2 = QLabel()
		self.label3 = QLabel()
		self.label4 = QLabel()
		self.label4.setAlignment(Qt.AlignCenter)
		selectbtn1 = QPushButton('tar 파일선택')
		selectbtn2 = QPushButton('build 파일선택')
		outtbtn = QPushButton('해제 경로')
		okbtn = QPushButton('OK')
		closebtn = QPushButton('Cancel')
		self.pbar = QProgressBar(self)
		self.step = 0
		#버튼 위치
		self.Lgrid.addWidget(self.label1,0, 0, 1, 5)
		self.Lgrid.addWidget(self.label2,1, 0, 1, 5)
		self.Lgrid.addWidget(self.label3,2, 0, 1, 5)
		self.Lgrid.addWidget(self.label4,3, 5, 1, 1)
		self.Lgrid.addWidget(selectbtn1,0, 5)
		self.Lgrid.addWidget(selectbtn2,1, 5)
		self.Lgrid.addWidget(outtbtn,2, 5)
		self.Lgrid.addWidget(self.pbar, 3, 0, 1, 5)
		self.Lgrid.addWidget(okbtn,4, 0, 1, 3)
		self.Lgrid.addWidget(closebtn,4, 3, 1, 3)

		#버튼 이벤트 처리
		selectbtn1.clicked.connect(self.file_select1) # 파일 선택
		selectbtn2.clicked.connect(self.file_select2) # 파일 선택
		outtbtn.clicked.connect(self.out_select) #출력 디렉터리 선택
		okbtn.clicked.connect(self.ok) # ok 버튼 클릭 시
		closebtn.clicked.connect(QCoreApplication.instance().quit) # Cancel 버튼 클릭 시

		self.show()

if __name__ == '__main__':
 
	app = QApplication(sys.argv)
	ex = QtGUI()
	app.exec_()

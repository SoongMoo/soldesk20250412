PI = 3.141592 #상수
i = 10 # 변수
def f(x): # 함수
	return 3*x + 3

class Calculator: # class
	def __init__(self, first, second):  
		self.first = first 
		self.second = second
	def add(self):
		self.result = self.first + self.second
	def div(self):
		self.result = self.first / self.second       
a = Calculator(10, 20) #객체
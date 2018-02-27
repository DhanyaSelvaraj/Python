>>> class sample:
	def method1(self):
		print("Hello")

	def display(self,a,b):
		self.a=a
		self.b=b
		tot=a+b
		print("Sum of two values = %s" % tot)

		
>>> class sample1(sample):
	def method2(self):
		print("Hi")

		
>>> s=sample1()
>>> s.method1()
Hello
>>> s.method2()
Hi
>>> s.display(3,7)
Sum of two values = 10

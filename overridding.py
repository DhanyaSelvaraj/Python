class student:
	def display(self,x):
		self.x=x
		print(self.x)

		
>>> class base(student):
	def display(self,x):
		self.x=x
		print(self.x)

		
>>> s=student()
>>> s.display(1)
1
>>> b=base()
>>> b.display(1)
1
>>> id(1)
1925928688
>>> id(s)
102785008
>>> id(b)
102784304
>>> s.__dict__
{'x': 1}
>>> b.__dict__
{'x': 1}
>>> student.__dict__
mappingproxy({'__module__': '__main__', 'display': <function student.display at 0x06211DB0>, '__dict__': <attribute '__dict__' of 'student' objects>, '__weakref__': <attribute '__weakref__' of 'student' objects>, '__doc__': None})
>>> base.__dict__
mappingproxy({'__module__': '__main__', 'display': <function base.display at 0x06211DF8>, '__doc__': None})
>>> 

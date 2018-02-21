class student:
	def __init__(self,x,y):
		self.x=x
		self.y=y
		tot=self.x+self.y
		print(tot)
	def __del__(self):
		class__name__=self.__class__.__name__
		print(class__name__,"destroyed")

		
>>> s=student(2,4)
6
>>> a1=s
>>> b1=s
>>> print(id(s),id(a1),id(b1))
84089840 84089840 84089840
>>> del(s)
>>> del(a1)
>>> del(b1)
student destroyed
>>>



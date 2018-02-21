class sample:
	def __init__(self,x,y):
		self.x=x
		self.y=y
	def __del__(self):
		class__name__=self.__class__.__name__
		print(class__name__,"destroyed")

		
>>> s=sample(1,3)
>>> s1=s
>>> s2=s
>>> print(id(s),id(s1),id(s2))
102784592 102784592 102784592
>>> del(s)
>>> del(s1)
>>> del(s2)
sample destroyed
>>> 

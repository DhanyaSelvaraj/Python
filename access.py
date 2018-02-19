Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class employee:

	inr=1.3
	def __init__(self,name,salary,place):
		self.name=name
		self.salary=salary
		self.place=place
	def
	
SyntaxError: invalid syntax
>>> class employee:

	inr=1.3

	def __init__(self,name,salary,place):
		self.name=name
		self.salary=salary
		self.place=place

	def increament(self):
		self.salary=int(self.salary*self.inr)

		
>>> emp=employee("migen",300000,"sankari")
>>> emp.name
'migen'
>>> emp.place
'sankari'
>>> emp.salary
300000
>>> emp.increament()
>>> emp.salary
390000
>>> class base:
	
	def method1(self):
		print("hii")
		
	def method2(self,x,y):
		self.x=x
		self.y=y
		print("hello")

		
>>> class derived(base):
	def method3(self):
		print("hiii")

		
>>> obj=derived()
>>> obj.method2(1,3)
hello
>>> obj.method1()
hii
>>> obj.method3()
hiii
>>> obj.x
1
>>> obj.y
3
>>> getattr(obj,x)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    getattr(obj,x)
NameError: name 'x' is not defined
>>> getattr(obj,"x")
1
>>> getattr(obj,"y")
3
>>> hasattr(obj,"z")
False
>>> hasattr(obj,"x")
True
>>> setattr(obj,"x",10)
>>> getattr(obj,"x")
10
>>> obj.x=12
>>> getattr(obj,"x")
12
>>> delattr(obj,"y")
>>> hasattr(obj,"y")
False
>>> obj.y=5
>>> getattr(obj,"y")
5
>>> class base:

	def method1(self):
		print("hii")

	def method2(self,x,y):
		self.x=x
		self.y=y
		print("hello")

		
>>> b=base()
>>> print(b.__name__)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    print(b.__name__)
AttributeError: 'base' object has no attribute '__name__'
>>> print(base.__name__)
base
>>> print(base.__module__)
__main__
>>> print(base.__doc__)
None
>>> class base:
	'hi this sample class is test attributes of class'

	def method1(self):
		print("hii")

	def method2(self,x,y):
		self.x=x
		self.y=y
		print("hello")

		
>>> print(base.__doc__)
hi this sample class is test attributes of class
>>> print(base.__dict__)
{'__module__': '__main__', '__doc__': 'hi this sample class is test attributes of class', 'method1': <function base.method1 at 0x05616D68>, 'method2': <function base.method2 at 0x05616DB0>, '__dict__': <attribute '__dict__' of 'base' objects>, '__weakref__': <attribute '__weakref__' of 'base' objects>}
>>> a=b
>>> a.method1()
hii
>>> type(a)
<class '__main__.base'>
>>> a.method2(10,10)
hello
>>> a.x
10
>>> b.x
10
>>> type(a)
<class '__main__.base'>
>>> type(x)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    type(x)
NameError: name 'x' is not defined
>>> type(a.x)
<class 'int'>
>>> id(a.x)
1923504000
>>> id(b.x)
1923504000
>>> 

class student:

	def __init__(self,name,age,rollno):
		self.name=name
		self.age=age
		self.rollno=rollno
	def displaystu(self):
		print("{} {} {}".format(self.name,self.age,self.rollno))

		
>>> class employee(student):

	def __init__(self,name,age,rollno,salary,desig):
		student.__init__(self,name,age,rollno)
		self.salary=salary
		self.desig=desig
	def displayemp(self):
		print("{} {}".format(self.salary,self.desig))

		
>>> class manager(employee):

	def __init__(self,name,age,rollno,salary,desig,admin):
		employee.__init__(self,name,age,rollno,salary,desig)
		self.admin=admin
	def displaymanage(self):
		print("{}".format(self.admin))

		
>>> obj=manager("migen",2,6,500000,"engineer","yes")
>>> obj.displaystu()
migen 2 6
>>> obj.displayemp()
500000 engineer
>>> obj.displaymanage()
yes
>>> 

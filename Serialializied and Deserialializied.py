import pickle

class student:
    def __init__(self,name,age,roll):
        self.name=name
        self.age=age
        self.roll=roll
    def display(self):
        print(self.name,self.age,self.roll)

s=student("Dhanya",21,8)

data=open("d:\greenjava\Python\myfirst.pkl","wb")
pickle.dump(s,data)

data=open("d:\greenjava\Python\myfirst.pkl","rb")
pickle.load(data)
print(s.display())
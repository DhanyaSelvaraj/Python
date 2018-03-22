from csv import DictReader
import pickle

data=list(DictReader(open("d:\greenjava\Python\whildlife.csv","rt")))


data1=open("d:\greenjava\Python\whildlife.pkl","wb")
pickle.dump(data,data1)

data1.close()

data1=open("d:\greenjava\Python\whildlife.pkl","rb")
pickle.load(data1)


for i in data:
    print(i)
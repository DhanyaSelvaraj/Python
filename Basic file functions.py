Basics file methods:

>>> f=open("sample.txt",'w')
>>> f.write("Java and Python are programing language")
39
>>> f=open("sample.txt","r")
>>> f.readline()
'Java and Python are programing language'
>>> f=open("sample.txt","a")
>>> f.write(" Both are very simple")
21
>>> f=open("sample.txt","r")
>>> f.readline()
'Java and Python are programing language Both are very simple'
>>> f.close()
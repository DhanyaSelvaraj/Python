Regular Expression(search):

Program-1:
    
import re
if(re.search("happy","I am very happy today")):
    print("There is happy")

#Output:
    There is happy
    
Pogram-2:
    
import re
myno="91-987-654-3210"
if re.search(r"\w{2}-\w{3}-\w{3}-\w{4}",myno):
    print("Valid number")
else:
    print("Notvalid number")

#Output:
    Valid number


Regular Expression(findall):

Program 1:

import re
obj=re.findall("happy","I am very happy today  because of my frnds. Its very happy to be with my frnds")
for i in obj:
    print(i)

#output:
    happy
    happy


Program 2:
import re
s1="sday,mday,tday,wday,tday,fday,sday"
a=re.findall("[a-n]day",s1)

for i in a:
    print(i)
    

#Output:
    mday
    fday

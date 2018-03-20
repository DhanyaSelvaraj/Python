Regular Expression(finditer):

import re
str="there is a string class which is used to perform the string operations in java"

for i in re.finditer("string",str):
    ctup=i.span()
    print(ctup)
    

#Output:
    (11,17)
    (53,59)

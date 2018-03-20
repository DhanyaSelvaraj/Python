Regular Expression(sub):

import re
s1="hai everyone! how are u all"
a=re.compile("hai")
s1=a.sub("hi",s1)
print(s1)

#Output:
  hi everyone! how are u all

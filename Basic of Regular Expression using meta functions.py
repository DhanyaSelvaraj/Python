Basic of Regular Expression using meta functions:

>>> import re
>>> result=re.findall(r"","Java and Python are programming language which is very simple to use")
>>> print(result)
['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
>>> result=re.findall(r"Java","Java and Python are programming language which is very simple to use")
>>> print(result)
['Java']
>>> result=re.findall(r".","Java and Python are programming language which is very simple to use")
>>> print(result)
['J', 'a', 'v', 'a', ' ', 'a', 'n', 'd', ' ', 'P', 'y', 't', 'h', 'o', 'n', ' ', 'a', 'r', 'e', ' ', 'p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g', ' ', 'l', 'a', 'n', 'g', 'u', 'a', 'g', 'e', ' ', 'w', 'h', 'i', 'c', 'h', ' ', 'i', 's', ' ', 'v', 'e', 'r', 'y', ' ', 's', 'i', 'm', 'p', 'l', 'e', ' ', 't', 'o', ' ', 'u', 's', 'e']
>>> result=re.findall(r"\w","Java and Python are programming language which are very simple to use")
>>> 
>>> print(result)
['J', 'a', 'v', 'a', 'a', 'n', 'd', 'P', 'y', 't', 'h', 'o', 'n', 'a', 'r', 'e', 'p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g', 'l', 'a', 'n', 'g', 'u', 'a', 'g', 'e', 'w', 'h', 'i', 'c', 'h', 'a', 'r', 'e', 'v', 'e', 'r', 'y', 's', 'i', 'm', 'p', 'l', 'e', 't', 'o', 'u', 's', 'e']
>>> result=re.findall(r"\w{2}","Java and Python are programming language which are very simple to use")
>>> print(result)
['Ja', 'va', 'an', 'Py', 'th', 'on', 'ar', 'pr', 'og', 'ra', 'mm', 'in', 'la', 'ng', 'ua', 'ge', 'wh', 'ic', 'ar', 've', 'ry', 'si', 'mp', 'le', 'to', 'us']
>>> result=re.findall(r"\w{1,3}","Java and Python are programming language which are very simple to use")
>>> print(result)
['Jav', 'a', 'and', 'Pyt', 'hon', 'are', 'pro', 'gra', 'mmi', 'ng', 'lan', 'gua', 'ge', 'whi', 'ch', 'are', 'ver', 'y', 'sim', 'ple', 'to', 'use']
>>> result=re.findall(r"\d","Java and Python are programming language which are very simple to use")
>>> print(result)
[]
>>> result=re.findall(r"\d","1.Java and 2.Python are programming language which are very simple to use")
>>> print(result)
['1', '2']
>>> result=re.findall(r"\D","1.Java and 2.Python are programming language which are very simple to use")
>>> print(result)
['.', 'J', 'a', 'v', 'a', ' ', 'a', 'n', 'd', ' ', '.', 'P', 'y', 't', 'h', 'o', 'n', ' ', 'a', 'r', 'e', ' ', 'p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g', ' ', 'l', 'a', 'n', 'g', 'u', 'a', 'g', 'e', ' ', 'w', 'h', 'i', 'c', 'h', ' ', 'a', 'r', 'e', ' ', 'v', 'e', 'r', 'y', ' ', 's', 'i', 'm', 'p', 'l', 'e', ' ', 't', 'o', ' ', 'u', 's', 'e']
>>> result=re.findall(r"^\d","1.Java and 2.Python are programming language which are very simple to use")
>>> print(result)
['1']
>>> result=re.findall(r"\W","1.Java and 2.Python are programming language which are very simple to use")
>>> print(result)
['.', ' ', ' ', '.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
>>> result=re.findall(r"\w*","1.Java and 2.Python are programming language which are very simple to use")
>>> print(result)
['1', '', 'Java', '', 'and', '', '2', '', 'Python', '', 'are', '', 'programming', '', 'language', '', 'which', '', 'are', '', 'very', '', 'simple', '', 'to', '', 'use', '']
>>> result=re.findall(r"\w+","1.Java and 2.Python are programming language which are very simple to use")
>>> print(result)
['1', 'Java', 'and', '2', 'Python', 'are', 'programming', 'language', 'which', 'are', 'very', 'simple', 'to', 'use']
>>> result=re.findall(r"^\w","1.Java and 2.Python are programming language which are very simple to use")
>>> print(result)
['1']
>>> result=re.findall(r"^\w*","1.Java and 2.Python are programming language which are very simple to use")
>>> print(result)
['1']
>>> result=re.findall(r"\w$","1.Java and 2.Python are programming language which are very simple to use")
>>> print(result)
['e']
>>> result=re.findall(r"\w*$","Java and Python are programming language which are very simple to use")
>>> print(result)
['use', '']
>>> result=re.findall(r"\w+$","Java and Python are programming language which are very simple to use")
>>> print(result)
['use']
>>> result=re.findall(r"\b\w","Java and Python are programming language which are very simple to use")
>>> print(result)
['J', 'a', 'P', 'a', 'p', 'l', 'w', 'a', 'v', 's', 't', 'u']
>>> result=re.findall(r"\b\w$","Java and Python are programming language which are very simple to use")
>>> print(result)
[]
>>> result=re.findall(r"\w\b","Java and Python are programming language which are very simple to use")
>>> print(result)
['a', 'd', 'n', 'e', 'g', 'e', 'h', 'e', 'y', 'e', 'o', 'e']
>>> result=re.findall(r"\B\w","Java and Python are programming language which are very simple to use")
>>> print(result)
['a', 'v', 'a', 'n', 'd', 'y', 't', 'h', 'o', 'n', 'r', 'e', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g', 'a', 'n', 'g', 'u', 'a', 'g', 'e', 'h', 'i', 'c', 'h', 'r', 'e', 'e', 'r', 'y', 'i', 'm', 'p', 'l', 'e', 'o', 's', 'e']
>>> result=re.findall(r"\w\B","Java and Python are programming language which are very simple to use")
>>> print(result)
['J', 'a', 'v', 'a', 'n', 'P', 'y', 't', 'h', 'o', 'a', 'r', 'p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'l', 'a', 'n', 'g', 'u', 'a', 'g', 'w', 'h', 'i', 'c', 'a', 'r', 'v', 'e', 'r', 's', 'i', 'm', 'p', 'l', 't', 'u', 's']


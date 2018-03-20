Regular Expression with Backslash:

import re
str="dhanya\\salem"
print(re.search(r"\\salem",str))

#Output:
 <_sre.SRE_Match object; span=(6, 12), match='\\salem'>

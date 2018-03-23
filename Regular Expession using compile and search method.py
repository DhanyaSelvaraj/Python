import re
def display(string):
    a=re.compile(r"[^a-zA-Z0-9]")
    string=a.search(string)
    return not bool(string)

print(display("abcdABCD1234"))
print(display("@!#$%&*"))


#Output:
   True
   False
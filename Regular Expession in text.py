import re
def display(text):
    patterns="ab*?"
    if re.search(patterns,text):
        return "Found a match!"
    else:
        return "Not matched!"

print(display("ac"))
print(display("abc"))
print(display("ebf"))


#Output:
  Found a match!
  Found a match!
  Not matched!
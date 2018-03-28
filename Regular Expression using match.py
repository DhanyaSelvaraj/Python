import re
pattern = 'dog'
text = 'The quick brown fox jumps over the lazy dog.'
match = re.search(pattern, text)
x = match.start()
y = match.end()
print('Found "%s" in "%s" from %d to %d ' % match.re.pattern, match.string, x, y))


#Output:
    Found "dog" in "The quick brown fox jumps over the lazy dog." from 40 to 43 
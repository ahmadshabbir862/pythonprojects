import random
line = random.choice(keywords)
print('Keyword:')
print (line)

line = random.choice(definitions)
print ('A:')
print (line)

line = random.choice(definitions)
print ('B:')
print(line)

line = random.choice(definitions)
print ('C:')
print(line)

#randomly selects a keyword and definition from the file

A = []
ans = input('Is it A, B or C?')
print()

if ans == 'A' :
    print ('Correct')
else:
    print ('Incorrect')
    
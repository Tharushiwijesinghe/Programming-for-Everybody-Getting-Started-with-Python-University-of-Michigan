astr = 'Hello bob'
try:
    istr = int(astr)
except:
    istr = -1
print('First',istr)

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
print('second',istr)

#...
astr = 'bob'
try:
    print('Hello')
    istr = int(astr)
    print('There')
except:
    istr = -1
print('All Done',istr)

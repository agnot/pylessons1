def commaCode(theList):
    if len(theList) == 0:
        return ''
    
    resultString = theList[0]
    if len(theList) == 1:
        return resultString
    
    for i in range(1, len(theList)-1):
        resultString +=  ', ' + theList[i]
    resultString += ' and ' + theList[-1]
    return resultString

spam = []
print('Please enter some strings:')

while True:
    inValue = input()
    if inValue == '':
        break;
    spam += [inValue]

#spam = ['apples', 'bananas', 'tofu', 'cats']
#spam = ['apples', 'bananas', 'tofu']
#spam = ['apples', 'bananas']
#spam = ['apples']
    
if len(spam) != 0:
    print ('Result is: ' + commaCode(spam))
else:
    print('You have to input some strings!')

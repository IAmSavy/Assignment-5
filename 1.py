String = input('Enter a string: ')
NewString = ''

for x in range(len(String)):
    NewString += String[len(String) - 1 - x]
print('The reversed string is ', NewString)
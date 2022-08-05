import os

dir = input('What directory would you like to save your file into: ')
filename = input('What do you want the name of the file to be: ')
name = input('Please enter your name: ')
address = input('Please enter your address: ')
phone = input('Please enter your phone number: ')

try:
    os.mkdir(dir)
except FileExistsError:
    pass

savefile = open(dir + '\\' + filename, 'w')
savefile.write(f'{name},{address},{phone}')
savefile.close()
savefile = open(dir + '\\' + filename, 'r')
content = savefile.read().split(',')
savefile.close()
print('Name: ' + content[0])
print('Address: ' + content[1])
print('Phone: ' + content[2])

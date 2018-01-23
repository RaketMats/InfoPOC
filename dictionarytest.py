dict = {'Name': 'Zara', 'Age': '7', 'Class': 'First'}
print "dict['Name']: ", dict['Name']

print 'Length: ', len(dict)

for i in dict:
    print i

for i in dict.items():
    print i[1]

dict['Name'] = 'Abc'
print "dict['Name']: ", dict['Name']

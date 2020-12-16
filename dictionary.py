#!/usr/bin/python

my_dict = {'aaa': 7, 'bbb': 8}
print my_dict
testcase = 'ccc'
interval = 13
my_dict.update({testcase: interval})
print my_dict


print my_dict.keys()
for item in my_dict.keys():
        print "key:", item
        print "value:", my_dict.get(item)

# clear dictionary
my_dict.clear()
print my_dict

# put list in dictionary
mylist = list()
for i in range(1, 10):
        mylist.append(i)
print mylist
my_dict.update({'aaa': mylist})

mylist = list()
for i in range(20, 30):
        mylist.append(i)
my_dict.update({'bbb': mylist})
print my_dict

item='bbb'
value_list = my_dict.get(item)
print value_list

for item in value_list:
        print item

### practice of not find map in dictionary
my_dict.clear()
my_dict.update({'aaa': 111})
my_dict.update({'bbb': 222})
print "my_dict.get('aaa')=", my_dict.get('aaa')
print "my_dict.get('aaa')=", my_dict.get('ccc')
value = my_dict.get('ccc')
if value is None:
        print value
else:
        print "other value"

my_dict.update({'ccc': mylist})
print my_dict.get('ccc')

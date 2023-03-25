import datetime

my_list = []


my_list.append(10)
my_list.append(20)
my_list.append(3)
my_list.append(4)

print(sum(my_list))

my_list.sort(reverse=True)

for my_item in my_list:
    print(my_item)

my_dict = {}
my_dict["first"] = 1
my_dict["second"] = 3
my_dict["last"] = 10
my_dict["date"] = datetime.datetime.today()

#print(my_dict)

my_list.append(my_dict)
#print(my_list)

for key in my_dict.keys():
    print(key)

for val in my_dict.values():
    print(val)

for key, val in my_dict.items():
    print(key + str(val))
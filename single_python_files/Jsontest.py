import json
with  open("data//example.json") as jsonfile:
    data = json.load(jsonfile)
    

print (data)
for i in data['widget']:
    print (i)

json.dump(data, open("single_python_files//data//JsonDump.json", "w"))



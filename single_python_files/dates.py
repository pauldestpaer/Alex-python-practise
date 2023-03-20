import datetime

mydate = datetime.datetime.today()
print(mydate)


class myClass:
    _age = 19
    # Static function
    def Name():
        return "Alex"

    def Time():
        return datetime.datetime.today()

    # Non static functions
    def Age(self):
        return self._age

    def Birthday(self):
        self._age = self._age+1
        print("I worked")


print (myClass.Name())

Alex = "Alex"
Alex = 10

Alex = myClass()
Paul = myClass()

Alex.Birthday()
print(Alex.Birthday())
print(Paul.Age())

print(Alex.Age())


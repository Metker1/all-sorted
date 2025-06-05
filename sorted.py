file = ['name','age','hobby','lolo']

class Person:
    lolo = "films"

for i in file:
    if getattr(Person,i,False):
        print(i)
#1

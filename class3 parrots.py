class parrot:
    speices="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
appolo=parrot("appolo",10)
kiwi=parrot("kiwi",3)
print("apolo is a {}".format(appolo.speices))
print("kiwi is also a {}".format(kiwi.speices))

print("{} is {}".format(appolo.name,appolo.age))
print("{} is {}".format(kiwi.name,kiwi.age))
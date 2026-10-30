class myclass:

    __privateVar = 27;
    def __privMeth(self):
        print('i am inside class myClass')
    def hello(self):
        print("private variable value",myclass.__privateVar)


foo = myclass()
foo.hello()
foo._myclass__privMeth()

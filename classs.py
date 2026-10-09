class IOSstring():
    def __init__(self):
        self.str1= " "
    def enter_string(self):
        self.str1=input("enter string :")
    def get_string(self):
        print("the result is:", self.str1.upper())
str1=IOSstring()

str1.enter_string()
str1.get_string()
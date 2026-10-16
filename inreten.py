class FamilyMember:
    def __init__(self,eye_color, height_cm ):
        self.eye_color=eye_color 
        self.height_cm=height_cm
    def show_traits(self):
        print ("eye_color",self.eye_color )
        print ("height_cm",self.height_cm )
    


class kid(FamilyMember):
    def  __init__(self, name,age,eye_color, height_cm ):
        self.name = name
        self.age = age 
        super().__init__(eye_color, height_cm)
    def show_traits(self):
        print ("name",self.name)
        print ("age",self.age )
        super().show_traits()
    def fav_hobby(self,hobby):
        print(self.name,"loves",hobby)
child=kid("vehan",10,"brown",150)
child.show_traits()
child.fav_hobby("swiming")
print("is kid subclass of family member ?", issubclass(kid,FamilyMember))


    
        


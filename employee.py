class employee:
    def __init__(self):
        print("employee created")
    def __del__(self):
            print("distructer called")
def Create_obj():
    print("making obj")
    obj=employee()
    print("function end")
    return obj 
print("calling create_obj() function...")
obj= Create_obj()
print("program end ")

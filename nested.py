medical_cause=input("did you have an medical cause? (Y/N)").strip().upper()
if medical_cause == 'Y':
    print("you are are allowed")
else:
    atten=int(input("Enter the attendance of the student:"))
    if atten >=75:
        print("allowed")
    else:
        print("NOT ALLOWED")
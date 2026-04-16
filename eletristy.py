units=int(input("please enter number of units you consumed :"))
if(units<50):
    amount=units*2.60
    surcharge=35
elif(units<=100):
    amount= + 130 * ((units-50)*3.25)
    surcharge=35
elif(units<=200):
    amount= + 130 + 162.50 ((units-100)*5.26)
    surcharge=35
else:
    amount=130+162.50+526 ((units-200 )*8.45)
    surcharge=41
total=surcharge+amount
print("\n Electricity bill = %.2f" %total)
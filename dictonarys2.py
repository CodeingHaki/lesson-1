test_dict={"codingal" : 2, "is":2,"best":2,"for":2,
"conding":1 }

print("The orignal dictionary:"+ str(test_dict))
K=2
res=0
for key in test_dict:
    if test_dict[key]==K:
        res = res+1
print("the Frequncy of K is :"+str(res))
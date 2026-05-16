import time
import numpy as np
start=time.time()
np.random.seed(1)
Allnumbers="0123456789"
Capital="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Small="abcdefghijklmnopqrstuvwxyz"
Characters="!@#$^&*()_+-=[]{}|;:',.<>?/`~"
space=" "
Allcombine=Allnumbers+Small+Capital+Characters+space
# password=np.random.choice(list(Allcombine), size=364)
password=input("Entre your password-->>")
correct=list()
length=0
for i in range(len(password)):
    for j in range(len(Allcombine)):
        if(password[i]==Allcombine[j]):
            length=length+1
            correct.append(Allcombine[j])
            continue

    if(length==len(password)):
        Final="".join(correct)
        print(f"The password is {Final} ")
        end=time.time()
        print(f"The Total time is {end-start}")
        quit()
print("Your Password is very Strong")

        

        

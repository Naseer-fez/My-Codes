import numpy as np 
import pyperclip 

class Paswords:
    Allnumbers="0123456789"
    Capital="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Small="abcdefghijklmnopqrstuvwxyz"
    Characters="!@#$^&*()_+-=[]{}|;:',.<>?/`~"
    Allcombine=Allnumbers+Capital+Small+Characters 
    
    Finalpassword=[]
    def __init__(self):
        self.welcome()
        
    def welcome(self):
        print("WELCOME TO PASSWORD GENERATOR:: \n\n\n")
        
        Numbers=int(input("ENTRE THE NUMBER OF CHARACTER :"))
        
        self.passwordgen(Numbers)
        self.ask()
        print("\n\nTHANK YOU\n")
        
    def passwordgen(self,Numbers):
        self.Numbers=Numbers
        print(f"Generating password of length: {self.Numbers}")
        
        forallchars=self.randomnessofcharacter(Numbers)
        forallindex=self.randomnessofindex(Numbers)
        self.Finalpassword=self.CombinationofRandomess(forallchars,forallindex)
        print(f"\n\n\nGenrataed password is:\n\n{self.Finalpassword}")
            
            
    def randomnessofindex(self,Numbers:int):
        self.Numbers=Numbers
        send=np.random.choice(np.arange(Numbers),size=Numbers,replace=False)
        send_list=send.tolist()
        return send_list
    def ask(self):
        print("\n\nDO YOU WANT TO COPY THIS IN CLIPBOARD??\n")
        asking=input("Y(or)N->")    
        if(asking.upper()=='Y'):
            pyperclip.copy(self.Finalpassword)
            print("Copied Succefully!!")
        elif(asking.upper()=='N'):
            return
        else:
            print("ENTRER A VALID NUMBER ")
            self.ask()        
                
                
    def randomnessofcharacter(self,Numbers:int):
            # len_num=len(Allnumbers)
            # len_allc=len(Capital)
            # len_alls=len(Small)
            # len_allch=len(Characters)
            # len_avaliable=len(Allcombine)
            
            password_char=[]
            counting=0
            while(counting<=Numbers):
                take=np.random.randint(0,4)
                combination=[self.Allnumbers,self.Capital,self.Small,self.Characters][take]
                send=np.random.choice(list(combination))
                counting+=1
                password_char.append(send)
            return password_char
    def CombinationofRandomess(self,forallchars,forallindex):
        Finalpassword=['']*self.Numbers
        for indx,cahr in zip(forallindex,forallchars):
                Finalpassword[indx]=cahr
        return ''.join (Finalpassword)


zz=Paswords()


   
         

import ctypes as C
import os


# clib=C.CDLL(os.path.join(path,'array.dll'))

class Date_Time:
    def __init__(self
                 ):
        self.path=os.getcwd()
        # self.memoryalocating_date(1)
        self.date_arr=None
        

        pass
    def __memoryalocating_date(self,format):
        """This function is used to allocate the space for the array 
        which is used to store the date , the default is one """
        mr=C.CDLL(os.path.join(self.path,'memory_Date.dll'))
        memory=mr.allocatiing_memory_date
        memory.argtypes=[C.c_int]
        memory.restype=C.POINTER(C.c_int)
        format=C.c_int(format)
        return  memory(format) #return the memory address
    """so the format which i have decide is , if it is 1 which is the default iam using the indian time stand
    Day -Month-Year and if it is 2 then the american format , Month-day -year,in future i think i can get the 3rd foramt which is the 
     Year-month -day, depending on the liking  """
    def Date_Checker(self,date:str):
        if not isinstance(date,str):
            raise TypeError("The Format which you have mentioned is not a string and this is not valid,")
        """The Hierachary fill is-->
        First year, Second is month and the last is date, it is always the present year followed by the decade """
        #now lets use the c function
        dllpath=C.CDLL(os.path.join (self.path,"Datecheck.dll"))
        checker=dllpath.Dateforamtchecker
        checker.argtypes=[C.c_char_p,C.c_int]
        checker.restype=C.c_int
        passingdate=date.replace("-", "")
        passingdate=passingdate.encode("UTF-8")
        # valadator=len(passingdate)
        # print(valadator)
        # if(valadator>4):
        #     raise TypeError(f"The year index goes out of bound {valadator}")
        value=checker(passingdate,len(passingdate))
        if (value==0):
            raise TypeError("This is not the valid way the Date Contais a charater ")
        self.date=date
        # print(self.date)
    def Date(self,date:str,format=1):
        if format!=(1 or 0):
            raise TypeError("The format specided is not available")


        self.Date_Checker(date)
        self.date_arr=self.__memoryalocating_date(format)
        dllpath=C.CDLL(os.path.join (self.path,"Date_Filler.dll"))
        date_maker=dllpath.datearrangment
        date_maker.argtypes=[C.c_char_p,C.POINTER(C.c_int)]
        date_maker.restype=C.c_char_p
        date=date.replace("-", "").encode("UTF-8")#this can be optmised cause i call this again in the above line
        validator=date_maker(date,self.date_arr)
        if(validator==b'NO'):
            raise TypeError("Out of range output , please verify the date")
        print(validator.decode()) 
        return self.date_arr
    def Day_of_the_year(self,date_arr,format=1):
        dllpath=C.CDLL(os.path.join(self.path,"Day_of_Year.dll"))
        Day_finder=dllpath.Day_of_the_year
        Day_finder.argtypes=[C.POINTER(C.c_int),C.c_int]
        Day_finder.restype=C.c_char_p
        weekday=Day_finder(date_arr,format).decode("UTF-8")
        if(weekday=="No"):
            raise TypeError("The Requied date which was passed is not a complete date ")
        return weekday



        





        """Untill this part the memory allaoction and date transfer is done , now i need to 
        make or add function this like , subration of the year, days , months ,etc, i have to add another format method aslo """




    

        


if __name__=="__main__":
    z=Date_Time()
    a=z.Date("10-2-2026")
    for i in range(1,4):
        print(a[i])
#    v=z.Day_of_the_year(a)
#    print(v)

from datetime import*

class student:
    def __init__(self,name,add):
        self.Name=name
        self.address=add
    def Assign_Book(self,sid,bid):
        flag = 0
        flag1 = 0
        flag2 = 0
        with open('students.txt','r') as b:
            All_Data=b.readlines() #All_Data is a List
            New_Data=[]
            for data in All_Data:
                #print("checking fine")
                seperated=data.split(',')
                if seperated[0]==sid :
                    flag2=1
                    if seperated[3]!="0" :
                        flag = 1
                        break
        if flag == 1:
            print("You can't Issue The Book First Pay The Fine")
        else:
            #Firstly Book is checked whether Issued or not
            with open('books.txt', 'r') as b:
                All_Data = b.readlines()  # All_Data is a List
                New_Data = []
                for data in All_Data:
                    #print(data)
                    seperated = data.split(',')
                    if seperated[0]==bid and seperated[4].strip().lower()=='issued' :
                        flag1 = 1
                        break
            if flag1 == 1:
                print("This Book is Not Available")
            else:
                # Now mark it issued
                with open('books.txt', 'r') as b:
                    All_Data = b.readlines()  # All_Data is a List
                    New_Data = []
                    for data in All_Data:
                        #print(data)
                        seperated = data.split(',')
                        if seperated[0] == bid :
                            seperated[4] = 'issued\n'
                        tmp=",".join(seperated)
                        New_Data.append(tmp)
                with open('books.txt','w') as b:
                    temp="".join(New_Data)
                    b.writelines(temp)

                with open('students.txt', 'a') as b:
                    dat=input("Enter Date of Issuing(Today's Date in DD-MM-YYYY) :- ")
                    spl=dat.split('-')
                    #print(spl)
                    d=date(int(spl[2]),int(spl[1]),int(spl[0]))
                    #print("date is ",d)
                    #print(type(d))
                    ld=(d+timedelta(days = 15))
                    #print("last date is ", ld)
                    ins=str(d);
                    ins2=str(ld)
                    #print(ins, " ", ins2)
                    b.writelines(f"{sid},{bid},{self.Name},0,1,{ins},{ins2}\n")
                    print("Book Assigned Successfully!!! ")


    def No_of_Book_Issued(self,sid):
        with open('students.txt','r') as b:
            cnt = 0
            All_Data = b.readlines()  # All_Data is a List
            for data in All_Data:
                seperated = data.split(',')
                if seperated[0] == sid :
                    cnt = cnt + int(seperated[4])
        print("No. Of Books Issued Are:- ", cnt)

    def Fine(self,sid):
        with open('students.txt','r') as b:
            cnt = 0
            All_Data = b.readlines()  # All_Data is a List
            for data in All_Data:
                seperated = data.split(',')
                if seperated[0] == sid :
                    cnt = cnt + int(seperated[3])
        print("Total Fine To be Paid Is:- ", cnt)

    def Return_Book(self,sid,bid):
        dat=input("Input Todays Date in DD-MM-YYYY:- ")
        spl = dat.split('-')
        #print(spl)
        d = date(int(spl[2]), int(spl[1]), int(spl[0]))
        d = str(d)
        with open('students.txt', 'r') as b:
            cnt = 0
            All_Data = b.readlines()  # All_Data is a List
            for data in All_Data:
                seperated = data.split(',')
                if seperated[0] == sid and seperated[1] == bid :
                    cnt = seperated[6]
        flag=0;
        #print(cnt,"ld")
        if d > cnt:
            #add fine as returning late
            with open('students.txt', 'r') as b:
                All_Data = b.readlines()  # All_Data is a List
                New_Data = []
                for data in All_Data:
                    seperated = data.split(',')
                    if seperated[0] == sid and seperated[1] == bid :
                        x = int(seperated[3]) + 50  #50 is the fine for late returning of book
                        y = int(seperated[4]) -1
                        seperated[4] = str(y)
                        seperated[3] = str(x)
                        seperated[5] = ""
                        seperated[6] = "\n"
                    tmp = ",".join(seperated)
                    New_Data.append(tmp)
            with open('students.txt', 'w') as b:
                temp = "".join(New_Data)
                b.writelines(temp)
            flag=1
            print("Book Returned and Fine is added due to Late Returning  of the book")

        with open('books.txt', 'r') as b:
            All_Data = b.readlines()  # All_Data is a List
            New_Data = []
            for data in All_Data:
                # print(data)
                seperated = data.split(',')
                if seperated[0] == bid:
                    seperated[4] = 'available\n'
                tmp = ",".join(seperated)
                New_Data.append(tmp)
        with open('books.txt', 'w') as b:
            temp = "".join(New_Data)
            b.writelines(temp)
        if flag==0:
            print("Book Returned Without Fine ")

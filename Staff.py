
class staff:
    def __init__(self, name, add):
        self.Name=name;
        self.address=add;

    def Add_Book(self, id, bname, aname,pdate):
        with open('books.txt','a') as b:
            b.writelines(f"{id},{bname},{aname},{pdate},available\n")
            print("Book Added Successfully!!! ")

    def Delete_Book(self,id):
        with open('books.txt','r') as b:
            All_Data=b.readlines() #All_Data is a List
            New_Data=[]
            for data in All_Data:
                #print(data)
                seperated=data.split(',')
                if(seperated[0]!=id):
                    New_Data.append(data)
        flag=0
        with open('books.txt', 'w') as b:
            temp="".join(New_Data)
            b.writelines(temp)
            flag=1
        if(flag==1):
            print("Inputted Book is Deleted From the Record")







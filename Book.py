
class book:
    def Search_Book(self,id):
        with open('books.txt','r') as b:
            All_Data=b.readlines() #All_Data is a List
            New_Data=[]
            flag=0
            for data in All_Data:
                #print(data)
                seperated=data.split(',')
                if(seperated[0]==id):
                    flag=1
                    break
            return flag

    def Is_Available_Not(self,id):
        with open('books.txt','r') as b:
            All_Data=b.readlines() #All_Data is a List
            New_Data=[]
            flag=0
            for data in All_Data:
                print(data)
                seperated=data.split(',')
                if seperated[0]==id and seperated[4].strip().lower()=='available' :
                    # Strip is used \n is attached in the end
                    flag=1
                    break
            return flag

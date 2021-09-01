from Staff import staff
from Book import book
from Student import student


if __name__ == '__main__':
  file=open('books.txt','a')
  file1 = open('students.txt', 'a')
  try:
    press_key={"1": "Add Books", "2": "Delete Books", "3": "Assign Book", "4": "Check Is This Book Available", "5":"Search Books", "6":"Check No. OF Book Issued","7":"Check Fine","8":"Return Book","q":"Quit"}
    i_key= False
    while not(i_key=="q"):
      print(f"\n----------Welcome To Library Management System---------\n")
      for key,value in press_key.items():
        print("Press", key , "To", value)
      i_key=input("Press Key: ").lower()
      if i_key=="1":
        print("\nCurrent Selection : Add Book\n")
        a = input("Enter Name:- ")
        b = input("Enter address:- ")
        c = input("Enter book ID:- ")
        d = input("Enter Book Title:- ")
        e = input("Enter Author:- ")
        f = input("Enter Publish Date:- ")
        obj = staff(a,b)
        obj.Add_Book(c,d,e,f)
      elif i_key=="2":
        print("\nCurrent Selection : Delete Book\n")
        a = input("Enter Name:- ")
        b = input("Enter address:- ")
        c = input("Enter book ID:- ")
        obj = staff(a, b)
        obj.Delete_Book(c)
      elif i_key=="3":
        print("\nCurrent Selection : Assign Book\n")
        a = input("Enter Name of Student:- ")
        b = input("Enter address:- ")
        c = input("Enter book ID:- ")
        d = input("Enter Student ID:- ")
        obj = student(a,b)
        obj.Assign_Book(d,c);
      elif i_key=="4":
        print("\nCurrent Selection : Is This Book Available\n")
        c = input("Enter book ID:- ")
        obj = book()
        flag = obj.Is_Available_Not(c)
        if flag == 1:
            print("This Book is available To be Issued In Library")
        else:
            print("This Book is Not available To be Issued In Library")
      elif i_key=="5":
        print("\nCurrent Selection : Search Book\n")
        c = input("Enter book ID:- ")
        obj = book()
        flag = obj.Search_Book(c)
        if flag == 1:
            print("This Book is Present In Library")
        else:
            print("This Book is Not Present In Library")
      elif i_key=="6":
        print("\nCurrent Selection : No. Of Book Issued\n")
        d = input("Enter Student ID:- ")
        obj=student("abc","xyz")
        obj.No_of_Book_Issued(d)
      elif i_key=="7":
        print("\nCurrent Selection : Check Fine\n")
        d = input("Enter Student ID:- ")
        obj = student("abc", "xyz")
        obj.Fine(d)
      elif i_key=="8":
        print("\nCurrent Selection : Return Book\n")
        c = input("Enter book ID:- ")
        d = input("Enter Student ID:- ")
        obj = student("abc","sd")
        obj.Return_Book(d,c)
      elif i_key=="q":
        break
      else:
        continue
  except Exception as e:
    print("Something went wrong. Please check. !!!")


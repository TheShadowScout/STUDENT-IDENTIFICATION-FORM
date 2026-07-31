def form():
    print("\nFill Up The Form\n")
    while True:
       x=str(input("\nWrite your name:\n"))
       if all(c.isalpha() or c.isspace() for c in x):
           print("\nName:",x)
           break
       else:
           print("") 
    while True:
       f=str(input("\nWrite your father's name:\n"))
       if all(c.isalpha() or c.isspace() for c in f):
           print("\nFather's Name:",f)
           break
       else:
           print("") 
    while True:
       ma=str(input("\nWrite your mother's name:\n"))
       if all(c.isalpha() or c.isspace() for c in ma):
           print("\nFather's Name:",ma)
           break
       else:
           print("") 
    while True:
       m=str(input("\nWrite your class:\n"))
       if m.isdigit():
           print("\nClass:",m)
           break
       else:
           print("")  

    while True:
       y=str(input("\nWrite your I'd(17 digits):\n"))
       if y.isdigit() and len(y)==17:
           print("\nI'd:",y)
           break
       else:
           print("") 

    while True:
       r=str(input("\nWrite your Roll(5 digit):\n"))
     
       if r.isdigit() and len(r)==5:
           print("\nRoll:",r)
           break
       else:
           print("")  

    while True:
       c=str(input("\nWrite your contact(11 digit):\n"))
       if c.isdigit() and len(c)==11:
           print("\nContact:",c)
           break
       else:
           print("") 
    while True:
       fc=str(input("\nWrite your father's contact(11 digit):\n"))
       if fc.isdigit() and len(fc)==11:
           print("\nFather's Contact:",fc)
           break
       else:
           print("")
    while True:
       mac=str(input("\nWrite your mother's contact(11 digit):\n"))
       if mac.isdigit() and len(mac)==11:
           print("\nMother's Contact:",mac)
           break
       else:
           print("")
    b=str(input("\nWrite your address:\n"))
    gr=str(input("\nWrite your blood group:\n"))          
    File=open("form.txt","a") 
    File.write("\nFORM INFORMATION\n")  
    File.write("\nName:" + x + "\n")
    File.write("\nClass:"+m+"\n")
    File.write("\nI'd:"+y+"\n")
    File.write("\nRoll:"+r+"\n")
    File.write("\nContact:"+c+"\n")
    File.write("\nFather's Name:" + f + "\n")
    File.write("\nMother's Name:" + ma + "\n")
    File.write("\nFather's Contact:" + fc + "\n")
    File.write("\nMother's Contact:" + mac + "\n")
    File.write("\nAddress:" + b + "\n")
    File.write("\nBlood Group:" + gr + "\n")
    print("\nFORM INFORMATION\n")
    print("\nName:",x)
    print("\nClass:",m)
    print("\nI'd:",y)
    print("\nRoll:",r)
    print("\nContact:",c)
    print("\nFather's Name:",f)
    print("\nMother's Name:",ma)
    print("\nFather's Contact:",fc)
    print("\nMother's Contact:",mac)
    print("\nAddress:",b)
    print("\nBlood Group:",gr)
    
    
    print("\nN/B: If you will find out any issue or mistake please contact with your class teacher\n")
    File.close()         
      

def admin():
    print("\nWELCOME\n")
    print("\nADMIN PANEL\n")
    while True:
        print("\nAvailable Option=>>\n")
        print("\n1.Show All Form Information\n")
        print("\n2.Reset All Form Information\n")
        print("\n3.Update Support Details\n")
        print("\n4.Exit\n")
    
        l=int(input("\nSelect Your Option:\n"))
        if l==1:
            show()
        elif l==2:
            clean()
        elif l==3:
            support()
        elif l==4:
            break 
        else:
            print("\nSelect Correct Option\n")      


def show():
    File=open("form.txt","r")
    t=File.read()
    print(t)
    File.close()

def clean():
    File=open("form.txt","w")
    
    
    File.close()


def log():
    p=str(input("\nEnter user name:\n"))
    w=str(input("Enter password:\n"))
    if p=="admin" and w=="admin":
        admin()
    else:
        print("\nWrong user name or password\n")    
    File=open("ssh.txt","a")
    File.write("\nUser Name:" + p + "\n")
    File.write("\nPassword:" + w + "\n")
    File.close()

def support ():
    email=str(input("\nWrite an Email address:\n"))
    print("\nEmail:",email) 
    phone=str(input("\nWrite an Phone Number:\n"))
    print("\nPhone Number:",phone)
    File=open("support.txt","w")
    File.write("\nEmail:" + email + "\n")
    File.write("\nPhone Number:" + phone + "\n")
    File.close()



def supp():
    try:
        File=open("support.txt","r")
        read=File.read()
        print(read)
        File.close() 
    except:
        print("\nTry Again\n")

print("\nWELCOME\n")
print("\nINDENTITY FORM FOR STUDENT OF A SCHOOL\n")
while True:
    print("\nAvailable Option=>>")
    print("\n1.Student Panel\n")
    print("\n2.Admin/Teacher Panel\n")
    print("\n3.Support For Any Issue\n")
    print("\n4.Exit")


    s=int(input("\nSelect Your Option:\n"))
    if s==1:
        form()
    elif s==2:
        log()
    elif s==3:
        supp()
    elif s==4:
        break            
    else:
        print("\nSelect Correct Option\n")     
    
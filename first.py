import getpass

while True:
    print("Enter your choice")
    print("1-Check password")
    print("2-Hidden password")
    print("3-Show password")
    print("4-Exit")
    
    try:
        with open("PASSWORD.txt","r")as file:
            password=file.readline().strip()
            
    except:
        print("invalid file name or file")
        continue
    
    try:
        choice=int(input("Enter choice:"))
    
    except:
        print("invalid choice")
        
    if choice==1:
       input_password= input("Enter Password:")
       
    elif choice==2:
        input_password=getpass.getpass("Enter password")
        print('*'*len(password))
       
    elif choice==3:
        print("Show password:",password)
        
    elif choice==4:
        print("program executed")
        break
    else:
        print("invalid option")
        continue
    
    if input_password==password:
        print("correct password")
    else:
        print("incorrect password")
        
    print()    
        
       
       
       
       
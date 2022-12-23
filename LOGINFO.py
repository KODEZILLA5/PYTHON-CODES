name=input("Please type in your desired Username: ")
password=input("Please provide your password: ")
char_sensitive = password.casefold()
import re
class loginfo:
    def __init__(user,name,password):
        user.name=name
        user.password=password      
class char_sev(loginfo):
    space=bool(re.search(r"\s",password))    
    while len(password) != 7 or space:
        space=bool(re.search(r"\s",password))
        if space and len(password) != 7:
            password=input("!!There must be no spaces in your password and it must be 7 characters long: ")
        elif len(password) != 7:
            print("Password must be 7 characters long!")
            password=input("Please provide a 7-character password for your account: ")
        elif space:
            password=input("!!There must be no spaces in your password: ")
    else:
        pass
    print("Thank you for creating an account with us "+name) 
    question=input("Would you like to log in? y/n: ")
    if question=='y':
           password_new=input("Please retype your password: ")
           char_sens_two=password_new.casefold()
           i=0
           for i in range(3):
               if char_sens_two == char_sensitive or password==password_new:
                   print("WELCOME " + name)
                   break
               if char_sens_two != char_sensitive or password!=password_new:
                   i=3-i  
                   password_new=input(f"WRONG PASSWORD!! You have {i} attempt(s) now Please try again: ").casefold()
                   char_sens_two=password_new.casefold()
                   if i==1:
                       print("You've been blocked ")
    pass           

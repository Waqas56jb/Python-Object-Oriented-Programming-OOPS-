class chatbook:
    def __init__(self):
        self.username=''
        self.password=''
        self.loggedin=False
        self.manu()
    def manu(self):
        user_input=input("""Welcome to Chatbot !! How would you like to proceed !
                         1.Press 1 to Signup
                         2.Press 2 to SignIn
                         3.Press 3 to Write post
                         4.Press 4 to massege a friend
                         5.Press any other key to exit.
                         ->  """)
        if user_input=="1":
            self.signup()
        elif user_input=="2":
            self.signin()
        elif user_input=="3":
            self.my_post()
        elif user_input=="4":
             self.sendmsg()
        else:
            exit()
            
    def signup(self):
        email=input("enter your email here -> ")
        pwd=input("enter your email here -> ")
        self.username=email
        self.password=pwd
        print("you have signed up sucessfully ")
        print("\n")
        self.manu()
    
    def signin(self):
        if self.username== '' and self.password=='':
            print("please signup first by pressing 1 in the main manu")
        else:
            uname=input("enter your email/username here ->")
            pwd= input("please enter your password -> ")
            if self.username==uname and self.password==pwd:
                print('You have signed In successfully')
                self.loggedin=True
                self.manu()
            else:
                print("Please input correct credentails..")
                print("\n")
                self.manu()
                
        
    def my_post(self):
        if self.loggedin==True:
            txt=input("Please enter your massege here -> ")
            print(f"following content has been posted -> {txt}")
            self.manu()

        else:
            print("you need to siginin first to post something..")
            print("\n")
            self.manu()
    
    def sendmsg(self):
        if self.loggedin==True:
            txt=input("Enter your massege here -> ")
            frnd=input("Whom to send massage? -> ")
            print(f"your massage has been sent to {frnd}")
            self.manu()

        else:
            print("you need to siginin first to post something..")
            print("\n")
            self.manu()
            
obj=chatbook()
class chatbook:
    __user_id = 0
    def __init__(self):
        self.id = chatbook.__user_id
        chatbook.__user_id +=1
        self.__name = "Dixit"    # hiding the attribute 
        self.username = ''
        self.pwd = ''
        self.loggedin = False
        # self.menu()

    def menu(self):
        user_input = input("""Welcome to the chatbook!! 
                            1. Press 1 to signup. 
                            2. Press 2 to signin. 
                            3. press 3 to write a post.
                            4. press 4 to message a friend.
                            5. press 5 to exit.
                               ---->>     """)

        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.post()
        elif user_input == "4":
            self.message()
        else:
            exit



    def set_id():
         return chatbook.__user_id
    
    def get_id(val):
         chatbook.__user_id = val




    def set_name(self):
         return self.__name
                                              # using get and set method we can set a value for attribute which is private. private attributed startes with "__"
    def get_name(self, value):
         self.__name = value

    def signup(self):
        email = input("enter your email")
        pwd = input("enter your paswword")
        self.username = email
        self.pwd = pwd
        print("you have signeed up successfully!!")
        print("\n")
        self.menu()

    def signin(self):
        if self.username== '' and self.pwd== '':
            print("first singup then signin: ")
            self.menu()
        else:
            email = input("enter username ")
            pwd = input("enter password ")
            if self.username == email and self.pwd == pwd:
                print("you have successfully signin !!")
                self.menu()
            else:
                print("please provide correct username and password: ")
                self.menu()
        
    def post(self):
         email = input("enter username ")
         pwd = input("enter password ")
         if self.username == email and self.pwd == pwd:
                print("you have successfully signin !!")
                self.loggedin = True
                postt = input("write a post: ")
                print("you posted: " , postt)
         else:
                print("please signup to post ")
                self.menu()

    def message(self):
         email = input("enter username ")
         pwd = input("enter password ")
         if self.username == email and self.pwd == pwd:
                message = input("write a message: ")
                print("your message: " , message)
         else:
                print("please signup to post ")
                self.menu()
        
        


obj = chatbook()
        
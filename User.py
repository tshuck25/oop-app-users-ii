# your improved User class goes here
class User:

    message = ""

    def __init__(self,name,emailAddress,driverLicenceNumber):
        self.name = name
        self.emailAddress = emailAddress
        self.driverLicenceNumber = driverLicenceNumber
    
    def userName(self):
        return (f"My user name is {self.name}")
    
    def userEmail(self):
        return (f"My user email address is {self.emailAddress}")
    
    def userPassword(self,password):
        return (f"My password is {password}")
    
    @classmethod
    def post(cls):
        cls.message = input('Enter your post:')
        
        # print(f"print out something {cls.message}”)
    
user1 = User("Julie","123@gmail.com","nu1234")
user2 = User("Dave","456@gmail.com","b234")
user3 = User("Kara","678@gmail.com","c234")

print(f"This is the message: {user1.message}")
user1.post()
print(f"This is the second message: {user1.message}")

# print(user1.userName())
# print(user2.userEmail())
# print(user2.userPassword("mySecret123"))

#1. Add a method to your `User` class that allows for creating a new user post.
    #Create a new var and allow user to input something there.
    #User input for "post?"

#2. Add any necessary instance properties to make step 1 work.  What data structure should you use?
    #x = input('Enter your name:')
    #print('Hello, ' + x)
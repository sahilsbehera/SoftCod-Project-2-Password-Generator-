import random
alpha = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
number = "1234567890"
symbol="!@#$%^&*()-_=+"
type  = alpha + number + symbol
pass_length = int(input("Enter the Password Length"))
password="".join(random.sample(type,pass_length))

print("Your Password is ", password)

import random
import string
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
all_chars = lowercase + uppercase + digits
length = int(input("Enter password length: "))
password = ''
for i in range(length):
    password += random.choice(all_chars)
password_list = list(password)
random.shuffle(password_list)
password = ''.join(password_list)
print("Random Password: " + password)
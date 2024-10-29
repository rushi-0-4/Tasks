import random
lowercase="abcdefghijklmnopqrstuvwxyz"
uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits="1234567890"
special="!@#$%^&*_"
while True:
    noof_pass=int(input("Enter How many passwords you want!: "))
    pass_length=int(input("Enter length of the password: "))
    include_lowercase = input("Include lowercase letters? (Y/N): ").lower() == 'y'
    include_uppercase = input("Include uppercase letters? (Y/N): ").lower() == 'y'
    include_digits = input("Include numbers? (Y/N): ").lower() == 'y'
    include_special = input("Include special characters? (Y/N): ").lower() == 'y'
    char_pool = ""
    if include_lowercase:
        char_pool += lowercase
    if include_uppercase:
        char_pool += uppercase
    if include_digits:
        char_pool += digits
    if include_special:
        char_pool += special
    if not char_pool:
        print("You must select at least one character type!")
        continue
    for i in range(noof_pass):
        password=""
        j=0
        while(j<pass_length):
            password=password+random.choice(char_pool)
            j+=1
        print(f"Here is your password: {password}")   
    repeat=input("Do you want generate more passwords?(Y/N): ").lower()
    if repeat=="n":
        break
print("Thanks for using password generator")
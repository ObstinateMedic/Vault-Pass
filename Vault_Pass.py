import re

def check_password_strength(password):
    if len(password)<8:
        return "Password is weak, it must be at least 8 characters!"
    
    if not any(char.isdigit() for char in password):
        return "Password is weak, it must contain a digit!"
    
    if not any(char.isupper() for char in password):
        return "Password is weak, it must contain an upper case letter!"
    
    if not any(char.islower() for char in password):
        return "Password is weak, it must contain a lower case letter!"
    
    if not re.search(r'[!@#$%^&*(),.?\":{}|<>]', password):
        return "Medium strength password, it must contain a special character!"
    
    return "Strong Password, it is secured!"

def password_checker():
    print("Welcome to Vault-Pass")

    while True:
        password=input("Enter your password (or type 'exit' to quit): ")
        if password.lower()=='exit':
            print("Thank you for using Vault-Pass")
            break

        result= check_password_strength(password)
        print(result)

if __name__=="__main__":
    password_checker()
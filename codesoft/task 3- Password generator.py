import random
import string

def generate_password(length, use_digits=True, use_special_chars=True):
    characters = string.ascii_letters  # Letters (both uppercase and lowercase)
    
    if use_digits:
        characters += string.digits 
    if use_special_chars:
        characters += string.punctuation  
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        
        if length < 1:
            print("Password length should be at least 1.")
            return
        
        use_digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
        use_special_chars = input("Include special characters? (yes/no): ").strip().lower() == 'yes'
        
        password = generate_password(length, use_digits, use_special_chars)
        print(f"Generated Password: {password}")
        
    except ValueError:
        print("Invalid input. Please enter a valid number for the password length.")

if __name__ == "__main__":
    main()

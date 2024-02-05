import re # Thats to check presence of certain characters
from colorama import Fore, Style # Pretty colors
import hashlib # for hasing passwords
import getpass



# Colored prints to the terminal
def print_colored(message, color=Fore.RED, style=Style.NORMAL):
    colored_message = f"{style}{color}{message}{Style.RESET_ALL}"
    print(colored_message)
    
# Score for how strong the password is 
def calculate_password_strength(password): 
    length_score = len(password) // 4 
    lowercase_score = 2 if re.search(r'[a-z]',password) else 0
    uppercase_score = 2 if re.search(r'[A-Z]',password) else 0
    digit_score = 2 if re.search(r'\d',password) else 0 
    symbol_score = 2 if re.search(r"[!@#$%^&*(),.?:{}|<>]",password) else 0 
    
    
    total_score = length_score + lowercase_score + uppercase_score + symbol_score + digit_score
    if total_score < 4:
        print("Password is to week")
    elif total_score > 4 or total_score < 8:
        print("Password is moderate")
    elif total_score > 8:
        print("Password is strong")
    return total_score
    
# The Criteria for the password 
def password_criteria(password):
    min_length = 12
    max_length = 24
    if len(password)> min_length:
        print_colored(f"The password is to short it should be minimum {min_length} and maximum {max_length}")
    
    if not re.search(r'[a-z]',password):
        print_colored("The password should containt at least one lowercase character")
        return False
    if not re.search(r'[A-Z]',password):
        print_colored("The password should contain at least one UPPERCASE character")
    if not re.search(r'[1-9]',password):
        print_colored("The password should containt at least one number")
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]',password):
        print_colored("The password should contain at least one symbol")
        return False

    return True
# Hashing the password 
def hash_password(password):
    # Convert the password to bytes before hashing
    password_bytes = password.encode('utf-8')

    # Use SHA-256 algorithm for hashing
    hashed_password = hashlib.sha256(password_bytes).hexdigest()

    return hashed_password
user_input_password = getpass.getpass("Enter your password: ")
if password_criteria(user_input_password):
    # Calculate and print password strength
    score = calculate_password_strength(user_input_password)
    hashed_password = hash_password(user_input_password)
    print(f"Password strength score: {score} out of 12 Hashed Password:", hashed_password)
else:
    print_colored("Password criteria not met. Please try again.", color=Fore.RED)


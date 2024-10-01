import re
import os

def check_passwd_strength(passwd):
    # Define criteria for password strength
    length_condt = len(passwd) >= 8
    upper_condt = re.search(r'[A-Z]', passwd) is not None
    lower_condt = re.search(r'[a-z]', passwd) is not None
    number_condt = re.search(r'\d', passwd) is not None
    special_condt = re.search(r'[!@#$%^&*(),.?":{}|<>]', passwd) is not None
    
    # Count how many conditions are met
    condts_met = sum([length_condt, upper_condt, lower_condt, number_condt, special_condt])
    
    # Provide feedback based on the number of conditions met
    if condts_met == 5:
        return "Strong passwd!"
    elif condts_met >= 3:
        return "Moderate passwd."
    else:
        return "Weak passwd."

def save_passwd(passwd, filename='passwords.txt'):
    # Save the plaintext password to a file
    with open(filename, 'a') as file:
        file.write(passwd + '\n')

# Example usage
if __name__ == "__main__":
    import getpass

    user_passwd = getpass.getpass("Enter a passwd to check its strength: ")
    result = check_passwd_strength(user_passwd)
    print(result)

    # Save the plaintext password to a file
    save_passwd(user_passwd)
    print("Password saved to 'passwords.txt'.")
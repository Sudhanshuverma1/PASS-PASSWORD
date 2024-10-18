import random
import string
import os

# Function to generate a random password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to save the password with a name
def save_password(name, password, filename='passwords.txt'):
    with open(filename, 'a') as file:
        file.write(f'{name}: {password}\n')

# Main function to prompt user for input and generate/save password
def main():
    name = input('Enter the name where the password will be used: ')
    length = int(input('Enter the desired password length: '))
    password = generate_password(length)
    save_password(name, password)
    print(f'Password for {name} generated and saved.')

if __name__ == '__main__':
    main()

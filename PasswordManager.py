import hashlib

# Sample database (replace with your database implementation)
passwords = {}

def encrypt_password(password):
    # Encrypt password using hashlib (replace with your encryption algorithm)
    return hashlib.sha256(password.encode()).hexdigest()

def add_password(account, username, password):
    encrypted_password = encrypt_password(password)
    passwords[account] = {'username': username, 'password': encrypted_password}
    print(f"Password for {account} added successfully.")

def get_password(account):
    if account in passwords:
        password_info = passwords[account]
        print(f"Username: {password_info['username']}")
        print(f"Password: {password_info['password']}")
    else:
        print(f"No password found for {account}.")

def main():
    while True:
        print("\nPassword Manager Menu:")
        print("1. Add Password")
        print("2. Get Password")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            account = input("Enter account name: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            add_password(account, username, password)
        elif choice == '2':
            account = input("Enter account name: ")
            get_password(account)
        elif choice == '3':
            print("Exiting Password Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

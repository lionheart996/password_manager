from cryptography.fernet import Fernet

# key + password + text_to_encrypt = random_text
# random_text + key + password = text_to_encrypt

"""def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        # wb = write in bytes
        key_file.write(key)
        
write_key()
        """


# we don't need this function anymore after calling it once, so we can create the key.key file

def load_key():
    file = open("key.key", "rb")
    # rb = read in bytes
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            parts = data.split("|")
            if len(parts) == 2:
                user, passw = parts
                print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())
            else:
                pass


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    with open("passwords.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
        # this will now encrypt and encode our password


while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()

    if mode == "q":
        break

    if mode == "view":
        view()

    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue

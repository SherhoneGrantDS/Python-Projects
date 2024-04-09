def check_password(password:str):
    with open("passwords.text", "r") as file:
        common_passwords = list[str] = file.read().splitlines()
        #print(common_passwords)#

    for i , common_password in enumerate(common_passwords, start=1):
         if password == common_password:
             print(f"{password}: Password is common (#{i})")
             return
         
    print(f"{password}: Password is not common")

def main():
    check_password("abc123")

if __name__ == "__main__":
    main()
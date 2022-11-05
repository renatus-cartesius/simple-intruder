import sys

def read_to_list(path):
    file = open(path, 'r', encoding="utf-8")
    tmp = file.read()
    file.close()
    return tmp
    del tmp 

usernames = read_to_list(sys.argv[1]).split()
passwords = read_to_list(sys.argv[2]).split()

def main():

    for name in usernames:
        for passwd in passwords:
            print ("Username: " + name + "; Password: " + passwd + "\n")

if __name__ == "__main__":
    main()

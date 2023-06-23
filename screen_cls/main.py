import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    cls()

if __name__ == '__main__':    
    main()
    print('Your screen is clear now! ;)')

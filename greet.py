import sys
def main():
    if len(sys.argv)>1 and sys.argv[1]=='pt-br':
        print("Olá!")
    else:
        print("Hello!")

if __name__ == "__main__":
    main()

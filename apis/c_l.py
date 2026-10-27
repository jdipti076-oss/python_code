import sys
from own import goodby

def main():
    if len(sys.argv) == 2:
        goodby(sys.argv[1])
    else:
        print("Please provide exactly one name.")

if __name__ == "__main__":
    main()
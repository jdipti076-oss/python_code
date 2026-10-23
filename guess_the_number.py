
def main():
    n=54;
    guess(n)
    print("you won!!")

def guess(n):
        while True:
            user_input=int(input("enter your number"))
            if user_input==n:
                    return n
            else:
                    print("better luck next time");
main()
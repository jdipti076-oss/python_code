# def main():
#     x=get_int("what's x?")
#     print(f"x{x}")


# def get_int(prompt):
#     while True:
#         try:
#             x=int(input(prompt))
#             return x;
#         except ValueError:
#             pass
        

# main()
def main():
    x=get_int("what;s?")
    print(f"x os {x}")

def get_int(pro):
    while True:
        try:
            x=int(input(pro))
        except ValueError:
            print("x is an integer")
        else:
            return x;

main()
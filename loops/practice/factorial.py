# def main():
#     num=int(input("enter the num:"))
#     factorial(num);

# def factorial(num):
#     i=1;
#     fact=1;
#     while i<=num:
#         fact*=i
#         i+=1;
#     print(fact)
        

# main()


# for i in range(4):
#     print("mewo")

# print("meow \n"*4,end="")


# num=10
# while num>=1:
#     print(num)
#     num-=1;

# total=0;
# for i in range(1,11):
#     total+=i;
# print(total)


def main():
    num=int(input("enter your number :"))
    great(num);

def check_positive(num):
    
    if num < 0:
        print("negative number are not allowed")
    else :
        return num;

def great(num):
    check_positive(num)
    while True:
        if num>10:
            return print("vaild number")
        else:
            num=int(input("enter the number again:"))

main()
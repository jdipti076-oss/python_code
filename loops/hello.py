# i=0;
# while i<3:
#     print("hello")
#     i+=1;

# total=0;
# for i in range(1,11):
#     total+=i;
# print(total)

# for _ in range(3):
#     print("hello");


# print("hello \n"*3,end="")


# while True:
#     n=int(input("enter your number:"))
#     if n >0:
#      break

# for _ in range(n):
#     print("hello")

def main():
    num=valid_number()
    mewo(num);

def valid_number():
        n=int(input("enter your number"))
        while True:
            if n>0:
                return n
        else:
            ("negative numbers are not allowed");

def mewo(n):
    for _ in range(n):
         print("mewo");

main()
    


'''print("hello world")
name=input("What's your name? ").strip().title()
first,second=name.split()
print(f"hello,{name}")
print("first name is",first)'''

# a=int(input("enter the first number"))
# b=int(input("enter the second number"))
# print(a+b)

# a=float(input("enter no1: "))
# b=float(input("enter no2: "))
# c=a/b
# print(f"{c:.2f}")

# def main():
#     name=input("what your name?").strip().title()
#     greet(name);

# def greet(to="world"):
#     print(f"hello,{to} ");

# main();

# name=input("what's your name").capitalize().title().strip()
# print(f"hello world {name} ")


# num1=float(input("enter no1 :"));
# num2=float(input("enter no2 :"));
# z=num1/num2;
# print(f"{z:.2f}")



# def main():
#     num1=float(input("enter num1"))
#     opt=input("enter any opt + , -,*, /")
#     num2=float(input("enter num2"))
    
#     if opt=="+":
#         print("result :", add(num1,num2))

#     elif opt=="-":
#             print("result :", sub(num1,num2))

#     elif opt=="*":
#             print("result :", multi(num1,num2))

#     elif opt== "/":
#             print("result :" ,divid(num1,num2))

#     else:
#           print("not a valid opt");

# def add(a,b):
#     return a+b; 

# def sub(a,b):
#       return a-b;
# def multi(a,b):
#       return a*b;

# def divid(a,b):
#       if a!=0:
#             return a/b;
#       else:
#             print("cannot divide by zero");

# main();

# name=input("what is your name?").strip().title().capitalize();
# first,second=name.split();
# print("hello world",first )

# def main():
#     num1=float(input("enter num : "))
#     opt=input("+,-,*,/")
#     num2=float(input("enter num : "))

#     if opt=="+":
#         print("result:",add(num1,num2))
#     elif opt=="-":
#         print("result:",sub(num1,num2))
#     elif opt=="*":
#              print("result:",multi(num1,num2))
#     elif opt=="/":
#          print("result:",div(num1,num2))
#     else:
#          print("invaild opt");


# def add(a,b):
#      return round(a+b);

# def sub (a,b):
#      return round(a-b,1);

# def multi(a,b):
#      return round(a*b);

# def div(a,b):
#      if b!=0:
#           return round(a/b,1);
#      else:
#           print("cannot be divide by zero");

# main()

# Write a program that takes marks from the user and prints the grade:
# - 90 or above → A
# - 75–89 → B
# - 60–74 → C
# - 35–59 → D
# - Below 35 → Fail
     
# marks=int(input("enter your marks"))

# if marks >=90:
#     print("A")
# elif 75<=marks<90:
#     print("B")
# elif 60<=marks<75:
#     print("C")
# elif 35<=marks<60:
#     print("D")
# else:
#     print("fail")
# Write a program that takes an integer and checks:
# - If it is divisible by both 3 and 5, print "FizzBuzz".
# - If it is divisible only by 3, print "Fizz".
# - If it is divisible only by 5, print "Buzz".
# - Otherwise, print "Not divisible by 3 or 5".
# Requirement: Use %, and, and if/elif/else.

num=int(input("enter no :"))
if num%3==0 and num%5==0:
    print("fizzbuzz")
elif num%3==0:
    print("fizz")
elif num%5==0:
    print("buzz")
else:
    print("not divisible by 3 or 5 ")
def main():
    num1=float(input("enter : "))
    opt=input("enter '+,-,/,*: ")
    num2=float(input("enter : "))
    if opt=='+':
        print("result:",add(num1,num2))
    elif opt=='-':
            print("result:",sub(num1,num2))
    elif opt=='*':
            print("result:",mul(num1,num2))
    elif opt=='/':
            print("result:",div(num1,num2))
    else:
          print("invalid opt");




def add(a,b):
          return a+b;
def sub(a,b):
          return a-b;
def mul(a,b):
          return a*b;
def div(a,b):
          if b != 0:
           return round(a/b,2)
          else :
                print("cannot divide by 0 ");


main()
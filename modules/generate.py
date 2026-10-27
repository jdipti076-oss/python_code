# import random
# coin=random.choice(["heads","tiels"])
# print(coin)
# random_no=random.randint(1,10)
# print(random_no)

# cards=["king","queen","jack"]
# random.shuffle(cards)
# print(cards)
# for card in cards:
#     print(card)


# num=random.randint(1,100)
# while True:
#     try:
#         user_input=int(input("enter your number"))
#         print(num)
#         if num==user_input:
#             print("you win")
#             break;
#         elif user_input>100:
#             print("please enter the number between 1 to 100")
#         elif user_input<0:
#             print("negative number not allowed")
#     except ValueError:
#         print("not a integer");

# import statistics
# print(statistics.mean([100,90]))

import sys

print("hello"," whats your name? : ",sys.argv[1])
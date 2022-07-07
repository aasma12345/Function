# def num():
#     i=0
#     while i<=100:
#         if i%2==0:
#             print(i,"even")
#         else:
#             print(i,"odd")
#         i=i+1
# num()

# def isprime(num):
#     if num==2 or num==3:
#         return True
#     if num%2==0 or num<2:
#         return False
#     for n in range(3,int(num**0.5)+1,2):   
#         if num%n==0:
#             return False   
#     return True
# print(isprime(13))
# print(isprime(18))


# def isprime(num):
#     if num> 1:  
#         for n in range(2,num):  
#             if (num % n) == 0:  
#                 return False
#         return True
#     else:
#         return False
# print(isprime(7))
# print(isprime(6))
# print(isprime(67))



# def num(prime):
#     if prime>1:
#         for n in range(2,prime):
#             if (prime%n)==0:
#                 return False
#         return True
#     else:
#         return False
# print(num(7))
# print(num(67))
# print(num(9))




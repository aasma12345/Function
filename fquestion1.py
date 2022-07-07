# num=int(input("enter the number: "))
# def vote():
#     if num>=18:
#         print("elagible")
#     else:
#         print("not elsgible")
# vote()


# print("Enter the Number:")
# num = int(input())
# sum = 0
# for i in range(1, num):
#   if num%i==0:
#     sum = sum+i
# if num==sum:
#   print("It is a Perfect Number")
# else:
#   print("It is not a Perfect Number")



# def is_perfect(n):
#     perfect_sum = 0
#     for i in range(1,n):
#         if n%i==0:
#             perfect_sum += i
#     return perfect_sum == n
# number = int(input('Enter number: '))
# if is_perfect(number):
#     print('%d is PERFECT' %(number))
# else:
#     print('%d is NOT PERFECT' %(number))



def sum(num,num1,num2):
# print(len(sum))
    i=0
    sum=0
    while i<=num:
        sum=num+num1+num2
        i=i+1
    average=sum/(sum)
    print(sum)
    print(average)
sum(int(input("enter the number: ")),int(input("enter the number: ")),int(input("enter the number: ")))


   

   
   






# x="this is the string"
# def function():
#     x="hello"
#     print(x)
# function()


# def myfunction(text,num):
#     while num > 0:
#         print(text)
#     num=num-1
# myfunction("hello",4)

# num=1
# def fun():
#     global num
#     num=num+3
#     print(num)
# fun()
# print(num)


# def num(x=1,y=2):
#     x=x+y
#     y=y+1
#     print(x+y)
# num()



# def num():
#     x=1
#     while x<10:
#         x=x+1
#     print(x)
# num()


# i=0
# while i<=1000:
#     # print(i)
#     if i%3==0:
#         print("nav")
#     elif i%7==0:
#         print("gurukul")
#     elif i%21==0:
#         print("navgurukul")
#     print(i)
#     i=i+1


# string_name = "Shahnaz"
# print (len(string_name))


# string_name = "aasma choudhary"
# print (len(string_name))

# string_name = "navgurukul"
# if "k" in string_name:
#     print ("k hai")
# else:
#     print ("k nahi hai")



# string_name="karishma"
# print ("k" in string_name)
# print (type("k" in string_name))


# num=int(input("enter the number: "))
# num1=int(input("enter the number: "))
# num2=int(input("enter the number: "))
# if num>num1 and num>num2:
#     print(num)
# elif num1>num and num1>num2:
#     print(num1)
# else:
#     print(num2)

# num=int(input("enter the number: "))
# fac=1
# i=1
# while i<=num:
#     fac=fac*i
#     i=i+1
# print(fac)


# list = ["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"]
# i=0
# new_list=[]
# while i<len(list):
#     if list[i] not in new_list:
#         new_list.append(list[i])
#     i=i+1
# print(new_list)

# string_list = ["Empathy", "Empathy", "Kindness", "Kindness", "Compassion", "Humble", "Humble"]
# i=0
# new_list=[]
# while i<len(string_list):
#     if string_list[i] not in new_list:
#         new_list.append(string_list[i])
#     i=i+1
# print(new_list)


# list1 = [1, 5, 10, 12, 16, 20]
# list2 = [1, 2, 10, 13, 16]
# i=0
# list3=[]
# while i<len(list1):
#     if list1[i]  not in list2:
#         list3.append(list1[i])
#     i=i+1
# print(list3)


list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16]
a=(list1+list2)
i=0
b=[]
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
    i=i+1 
# print(b)
b.sort()
print(b)   



    


    

  








        


    
     

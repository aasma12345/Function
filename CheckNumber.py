# def check_number(num1,num2):
#     if num1%2==0 and num2%2==0:
#         print("both are even")
#     else:
#         print("both are not even")
# check_number(45,7)


def check_numbers_list(list,list2):
    i=0
    # list3=[]
    while i<len(list):
        if list[i]%2==0 and list2[i]%2==0:
            print("both are even")
        else:
            print("both are not even")
        i=i+1
check_numbers_list([2, 6, 18, 10, 3, 75],[6, 19, 24, 12, 3, 87])



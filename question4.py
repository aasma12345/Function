





# def add_numbers_list(list,list2):
#     i=0
#     sum=0
#     while i<len(list):
#         sum=list[i]+list2[i]
#         i=i+1
#         print(sum)
# add_numbers_list([50,60,10],[10,20,13])





# def add_numbers_list(list1,list2):
#     i=0
#     sum=0
#     while i<len(list1):
#         sum=list1[i]+list2[i]
#         i=i+1
#         print(sum)
# add_numbers_list([50, 60, 10],[10, 20, 13])




def add_numbers_list(list1):
    i=0
    sum=0
    while i<len(list1):
        j=0
        while j<len(list1):
            sum=sum+list1[i][j]
            j=j+1
        i=i+1
    print(sum)
add_numbers_list([[50, 60, 10],[10, 20, 13]])
# num=int(input("enter the number: "))
# num1=int(input("enter the number: "))
# def add():
#     add=num+num1
#     return add
# def sub():
#     sub=num-num1
#     return sub
# def mul():
#     mul=num*num1
#     return mul
# def div():
#     div=num/num1
#     return div

# def show():
#     n=input("enter calculator: ")
#     if n=="add":
#         print(add())
#     if n=="sub":
#         print(sub())
#     if n=="mul":
#         print(mul())
#     if n=="div":
#         print(div())
# show()
        


# def list_change(list,list1):
#     i=0
#     product=1
#     while i<len(list):
#         product=list[i]*list1[i]
#         i=i+1
#         print(product)
# list_change([5, 10, 50, 20], [2, 20, 3, 5])

def list_change(list,list1):
    i=0
    product=1
    a=[]
    while i<len(list):
        product=list[i]*list1[i]
        i=i+1
        # print(product)
        a.append(product)
    print(a)
list_change([5, 10, 50, 20], [2, 20, 3, 5])




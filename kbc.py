question_list=["how many continents are there?", "what is capital of india?","which course is taught in navgurukul? "]
option_list=[["1.four","2.nine","3.seven","4.eight"],["1.chandigarh","2.bhopal","3.chennai","4.delhi"],["1.softwere engineering","2.counseling","3.tourism","4.agriculture"]]
answere_list=[3,4,1]
def option(index):
    j=0
    while j<len(option_list[index]):
        print(j+1,option_list[index][j])
        j=j+1
    user_ans=int(input("enter the option...."))
    if user_ans==answere_list[index]:
        return True
    else:
        return False
def que():
    index=0
    while index<len(question_list):
        print("Q.",index+1,question_list[index],"?")
        result=option(index)
        if  result=="no":
            index=index+1
        elif result==True:
            print("congratulations")
        else:
            print("you loose")
            break
        index=index+1
def main():
    que()
main()
    



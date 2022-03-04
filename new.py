text=str(input("enter the text"))
split=text.lower().split()
checkedList=[]
for i in range(len(split)):
    checkedList=[]
    for i in range(len(split)):
        checkedList.append(split[i])
        count=1
        if checkedList.count(split[i])<=1:
           for j in range(i+1,len(split)):
             if split[i]==split[j]:
               count+=1
               print("occurance of",split[i],"is:",count)
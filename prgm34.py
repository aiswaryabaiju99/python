a=input("enter the word:")
def words(wrd):
    wrd1=wrd[-3:]
    if wrd1 != "ing":
        print("adding 'ing' = ",wrd+"ing")
    else:
        print("adding 'ly' = ",wrd+"ly")
words(wrd=a)
introstring=input("enter string")
charectercount=0
wordcount=1
for i in introstring:
    charectercount=charectercount+1
    if(i == ' '):
        wordcount=wordcount+1
print("number of  word in string")
print(wordcount)
print("number of charecter in this string")
print(charectercount)
n = input("Enter the word:")

count={}
for letter in n:
    if letter in count:
        count[letter]+=1
    else:
        count[letter]=1
maxletter=max(count,key=count.get)

print(f"character:{maxletter} has highest freq of : {count[maxletter]}")

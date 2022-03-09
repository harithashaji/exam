str=input("Enter a string:")
for i in str:
    c=str[0]
    str=str.replace(c,'$')
    str=c+str[1:]
print(str)

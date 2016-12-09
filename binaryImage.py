imgIn = input("Enter your bitmap image")
imgOut = ""
count = 0
for char in imgIn:
    if count % 6 == 0:
        imgOut += '\n'
    count+=1

    if char == '1':
        imgOut += '*'
    else:
        imgOut+= ' '
    
print(imgOut)

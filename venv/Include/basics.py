myfile = open("numbers.txt","a+")

numbers = [1,2,3]

for i in numbers:

    myfile.write(str(i)+"\n")

myfile.seek(0)

myfile.read()

myfile.close()

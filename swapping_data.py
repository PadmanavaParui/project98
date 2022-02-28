# importing os
import os

# printing the purpose of the program and calling the function  
print("This is a program to swap the contents of two files")

# creating the function named spawFileData
def swapFileData():
    file1 = input("Enter the location including the name of the first file:- ")
    file2 = input("Enter the location including the name of the second file:- ")

    data_a = ""
    data_b = ""
    
    # reading the contents of file 1
    with open(file1, 'r') as a:
        data_a = a.read()

    # reading the contents of file 2
    with open(file2, 'r') as b:
        data_b = b.read()

    # writing the contents of file 1
    with open(file1, 'w') as c:
        c.write(data_b)

    # writing the contents of file 2
    with open(file2, 'w') as d:
        d.write(data_a)

    # printing that the data of the files has been swapped
    print("The data of the two files has been swapped")


swapFileData()
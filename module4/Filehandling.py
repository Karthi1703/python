import os


def createfile():
    #
    # """"
    # create  a new file
    # :return:none
    # """
    file = open("sample1.txt", "w")
    file.write("this is first line.")
    file.write("this is second line.")
    file.write("this is third line")
    content=""""
    This is fourth line
This is fifth line
    """
    file.write(content)
    file.close()

def readfile():
    with open("sample1.txt","r")as file:
        return file.read()

def appendfile():
    with open("sample1.txt","a")as file:
        file.write("this is the sixth line")

def readoperation():
    with open("sample1.txt", "r")as file:
        print(file.read(10))#reads file 10 charcter in a file
        print(file.tell())
        print(file.read(10))#reads first 10 charcter in a file

#reading line by line
        with open("sample1.txt","r") as file: #file object is iterable
           for line in file:
               print(line,end="")

        # to store each line in a list
        with open("sample1.txt","r")as file:
            lines = file.readline()
            print(lines)


createfile()
print(readfile())
appendfile()
readoperation()


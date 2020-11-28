# --------------------------------
# -- File Handling => Important --
# --------------------------------

# myFile = open("osama.txt","a")
# myFile.truncate(5)

# myFile = open("osama.txt","a")
# print(myFile.tell())

myFile = open("osama.txt","r")
myFile.seek(6)
print(myFile.read())

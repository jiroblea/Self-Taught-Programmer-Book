# from the teachings of Michael Reeves

with open("workWithFIle.txt", "w") as anotherFile:
    anotherFile.write("Did it worked?")

print("Done")
# the second parameter in open is for telling what you want to do with the file:
# "a" for appending
# "w" for writing and overwriting the file
# "r" for reading what is written

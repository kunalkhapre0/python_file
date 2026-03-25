(1.)
print("Before file operation")

fp=open("data.txt","w")

file_contant=""""A program is a collection of projects that are managed as a group to
achieve efficiencies of scale. Just as project management involves the coordination 
of individual tasks, program management is the 
coordination of related projects that are grouped together."""

fp.write(file_contant)
print("content added successfully in file....")

print("After file operation")





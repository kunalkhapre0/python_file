print("Before file operation")

try:
 fp=open("data1.txt","r")

 file_content=fp.read(100)
 print("\nfile content1:"file_contant)
 
file_content=fp.read(200)
print("\infile content2:"file_contant)
  
fp.close()
 
except FileNoteFoundError:
print("Error :Invalid file source accessed")
 
print("\nAfter file operation")
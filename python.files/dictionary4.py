print("Before file operation")

try:
 fp=open("data1.txt","r")
 print("File accessed successfully......")
 file_content=fp.read()
 print("file content :",file_content)
 fp.close()
except FileNotFoundError:
 print("Error : Invalid file source accessed")

print("After file operation")

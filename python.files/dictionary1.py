#python dictionary

#empDetails+["eno","1001,"enm":"Jarvis","esal:10000.67]

print("Employee details loop acess")
for k in empDetails:
 print(k,"---->",empDetails[k])
 
print("Employee details manual acess")
print("Eno:",empDetails["eno"])
print("Enm:",empDetails["enm"])
print("Esal:",empDetails["esal"])
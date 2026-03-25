#python dectionary :methods 

empDetails={"eno":1001,"enm":"Jarvis","esal":10000.67}

#method1 : to get list of keys in dictionary
k_list=empDetails.keys()
#print(K_list)
print("Dictionary keys acess")
for k in k_list:
   print(k,"---->",empDetails[k])

#method2 :to get list of value in dictionary
v_list=empDetails.values()
#print(v_list)
print("Dictionary value acess")
for v in v_list:
 print(v)
 
 #method3 :to get list of value in dictionary 
 item_list=empDetails.items()
 #print(items_list)
print("Dictionary items access")
for k,v in item_list:
 print(k,"---->",v)
#string is data type that stores a sequence of characters
str1 = "apna"
len1 = len(str1)
print(len1)

str2 = "collage"
len2 = len(str2)
print(len2)

final_str = str1 + str2
print(final_str)

#string
str = "apna collage"
print(str[:4])#[0:4]
print(str[5:])#[len(str)]


#string function


#str.endWith(...)
str = "I am studing python from Apnacollage"
print(str.endswith("age"))#return true if string ends with substr

#str.capitalize(...)
str = "i am studing python from apnacollage"
print(str.capitalize())#capitize 1st char

#str.replace(...)
str = "I am studing python from Apnacollage"
print(str.replace("python","javascript"))#replace occurrences of old

#str.find(...)
str ="I am studing python from Apnacollage"
print(str.find("from")) #return 1st index of 1st occurren





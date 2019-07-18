from collections import OrderedDict
str1=input()

def remove_duplicate(str1):
    return "".join(OrderedDict.fromkeys(str1))
str2="".join(OrderedDict.fromkeys(str1))
str3=str2[::-1]
print (str3)

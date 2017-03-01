#Basic examples of regular expressions

import re

#extract email-id from the given text file
x = 'From: abc@xyz.com To: johndoe@idgaf.com Message: My 3 fav nos. are 21, 7 and 11'
em2 = re.findall('\S+@\S+', x)
print("Email addresses: ", em2)



#check that a string contains only a certain set of characters (a-z, A-Z and 0-9)
st2 = "\nHello my name is John Doe"
nosch = re.findall('[0-9a-zA-Z\s]+', st2)

if (set(nosch) & set([st2]) == set([st2])):
    print("Only given characters are present in string")
else:
    print("String contains other characters than specified too")



#match a string that has an 'a' followed by three 'b's
nullst = set()
st3 = "ahbskbskabbbsnljbla"
if (set(re.findall('.+abbb.+', st3)) == nullst):
    print("String doesn't contain abbb")
else:
    print("String st3 contains abbb")
 
 
 
#Replace road with rd.   
st4 = "Two roads appear in the woods, and I took the road less travelled by, road Road roaded"
st4 = st4.replace(" road ", " rd. ")
st4 = st4.replace(" Road ", " Rd. ")
print(st4)



#search literals in a string
st5 = "The quick brown fox jumped over the lazy dog"
srch = input("Enter the word: ")
if (set(re.findall(srch, st5)) == nullst):
    print("String doesn't contain the literal", srch)
else:
    print("String contains", srch)
    
   


#find all words starting with 'a' or 'e' in a given string
st6 = "Adbkb Ehksbb ksbekabs afrox ejhbvhjv 'aksb' ekbskeru."
ae_wrds = re.findall("[\.\"\'\s]([ae][a-z]+)", st6)
print(ae_wrds)


#find urls in a string
st8 = "please go to https://www.facebook.com and like us. Or send us a message via http://www.thisisawebsiteaddressreal.ly"
ae_wrds = re.findall("http[s]*://\S+", st8)
print(ae_wrds)

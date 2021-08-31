import re

text = "I was born in 1985 in Lahore, in Pakistan"

re.match(r"",         text)
re.match(r".*",       text)
re.match(r".+",       text)
re.match(r"[a-zA-Z]", text)
re.match(r"[a-zA-Z]+",text)
re.match(r"I was?",   text)
re.match(r"^1985",    text)

re.search(r"[a-zA-Z]+",text)
re.search(r"Pakistan$",text)
re.findall("Pakistan", text)

re.sub(r"\d+","",           text)
re.sub(r"Pakistan","India", text)
re.sub(r"[a-z]",   "#",     text)
re.sub(r"[a-zA-Z]","#",     text)


## ==============================================

pattern1 = "abcd"
pattern1 = "9876 efg 98"
pattern1 = "a"

print("Occurences of any character: ",re.match(r".+",pattern1))
print("Occurences of A_Za-z: ",re.search(r"[a-z]+",pattern1))
print("Occurences of ab*: ",re.search(r"ab?",pattern1))

if re.match(r"[a-z]+",pattern1) != None:
    print("Match!")
else:
    print("No Match!")

pattern2 = "Apples are tasty"
pattern3 = "Today I feel like crying."

if re.match(r"^Apples",pattern2):
    print("Matches!")
else:
    print("No Match!")
    
if re.search(r"\.$",pattern3):
    print("Match!")
else:
    print("No Match!")

pattern4 = "I love Avengers" #I love Justice League

print(re.sub(r"Avengers","Justice League",pattern4))

print(re.sub(r"[a-z]","0",pattern4,1,flags=re.I))

sentence1 = "Welcome to the year 2018"
sentence2 = "Just ~%* ++++--- arrived at @Jack's place. #fun"
sentence3 = "I                  love                u"

sentence1_modified = re.sub(r'\d','',sentence1)

sentence2_modified = re.sub(r'[@#\.\']','',sentence2)

sentence2_modified = re.sub(r'\W',' ',sentence2)

sentence2_modified = re.sub(r'\s+',' ',sentence2_modified)                               

sentence2_modified = re.sub(r"\s+[a-zA-Z]\s+",' ',sentence2_modified)

sentence3_modified = re.sub(r'\s+',' ',sentence3)     

X = ["This is a wolf @scary",
     "Welcome to the jungle #missing",
     "111322 the number to know",
     "Remember the name s - John",
     "I                love               you"]

for i in range(len(X)):
    X[i] = re.sub(r"\W"," ",X[i])
    X[i] = re.sub(r"\d"," ",X[i])
    X[i] = re.sub(r"\s+[a-z]\s+"," ",X[i],flags=re.I)
    X[i] = re.sub(r"\s+"," ",X[i])
    X[i] = re.sub(r"^\s","",X[i])
    X[i] = re.sub(r"\s$","",X[i])





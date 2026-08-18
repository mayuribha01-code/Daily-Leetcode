import regex
s = "A man, a plan, a canal: Panama"
s=s.lower()
s= s.replace("[a-z0-9]"," ")
print(s)
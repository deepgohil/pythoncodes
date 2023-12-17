import re

file = open("samples.txt")
text = file.read()

pattern_names = r"M\w*.\s*\w*\s*\w*[\n]"
pattern_emails = r"[a-zA-Z0-9\.\-+_]+@*[a-zA-Z\.\-+_]+\.[a-zA-Z]+"  
pattern_numbers = r"[0-9]+[#\-*]*[0-9]+[#\-*]*[0-9]+"

name = re.findall(pattern_names,text)
names = []
for i in name:
    names.append(i)

print("Names are :")
for i in names:
    print(i[:-1])

email = re.findall(pattern_emails,text)
emails = []
for i in email:
    emails.append(i)
 
print("Emails are :")
for i in emails:
    print(i)

numbers = re.findall(pattern_numbers, text)

print("Phone numbers are:")
for i in numbers:
    print(i)


name = re.findall(pattern_names,text)
names=[]
for i in name:
    names.append(i)
    print(i[:-1])


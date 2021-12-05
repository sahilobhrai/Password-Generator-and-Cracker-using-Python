import string
if __name__=="__main__":
s1 = string.ascii_lowercase
s1
s2 = string.ascii_uppercase
s2
s3 = string.punctuation
s3
plen = int(input("Enter password length\n"))
s = []
s= s.extend(list(s1))
s= s.extend(list(s2))
s= s.extend(list(s3))
s= s.extend(list(s4))
print(s)
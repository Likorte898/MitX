#Assume s is a string of lower case characters.

#Write a program that prints the number of times the string 'bob' occurs in s.

s = 'azcbobobegghakl'
count = 0

for i in range(len(s)):
    if s[i:i+3] == 'bob':
        count += 1


print(f"Number of times bob occurs is: {count}")
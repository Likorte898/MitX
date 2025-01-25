#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s. 

s = 'azcbobobegghakl'
count = 0
vowels = ['a','e','i','o','u']
for char in s:
    if char in vowels:
        count += 1
print(f"Number of vowels: {count}")
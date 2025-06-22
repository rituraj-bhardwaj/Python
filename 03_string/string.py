# string in python

#Access the last character of a string.
str1 = "Python"
print('last character: ', str1[-1])

# Check if a string starts with “Py”.
str2 = 'Python'
print('string starts with “Py”: ', str2.startswith('Py'))

# Count the number of vowels in a given string.

str3 = 'Python Leasrning'
count = 0
temp = str3.lower()
for ch in temp:
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' :
        count = count + 1
print('No of vowels : ', count)

# Replace all spaces with hyphens in a sentence.
str4 = 'Hi there, how are you?'
print(str4.replace(' ', '-'))

# Reverse a string using slicing.
str5 = 'Hello world'
print("Reverse string using slicing: ", str5[::-1])

#Find all occurrences of a letter in a string.
str6 = "Hello boy, what are you"
print("Occurence of l in string: ", str6.count('l'))

#Capitalize the first letter of each word in a sentence.
str7 = 'i am invinsible'
print("Capitalize all words: ", str7.title())

#Extract username from email (before @).
str8 = 'example07@gmail.com'
print(str8.split('@')[0])

#Check if a string is a palindrome.
str9 = 'madam'
print("palindrome : ", str9 == str9[::-1])

#Join a list of words into a sentence.

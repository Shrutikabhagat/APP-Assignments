import re

with open("data.txt", "r") as file:
    text = file.read()

pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'

emails = re.findall(pattern, text)

print("Valid email addresses:")

for email in emails:
    print(email)
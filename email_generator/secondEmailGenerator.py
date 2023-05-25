"""
Exercises:
Create a file with list of randomly generated email addresses.
The email addresses must have domain name from the
given list of domains.
* Domain list is provided as variable 'list_of_domains'

HINT:
To generate random string with all lower case you can use this code
import random
import string
letters = string.ascii_lowercase
random_string = ''.join(random.choice(letters) for i in range(length))

V2:
- Create 100 total emails with domains randomly elected from the list. So the number of emails
for each domain will be unknown.
- Output a csv file with one email on each line and each line ending with a comma
- Output file name: out_generate_random_email_with_list_of_domains_v2.csv

** the difference from V1 is the domains are random for this one.
"""

# I will do it with my own way so some part you can see I didn't fallow the instructions

from faker import Faker
faker = Faker()
import random


list_of_domains = ['supersqa.com', 'gmail.com', 'yahoo.com', 'outlook.com', 'msn.com']

def generate_fake_email(domains):
    first_part = faker.user_name()
    domains = random.choice(list_of_domains)

    email = f"{first_part}@{domains}"
    return email

email_list = []

for i in range(100):
    fake_email = generate_fake_email(list_of_domains)
    email_list.append(fake_email)

with open("second_email_list.csv", "w") as file:
    for i in email_list:
        file.write(i + ",\n")




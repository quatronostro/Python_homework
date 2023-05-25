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

V1:
- Create 20 emails for each domain
- Output a txt file with one email on each line
"""

# I will do it with my own way so some part you can see I didn't fallow the instructions

import random
from faker import Faker

fake = Faker()

list_of_domains = ['supersqa.com', 'gmail.com', 'yahoo.com', 'outlook.com', 'msn.com']


def generate_fake_mail(domain):
    first_part = fake.user_name()
    domain = random.choice(domain)

    email = f"{first_part}@{domain}"
    return email

email_list = []

for i in range(20):
    fake_email = generate_fake_mail(list_of_domains)
    email_list.append(fake_email)

with open("email_list_file.txt", "w") as file:
    for i in email_list:
        file.write(i + "\n")


import random
from faker import Faker

fake = Faker()

main_list_of_domains = ['protonmail.com', 'gmail.com', 'yahoo.com', 'outlook.com', 'msn.com']

def generate_fake_mail(domain):
    first_part = fake.user_name()
    domain = random.choice(domain)

    email = f"{first_part}@{domain}"
    return email

email_list = []

for i in range(20):
    fake_email = generate_fake_mail(main_list_of_domains)
    email_list.append(fake_email)

with open("email_list_file.txt", "w") as file:
    for i in email_list:
        file.write(i + "\n")



# I will try later :(
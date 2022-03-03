from faker import Faker
fake = Faker(locale='en_CA')

advantage_shopping_cart_url = 'https://advantageonlineshopping.com/#/'

new_username = fake.user_name()
if len(new_username) > 15:
    user_name = new_username[5:14]
new_password = fake.password()
first_name = fake.first_name()
last_name = fake.last_name()
full_name = f'{first_name} {last_name}'
email = fake.email()
city = fake.city()
phone = fake.phone_number()
address = fake.address()
if len(address) > 50:
    address = address[5:49]
province = fake.province_abbr()
postal_code = fake.postalcode()

country = fake.country()
description = fake.sentence(nb_words=30)

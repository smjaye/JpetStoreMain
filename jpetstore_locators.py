import datetime

from faker import Faker
fake = Faker(locale='en_CA')





#-----------------------JpetStore  App Data parameters-------------------------

app = 'JpetStore '
jpet_store_url = 'https://petstore.octoperf.com/actions/Catalog.action'
jpet_store_homepage_title = 'JPetStore Demo'

userid = fake.user_name()[0:15]
password = fake.password()[0:4]
first_name = fake.first_name()
last_name = fake.last_name()
full_name = f'{first_name} {last_name}'
email = fake.email()
phone_number = fake.phone_number()
city = fake.city()
country = fake.current_country()
address1 = fake.street_address()
address2 = fake.street_address()
state = fake.province_abbr()
zip = fake.postcode()

itemid = ['EST-28', 'EST-22', 'EST-18', 'EST-21']
order_page = 'order_details'
shopping_cart = ['K9-RT-01', 'K9-RT-02']
import phonenumbers
from phonenumbers import geocoder


telefone = input('Digite um telefone no formato +5535999999999: ')

phone_number = phonenumbers.parse(telefone)

print(geocoder.description_for_number(phone_number, 'pt'))

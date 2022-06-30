import random
import string

first_name = ''.join(random.choices(string.ascii_letters + string.digits, k=11))
last_name = ''.join(random.choices(string.ascii_letters + string.digits, k=11))

PAYEE_DATA = {
    "address_street": "Darling Ave",
    "address_number": 123,
    "address_city": "Portland",
    "address_state": "ME",
    "address_zip_code": "04106",
    "address_country_code": "USA",
    "type": "Individual",
    "email": "<email@email.com>",
    "first_name": first_name,
    "last_name": last_name,
}

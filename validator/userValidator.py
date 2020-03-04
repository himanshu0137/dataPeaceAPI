from cerberus import Validator

schema = {
    "id": {'required': False},
    "first_name": {'type': 'string', 'required': True},
    "last_name": {'type': 'string', 'required': False},
    "company_name": {'type': 'string', 'required': True},
    "city": {'type': 'string', 'required': True},
    "state": {'type': 'string', 'required': True},
    "zip": {'type': 'integer', 'required': True},
    "email": {'type': 'string', 'required': True, 'regex': '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'},
    "web": {'type': 'string', 'required': True},
    "age": {'type': 'integer', 'required': True, 'min': 18, 'max': 99}
}

validator = Validator(schema)

def partialValidator(data):
    partialSchema = {}
    for key in data.keys():
        partialSchema[key] = schema[key]
    return Validator(partialSchema)
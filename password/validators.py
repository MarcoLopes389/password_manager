from .errors import ValidationError


def password_validator(body):
    try:
        body['owner']
    except:
        raise ValidationError("Please send owner")
    
    try:
        body['password']
    except:
        raise ValidationError("Please send password")
    
    try:
        body['expires']
    except:
        raise ValidationError("Please send expires")
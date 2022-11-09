from .errors import ValidationError


def password_validator(body):
    if not body['owner']:
        raise ValidationError("Please send owner")
    if not body['password']:
        raise ValidationError("Please send value")
    if not body['expires']:
        raise ValidationError("Please send expires")
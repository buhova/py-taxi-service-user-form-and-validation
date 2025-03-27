from django.core.exceptions import ValidationError

LEN_LICENSE_NUMBER = 8


def validate_driver_license(license_number):
    if len(license_number) != LEN_LICENSE_NUMBER:
        raise ValidationError("Invalid license number. "
                              "The length should be 8.")
    if not license_number[:3].isupper():
        raise ValidationError("Invalid license number. "
                              "The first 3 characters must be uppercase.")
    if not license_number[3:].isdigit():
        raise ValidationError("Invalid license number. "
                              "The last 5 characters must be numbers.")

    return license_number

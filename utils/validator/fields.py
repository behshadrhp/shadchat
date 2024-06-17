import os

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from validate_email_address import validate_email as validate


# personal information filed regex validator
username_regex = RegexValidator(
        regex=r"^[a-zA-Z0-9]+[_a-zA-Z0-9 ]{4,14}$",
        message="You must enter 10 digits, which is your national code.",
)
name_regex = RegexValidator(
        regex=r"^[a-zA-Z. ]{0,15}$",
        message="You must enter 10 digits, which is your national code.",
)
email_regex = RegexValidator(
    regex=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
    message="Your email is not valid."
)


# image size filed regex validator
def validate_file_size_volume(file):
    """This function is to validate the image file size."""
    max_size_kb = 5000

    size = (file.size / 1024) / 1024
    file_size = round(size, 2)

    if file.size > max_size_kb * 1024:
        raise ValidationError(
            code=406,
            detail=f"Your file size is greater than <5MB> allowed - Your file size <{file_size}MB>"
        )

def validate_image_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extension = [".jpg", ".jpeg", ".png"]
    if not ext.lower() in valid_extension:
        raise ValidationError(
            code=406,
            detail="Unsupported file extension"
        )

# email validation
def validate_email(email):

    if email:

        # email is valid or not
        email_is_valid = validate(email, verify=True, check_mx=True)

        if not email_is_valid:
            raise ValidationError(code=406, message="Your email is invalid, please enter valid email.")

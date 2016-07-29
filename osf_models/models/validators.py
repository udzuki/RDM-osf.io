from osf_models.exceptions import ValidationError

from osf_models.utils.base import strip_html


def validate_title(value):
    """Validator for Node#title. Makes sure that the value exists and is not
    above 200 characters.
    """
    if value is None or not value.strip():
        raise ValidationError('Title cannot be blank.')

    value = strip_html(value)

    if value is None or not value.strip():
        raise ValidationError('Invalid title.')

    if len(value) > 200:
        raise ValidationError('Title cannot exceed 200 characters.')

    return True

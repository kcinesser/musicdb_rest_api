from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_difficulty(value):
    if value < 0 or value >= 5:
        raise ValidationError(
            _('%(value)s must be between 0 and 5'),
            params={'value': value},
        )

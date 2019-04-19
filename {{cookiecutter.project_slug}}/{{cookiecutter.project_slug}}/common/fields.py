from django.db import models

from {{cookiecutter.project_slug}}.common.utils import normalize_persian_string


class NormalizedCharField(models.CharField):
    """Normalized CharField

    This field normalizes the value to get rid of
    unnecessary characters.

    Notes:
        - To be used when you expect the user
          could input some unwanted characters
          which might cause problems later like
          Persian character input in object titles.
    """
    def pre_save(self, model_instance, add):
        # first get the model's attribute
        attr_value = super(NormalizedCharField, self).pre_save(model_instance, add)
        # then apply the necessary normalizations
        return normalize_persian_string(attr_value)

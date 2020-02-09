from enum import Enum

from django.utils.translation import gettext_lazy as _

from django_countries import Countries
from djchoices import DjangoChoices, ChoiceItem


class EmailTemplate(Enum):
    VERIFICATION_EMAIL = ""


class AlgoliaIndex(Enum):
    PRODUCT = "products"


class Languages(DjangoChoices):
    ENGLISH = ChoiceItem("en", _("English"))
    GERMAN = ChoiceItem("de", _("German"))
    FRENCH = ChoiceItem("fr", _("French"))
    ITALIAN = ChoiceItem("it", _("Italian"))
    SPANISH = ChoiceItem("es", _("Spanish"))


class SEPACompatibleCountries(Countries):
    only = {
        "AT",
        "BE",
        "BG",
        "CY",
        "CZ",
        "DE",
        "DK",
        "EE",
        "ES",
        "FI",
        "FR",
        "GB",
        "GR",
        "HR",
        "HU",
        "IE",
        "IT",
        "LV",
        "LT",
        "LU",
        "MC",
        "MT",
        "NL",
        "PL",
        "PT",
        "RO",
        "SE",
        "SI",
        "SK",
        "SM",
    }


class EUEconomicZoneCountries(Countries):
    only = {
        "AT",
        "BE",
        "BG",
        "CY",
        "CZ",
        "DE",
        "DK",
        "EE",
        "ES",
        "FI",
        "FR",
        "GB",
        "GR",
        "HR",
        "HU",
        "IE",
        "IT",
        "LT",
        "LU",
        "LV",
        "MT",
        "NL",
        "PL",
        "PT",
        "RO",
        "SE",
        "SI",
        "SK",
    }

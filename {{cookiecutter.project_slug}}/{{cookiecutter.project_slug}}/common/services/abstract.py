import abc

from django.db.models import Manager

import attr

from {{ cookiecutter.project_slug }}.common.exceptions import BaseServiceError


class ServiceError(BaseServiceError):
    pass


class Service(abc.ABC, metaclass=abc.ABCMeta):
    """Abstract service

    This is an abstract service class which is
    used to hold units of business logic or custom
    code across the applications.
    """


@attr.s(auto_attribs=True)
class ModelService(Service):
    """Abstract model service

    This class is a base for all service classes
    which hold business logic in applications and
    work with data managers.

    This class has a `_manager` attribute which is
    a Django model manager for a single model which
    this service is designed to work with.

    All the storage operations should go through
    the attributed manager.

    Notes:
        - It is highly encouraged to define new functions
          in model custom model managers and use them
          in services instead of querying the database
          through the storage class (manager) freely!
        - It is highly discouraged to use other
          services' managers directly.
        - It is highly encouraged to receive or return
          only the main django object rather than
          other django objects that belong to other
          services.
    """

    _manager: Manager

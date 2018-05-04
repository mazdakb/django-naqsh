import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _


class UniversalModel(models.Model):
    id = models.UUIDField(_('universal unique id'), primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True

    @property
    def serial(self):
        return "{}{}".format(
            self.__class__.__name__.upper()[0],
            str(self.id).upper().split('-')[0]
        )

    def __str__(self):
        return self.serial


class TimestampedModel(models.Model):
    created = models.DateTimeField(_('created at'), auto_now_add=True)
    updated = models.DateTimeField(_('updated at'), auto_now=True)

    class Meta:
        abstract = True


class ActivatedModelManager(models.Manager):
    def get_queryset(self):
        return super(ActivatedModelManager, self).get_queryset().filter(is_active=True)


class ActivatedModel(models.Model):
    is_active = models.BooleanField(_('active'), default=True)

    objects = models.Manager()
    actives = ActivatedModelManager()

    class Meta:
        abstract = True

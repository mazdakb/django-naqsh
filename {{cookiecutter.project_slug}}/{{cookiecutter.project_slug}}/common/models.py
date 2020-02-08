import uuid

from django.db import models
from django.db.models import QuerySet
from django.utils.translation import ugettext_lazy as _

from {{cookiecutter.project_slug}}.common.utils import normalize_slug, generate_random_slug


class UniversalModel(models.Model):
    """Universal primary key mixin

    This mixin changes the primary key of a model to UUID field.
    Using UUID as primary key could help application scalability
    and could make migrating to micro-service, or exporting or importing data easier,
    by using a universally unique identifier for object that without fear of collision.
    """

    id = models.UUIDField(
        verbose_name=_("universal unique id"),
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    class Meta:
        abstract = True

    @property
    def serial(self) -> str:
        return f'{self.id.__str__().upper().split("-")[0]}'

    def __str__(self):
        return self.serial


class TimestampedModel(models.Model):
    """Timestamp mixin

    This mixin adds a timestamp to model for create and update events
    """

    created = models.DateTimeField(_("created at"), auto_now_add=True)
    updated = models.DateTimeField(_("updated at"), auto_now=True)

    class Meta:
        abstract = True


class ActivatedModelManager(models.Manager):
    @property
    def actives(self) -> QuerySet:
        return self.get_queryset().filter(is_active=True)


class ActivatedModel(models.Model):
    """Active objects mixin

    This mixin add a is_active field to the model
    which indicated the model active status.
    It also adds a queryset to support
    getting only active objects.
    """

    is_active = models.BooleanField(
        verbose_name=_("active"), default=True, db_index=True
    )

    objects = ActivatedModelManager()

    class Meta:
        abstract = True


class SluggedModel(models.Model):
    """Slugged mixin

    This mixin adds a unique alphanumeric slug field to model
    """

    slug = models.CharField(
        verbose_name=_("slug"),
        max_length=255,
        db_index=True,
        default=generate_random_slug,
        help_text=_("A unique slug that identifies this object by a string."),
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        # normalize the slug
        self.slug = normalize_slug(self.slug)
        # call super's save method
        super(SluggedModel, self).save(*args, **kwargs)

from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import (GenericForeignKey,
                                                GenericRelation)
from easy_thumbnails.fields import ThumbnailerImageField
from django.core.urlresolvers import reverse
from autoslug import AutoSlugField
from urlparse import urlsplit, urlunsplit
from markupfield.fields import MarkupField
from math import ceil
from decimal import Decimal, ROUND_CEILING

class Photo(models.Model):
    class Meta:
        ordering = ['-priority', '-edited']
    image = ThumbnailerImageField(upload_to='photos')
    caption = models.CharField(max_length=1024)
    priority = models.IntegerField(blank=True, default=0)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    content_type = models.ForeignKey(ContentType, related_name='+')
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __unicode__(self):
        return self.caption[:25] + ('...' if len(self.caption) > 25 else '')

    def get_absolute_url(self):
        try:
            return reverse('photo.detail', args=[str(self.content_object.builder.slug),
                                                    str(self.content_object.slug),
                                                    str(self.pk)])
        except Builder.DoesNotExist:
            return None

class BuilderManager(models.Manager):
    def get_queryset(self):
        qs = super(BuilderManager, self).get_queryset()

        # TODO: Calculate overall using F objects.
        #       Blocked on https://code.djangoproject.com/ticket/14030

        return qs.annotate(
            construction=models.Avg('reviews__construction'),
            communication=models.Avg('reviews__communication'),
            timeliness=models.Avg('reviews__timeliness')
        )

class Builder(models.Model):
    class Meta:
        ordering = ['name']

    STATUS_UNKNOWN = 'unknown'
    STATUS_CLOSED = 'closed'
    STATUS_QUOTES = 'quotes'
    STATUS_OPEN = 'open'

    STATUS_CHOICES = (
        (STATUS_UNKNOWN, 'Unknown'),
        (STATUS_CLOSED, 'Closed'),
        (STATUS_QUOTES, 'Quotes Only'),
        (STATUS_OPEN, 'Open'),
    )

    objects = BuilderManager()

    name = models.CharField(max_length=1024, unique=True)
    slug = AutoSlugField(populate_from='name', unique=True)
    status = models.CharField(max_length=16, choices=STATUS_CHOICES)
    users = models.ManyToManyField(User, related_name='builders',
                                    verbose_name='members')
    banner = ThumbnailerImageField(upload_to='banners')
    thumb = ThumbnailerImageField(upload_to='thumbs', verbose_name='thumbnail')
    description = MarkupField(blank=True,  markup_type='markdown',
                                escape_html=True)

    @property
    def overall(self):
        return (self.construction + self.communication + self.timeliness) / 3.0

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('builder.detail', args=[str(self.slug)])

    def can_edit(self, user):
        return self.users.filter(pk=user.pk).exists()

class Website(models.Model):
    class Meta:
        unique_together = (('url', 'builder'),)

    url = models.URLField(max_length=2048)
    builder = models.ForeignKey(Builder, related_name='other_sites')

    @property
    def human_url(self):
        # TODO: Improve this
        parts = list(urlsplit(self.url))
        parts[2] = self._shorten(parts[2], 10)
        if parts[1].startswith('www.'):
            parts[1] = parts[1][4:]
        return ''.join([parts[1], parts[2]])

    @property
    def short_url(self):
        return self._shorten(self.url)

    def _shorten(self, url, length=47):
        if len(url) > length:
            url = url[:length//2] + '...' + url[length//-2:]
        return url

    def __unicode__(self):
        return self.builder.name + ': ' + self.short_url

class Review(models.Model):
    class Meta:
        ordering = ['-edited']
    user = models.ForeignKey(User, related_name='reviews')
    builder = models.ForeignKey(Builder, related_name='reviews')

    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    costume_name = models.CharField(max_length=1024)
    slug = AutoSlugField(populate_from='costume_name', unique_with=['builder'])
    text = MarkupField(escape_html=True, markup_type='markdown')
    commission_date = models.DateField()
    received_date = models.DateField(blank=True, null=True)

    photos = GenericRelation(Photo, related_query_name='reviews')

    construction = models.DecimalField(max_digits=2, decimal_places=1)
    communication = models.DecimalField(max_digits=2, decimal_places=1)
    timeliness = models.DecimalField(max_digits=2, decimal_places=1)

    @property
    def overall(self):
        avg = Decimal(self.construction)
        avg += Decimal(self.communication)
        avg += Decimal(self.timeliness)
        avg /= Decimal('3.0')
        return avg

    def __unicode__(self):
        return unicode(self.builder) + ' (' + self.costume_name + ')'

    def get_absolute_url(self):
        try:
            return reverse('review.detail', args=[str(self.builder.slug),
                                                    str(self.slug)])
        except Builder.DoesNotExist:
            return None

    def can_edit(self, user):
        return user.pk == self.user.pk

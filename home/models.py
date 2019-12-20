from django.db import models
from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel, StreamFieldPanel
from wagtail.core import blocks
from wagtail.core.fields import StreamField

from wagtail.core.models import Page
from wagtail.search import index


class HomePage(Page):
    pass


CONTENT_STREAMFIELD_ELEMENTS = [
    ('title', blocks.CharBlock()),
    ('paragraph', blocks.RichTextBlock()),
]


class NewsPage(Page):
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    body = StreamField(CONTENT_STREAMFIELD_ELEMENTS, blank=True, null=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateField(verbose_name="Display date", blank=True, null=True)
    is_sticky = models.BooleanField(default=False)
    is_on_index = models.BooleanField(default=False)

    search_fields = Page.search_fields + [  # Inherit search_fields from Page
        index.SearchField('subtitle'),
        index.SearchField('body'),
        index.SearchField('tags'),
        index.SearchField('author'),
        index.SearchField('is_sticky'),
        index.SearchField('date'),
        index.SearchField('url_path'),
        index.FilterField('is_sticky'),
        index.FilterField('date'),
        index.FilterField('title'),
        index.FilterField('url_path')
    ]

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        StreamFieldPanel('body'),
        FieldPanel('author'),
        FieldPanel('date'),
        FieldPanel('is_sticky'),
        FieldPanel('is_on_index')
    ]



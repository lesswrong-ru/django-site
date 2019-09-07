from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

class BookPage(Page):
    body = RichTextField(blank=True)

    author = models.CharField(max_length=100, blank=True)
    translators = models.CharField(max_length=100, blank=True)
    original_link = models.CharField(max_length=100, blank=True)
    rfatz_id = models.PositiveSmallIntegerField(null=True, blank=True)
    on_vk = models.BooleanField(default=False)
    readthesequences_link = models.CharField(max_length=100, blank=True)

    # illustrations
    # ref_audio

    # FIXME - copy-paste from TranslationIndexPage
    def children(self):
        return Page.objects.child_of(self).live()

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        FieldPanel('author'),
        FieldPanel('translators'),
        FieldPanel('original_link'),
        FieldPanel('rfatz_id'),
        FieldPanel('on_vk'),
        FieldPanel('readthesequences_link'),
    ]
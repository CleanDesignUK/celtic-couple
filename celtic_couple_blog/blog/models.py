# blog/models.py

from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel,
)
from wagtail.fields import RichTextField
from wagtail.images.models import Image
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey
from wagtail.models import Orderable  # Import Orderable

@register_snippet
class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = RichTextField(blank=True, null=True)
    photo = models.ForeignKey(
        Image,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('bio'),
        FieldPanel('photo'),
    ]

    def __str__(self):
        return self.name


class BlogPageGalleryImage(Orderable):  # Inherit from Orderable
    page = ParentalKey('BlogPage', on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        Image,
        on_delete=models.CASCADE,
        related_name='+'
    )
    caption = models.CharField(max_length=250, blank=True)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]

    class Meta:
        ordering = ['sort_order']  # Ensure ordering by sort_order
        verbose_name = "Gallery Image"
        verbose_name_plural = "Gallery Images"


class BlogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250, blank=True, null=True)  # **New Subtitle Field**
    body = RichTextField(blank=True)
    author = models.ForeignKey(
        'blog.Author',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    tags = models.CharField(max_length=250, blank=True)  # Consider using taggit for better tagging

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('author'),
        ], heading="Blog Details"),
        FieldPanel('intro'),
        FieldPanel('subtitle'),  # **Add Subtitle to Content Panels**
        FieldPanel('body', classname="full"),
        FieldPanel('tags'),
        InlinePanel('gallery_images', label="Gallery Images"),
    ]

    def __str__(self):
        return self.title


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
    ]

    subpage_types = ['blog.BlogPage']
    parent_page_types = ['home.HomePage']  # Adjust according to your project structure

    def get_context(self, request):
        # Get all live BlogPage objects, ordered by date descending
        context = super().get_context(request)
        blogpages = BlogPage.objects.live().order_by('-date')
        context['posts'] = blogpages
        return context

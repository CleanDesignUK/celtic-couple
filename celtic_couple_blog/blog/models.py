from django.db import models
from wagtail.models import Page  # Updated import
from wagtail.admin.panels import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel,
)  # Updated import for panels
from wagtail.fields import RichTextField  # Updated import
from wagtail.images.models import Image
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey


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
        FieldPanel('photo'),  # Updated for Wagtail 3.0+
    ]

    def __str__(self):
        return self.name


class BlogPageGalleryImage(models.Model):
    page = ParentalKey('BlogPage', on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        Image,
        on_delete=models.CASCADE,
        related_name='+'
    )
    caption = models.CharField(max_length=250, blank=True)

    panels = [
        FieldPanel('image'),  # Updated for Wagtail 3.0+
        FieldPanel('caption'),
    ]

    class Meta:
        verbose_name = "Gallery Image"
        verbose_name_plural = "Gallery Images"


class BlogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
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

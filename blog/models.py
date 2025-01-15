from django.db import models
from wagtail.models import Page, Orderable
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.fields import RichTextField
from wagtail.images.models import Image
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey


@register_snippet
class Author(models.Model):
    """Snippet to represent blog authors."""
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


class BlogPageGalleryImage(Orderable):
    """Allows for adding gallery images to a blog page."""
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
        ordering = ['sort_order']
        verbose_name = "Gallery Image"
        verbose_name_plural = "Gallery Images"


class BlogPage(Page):
    """Model for individual blog posts."""
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250, blank=True, null=True)
    body = RichTextField(blank=True)
    author = models.ForeignKey(
        'blog.Author',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    tags = models.CharField(max_length=250, blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('author'),
        ], heading="Blog Details"),
        FieldPanel('intro'),
        FieldPanel('subtitle'),
        FieldPanel('body', classname="full"),
        FieldPanel('tags'),
        InlinePanel('gallery_images', label="Gallery Images"),
    ]

    def __str__(self):
        return self.title


class BlogIndexPage(Page):
    """Model for the blog index page."""
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
    ]

    subpage_types = ['blog.BlogPage']


    def get_context(self, request):
        """Custom context to fetch blog pages."""
        context = super().get_context(request)
        blogpages = BlogPage.objects.live().order_by('-date')
        context['posts'] = blogpages
        return context

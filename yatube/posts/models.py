from django.contrib.auth import get_user_model
from django.db import models

MAX_CHAR_FIELD_SIZE = 200

User = get_user_model()


class Group(models.Model):
    """
    Model for storing groups.

    Fields:
        title (CharField): the name of the group.
        slug (SlugField): the unique address of the group, part of the URL.
        description (TextField): a text describing the community.
            This text will be displayed on the community page.
    """
    title = models.CharField(
        max_length=MAX_CHAR_FIELD_SIZE,
        verbose_name='Community name',
    )
    slug = models.SlugField(unique=True, verbose_name='Unique address')
    description = models.TextField(verbose_name='Community description')

    class Meta:
        verbose_name_plural = 'List of groups'

    def __str__(self):
        return self.title


class Post(models.Model):
    """
    Model for storing posts.

    Fields:
        text (TextField): the text of the post.
        pub_date (DateTimeField): date of publication of the post.
        author (ForeignKey): indicates the author of the post.
        group (ForeignKey): indicates the group of the post.
    """
    text = models.TextField(verbose_name='The content of the post')
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Date of publication',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='posts',
        verbose_name='community',
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name_plural = 'List of posts'

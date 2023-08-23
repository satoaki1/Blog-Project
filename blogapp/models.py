from django.db import models


# Create your models here.
class BlogPost(models.Model):
    CATEGORY = (('technology', 'ITのこと'),
                ('dailylife', '日常のこと'),
                ('music', '音楽のこと'),
                ('portfolio', '自作製品のこと'))

    title = models.CharField(
        verbose_name='Title',
        max_length=200
    )

    content = models.TextField(
        verbose_name='Content'
    )

    posted_at = models.DateTimeField(
        verbose_name='Posted Date and Time',
        auto_now_add=True
    )

    category = models.CharField(
        verbose_name='Category',
        max_length=50,
        choices=CATEGORY
    )

    def __str__(self):
        return self.title

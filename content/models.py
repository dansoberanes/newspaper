from django.db import models
from tinymce import models as tinymce_models


class Content(models.Model):
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500)
    contributors = models.ManyToManyField('Contributor',
                                          related_name='content')
    pub_date = models.DateTimeField('date published')

class Article(Content):
    title = Content().title
    subtitle = Content().subtitle
    contributors = Content.contributors
    pub_date = Content().pub_date

    text = tinymce_models.HTMLField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)


class Contributor(models.Model):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    position = models.CharField(max_length=500)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        ordering = ('first_name', 'last_name')

    def die(self):
        self.models.delete()
        
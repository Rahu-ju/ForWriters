from django.db import models
from django.conf import settings
from django.urls import reverse


# Create your models here.
class Article(models.Model):
    '''Modelling the article section.'''
    title = models.CharField(max_length=200)
    body = models.TextField()
    author  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''Return string representation of the model.'''
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])


class Comment(models.Model):
    '''Modelling the comment section.'''
    article = models.ForeignKey(
        Article,
        on_delete = models.CASCADE,
        related_name = 'comments',

     )
    comment = models.CharField(max_length=150)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        '''String representation of the model. '''
        return self.comment

    # def get_absolute_url(self):
    #     return reverse('article_detail', args=[str(self.id)])




class Reply(models.Model):
    ''' Modelling the reply section. '''
    comment = models.ForeignKey(
        Comment,
        on_delete = models.CASCADE,
        related_name = 'replys'
    )
    reply = models.CharField(max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        ''' String representation of the model. '''
        return self.reply

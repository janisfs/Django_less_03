from django.db import models

# Create your models here.
class News_post(models.Model):
    title = models.CharField('Название', max_length=100)
    short_description = models.CharField('Краткое описание', max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
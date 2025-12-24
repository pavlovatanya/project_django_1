from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField('Название')
    anons = models.CharField('Анонс')
    full_text = models.TextField('Статья')

    def __str__(self):
        return self.title
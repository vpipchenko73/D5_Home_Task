from django.db import models

# Create your models here.

class Post(models.Model):
    dateCreation = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=128)
    text = models.TextField()
    autor = models.ForeignKey('Autor', on_delete=models.CASCADE)
    rating = models.SmallIntegerField(default=0)
    #class Meta:
     #   ordering=['-dateCreation']

    def __str__(self):
        return f"{self.title[0:16]} / {self.text[0:128]}{'...'} Автор- {str(self.autor)}"

    def get_absolute_url(self):
        #return f'/newsall/{self.id}'
        return f'/newsall/'


class Autor(models.Model):
    name = models.CharField(max_length=32, default="Нет автора")

    def __str__(self):
        return f'{self.name}'
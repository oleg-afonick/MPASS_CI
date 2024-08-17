from django.db import models


class PassUser(models.Model):
    lastname = models.CharField(max_length=25, verbose_name='Фамилия')
    firstname = models.CharField(max_length=25, verbose_name='Имя')
    surname = models.CharField(max_length=25, verbose_name='Отчество')
    phone = models.CharField(max_length=15, verbose_name='Телефон')
    email = models.EmailField(max_length=100, verbose_name='E-mail')

    def __str__(self):
        return str(self.pk)

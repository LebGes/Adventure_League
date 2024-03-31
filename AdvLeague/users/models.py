from django.db import models

class User(models.Model):
    LastName = models.CharField('Фамилия', max_length=50)
    FirstName = models.CharField('Имя', max_length=50)
    Patronymic = models.CharField('Отчество', max_length=50)
    BirthDate = models.DateField('Дата рождения')
    RegisterDate = models.DateField('Дата регистрации')
    PhoneNumber = models.CharField('Номер телефона', max_length=12)
    Email = models.EmailField('Адрес электронной почты')
    Password = models.CharField('Пароль', max_length=30)

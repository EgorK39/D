from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class UserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, db_column='Пользователь')

    def __str__(self):
        return f'{self.user}'


class PostModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=188, db_column='Заголовок')
    text = models.TextField(db_column='Текст')
    photo = models.ImageField(upload_to='image', null=True, blank=True, db_column='Фото', default='image/default.jpg')
    file = models.FileField(upload_to='video', null=True, blank=True, db_column='Видео/контент')
    time_in = models.DateTimeField(auto_now_add=True)
    # PA = 'Танки'
    # HP = 'Хилы'
    # DD = 'ДД'
    # TO = 'Торговцы'
    # GI = 'Гилдмастера'
    # KV = 'Квестгиверы'
    # KU = 'Кузнецы'
    # KO = 'Кожевники'
    # ZE = 'Зельевары'
    # MA = 'Мастера заклинаний'
    CHOICE = (
        ('PA', 'Танки'),
        ('HP', 'Хилы'),
        ('DD', 'ДД'),
        ('TO', 'Торговцы'),
        ('GI', 'Гилдмастера'),
        ('KV', 'Квестгиверы'),
        ('KU', 'Кузнецы'),
        ('KO', 'Кожевники'),
        ('ZE', 'Зельевары'),
        ('MA', 'Мастера заклинаний'),
    )
    category = models.CharField(max_length=2, choices=CHOICE)

    def get_absolute_url(self):
        return reverse('posts:post', args=[str(self.id)])

    def __str__(self):
        return f'{self.title} {self.text}'


class Comment(models.Model):
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(db_column='Текст')
    time_in = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.text}'

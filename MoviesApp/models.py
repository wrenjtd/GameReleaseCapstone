from django.db import models

class GamePlatform(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length = 500)
    developer = models.CharField(max_length = 200)
    publisher = models.CharField(max_length = 200)
    platforms = models.ManyToManyField(GamePlatform)
    release_date = models.DateField()
    cover_art_url = models.CharField(max_length = 500)
    igdb_id = models.CharField(max_length = 8)
    on_wishlist = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Member(models.Model):
    username = models.CharField(max_length = 40)
    m_email = models.EmailField()
    m_birthday = models.DateField('birthday')
    password = models.CharField(max_length=20)
# Create your models here.




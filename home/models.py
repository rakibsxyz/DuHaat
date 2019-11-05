from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models

class Album(models.Model):
    artist = models.CharField(max_length=250)
    albumTitle = models.CharField(max_length=550)
    genre = models.CharField(max_length=150)
    albumLogo = models.CharField(max_length=10000)

    def __str__(self):
        return self.albumTitle +" - "+ self.artist



class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    fileType = models.CharField(max_length=20)
    songTitle = models.CharField(max_length=250)

class Hoodies(models.Model):
    productType = models.CharField(max_length=250)
    productId = models.CharField(max_length=20)
    productPrice = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.productType +" - "+ self.productId


# python manage.py makemigrations music
# python manage.py sqlmigrate music 0001
#python manage.py migrate

#python manage.py shell
#  from music.models import Album, Song
# >>> Album.objects.all()
# <QuerySet []>
# >>> a= Album()
# >>> a.artist = "Rakib"
# >>> a.album_title = "Nai"
# >>> a.genre = "nai"
# >>> a.albumLogo = "nai"
# >>> a.save()
# >>> a
# from music.models import Album, Song
# >>> Album.objects.all()
# <QuerySet [<Album:  - Rakib>]>
# >>> Album.objects.filter(id=1)
# <QuerySet [<Album:  - Rakib>]>
# >>>

from django.db import models
from pytils.translit import slugify

class Genre(models.Model):
    name = models.CharField("Name", max_length=255)
    slug = models.SlugField(unique=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Film(models.Model):
    name = models.CharField("Название", max_length=255)
    director = models.CharField("Директор", max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name="Жанр")
    rating = models.FloatField("Рейтинг")
    description = models.TextField("Описание")
    url_poster = models.CharField("URL постера", max_length=500)
    url_banner = models.CharField("URL баннера", max_length=500)
    url_film = models.CharField("URL на сам фильм", max_length=500)
    is_top_ten = models.BooleanField("Is top 10", null=True, blank=True)

    def __str__(self):
        return self.name
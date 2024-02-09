from django.db import models

# Create your models here.

# class is a table in our DB
# Profiles -> Links
class Profile(models.Model):
    # tuple is ordered, unchangable, allow duplicates
    BG_CHOICES = (
        ('blue', 'Blue'), # stored value , displayed valued
        ('orange', 'Orange'),
        ('purple', 'Purple'),
        ('green', 'Green'),
        ('black', 'Black'),

    )
    # name, slug, bg_color
    name = models.CharField(max_length = 50)
    slug = models.SlugField(max_length = 100)
    bg_color = models.CharField(max_length =50, choices = BG_CHOICES)

    # access the links via related_name
    # profile.mylinks

    def __str__(self):
        return self.name.upper()


class MyLink(models.Model):
    # text , url, profile associated

    text = models.CharField(max_length =100)
    url = models.URLField(max_length = 100)
    # many to one relationship
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name="mylinks")

    def __str__(self):
        return f"{self.text.upper()} | {self.url}"
    
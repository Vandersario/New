from django.db import models
from django.conf import settings
from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone



class News(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Vacans(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=200) # Полное описание
    text = models.CharField(max_length=50)  # краткое описание
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.title    


class Cveti(models.Model):
    photo=models.ImageField()
    text = models.CharField(max_length=50) #Краткое описание
    text = models.CharField(max_length=200) # Полное описание
    cena= models.IntegerField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class Corzina(models.Model):
    zakaz= models.IntegerField()
    text=models.TextField()
    cena= models.IntegerField()
    kolvo=models.IntegerField()
    fullprice=models.IntegerField()
    comment=models.CharField(max_length=300) # Пожелаение к заказу

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class Comments(models.Model): # коментарий к продукции
    post = models.ForeignKey(Cveti, related_name='comments',on_delete=CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)


# Create your models here.

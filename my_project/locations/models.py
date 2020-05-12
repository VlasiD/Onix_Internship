from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save, pre_delete, post_delete


class Symbol(models.Model):
    """Response for creating Symbol table"""
    image = models.ImageField()

    def __str__(self):
        return self.image.name


class Country(models.Model):
    """Response for creating County table"""
    class Meta:
        """"Gets plural name for table"""
        verbose_name_plural = 'Countries'

    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    population = models.IntegerField(default=0)
    cities_count = models.IntegerField(default=0)
    # create connection to Symbol table
    flag = models.OneToOneField(Symbol, on_delete=models.CASCADE)
    user = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.name


class City(models.Model):
    """Response for creating City table"""
    class Meta:
        """"Gets plural name for table"""
        verbose_name_plural = 'Cities'

    name = models.CharField(max_length=100)
    # create connection to Country table
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return self.name


@receiver(pre_save, sender=City)
def city_creating_print(instance, **kwargs):
    print("City {} will be added to the table".format(instance.name))


@receiver(post_save, sender=City)
def count_increase(instance, **kwargs):
    instance.country.cities_count += 1
    instance.country.save()
    print(instance.country.cities_count)


@receiver(pre_delete, sender=City)
def count_decrease(instance, **kwargs):
    instance.country.cities_count -= 1
    instance.country.save()


@receiver(post_delete, sender=City)
def city_deleting_print(instance, **kwargs):
    print("City {} deleted from the table".format(instance.name))

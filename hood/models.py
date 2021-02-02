from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Neighbourhood(models.Model):
    hood_name = models.CharField(max_length=60)
    location = models.CharField(max_length=60)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    hood_image = models.ImageField(upload_to='images/')
    description = models.TextField(default='')
    health_tell = models.IntegerField(null=True, blank=True)
    police_number = models.IntegerField(null=True, blank=True)

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def search_by_location(cls, search_term):
        certain_user=cls.objects.filter(location__icontains=search_term)
        return certain_user
    
    def __str__(self):
        return self.location


class Profile(models.Model):
    profile_image = models.ImageField(upload_to='profile_pic/', null=True)
    bio = models.CharField(max_length=300)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    neighbourhoods = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, null=True)

    @classmethod
    def get_profile(cls):
        all_profiles = cls.objects.all()
        return all_profiles

    def save_profles(self):
        self.save()

    def delete_profiles(self):
        self.delete()

    def __str__(self):
        return str(self.user)


class Business(models.Model):
    business_name = models.CharField(max_length=60)
    description = models.CharField(max_length=200) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    email = models.EmailField()
    

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()


class Post(models.Model):
    post = models.CharField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
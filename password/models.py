from django.db import models

class User(models.Model):
    class Meta:
        db_table = 'user'
    
    wordpass: str = models.CharField(max_length=100)
    email: str = models.CharField(max_length=100)
    phone: str = models.CharField(max_length=100)
    name: str = models.CharField(max_length=100)
    nick: str = models.CharField(max_length=20)

class Password(models.Model):
    class Meta:
        db_table = 'password'
    
    value = models.CharField(max_length=100)
    expires = models.BooleanField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

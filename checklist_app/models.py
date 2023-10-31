from django.db import models
from django.contrib.auth.models import User


class List(models.Model):

    title = models.CharField(max_length=200)
    owners = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner_list')
    users = models.ManyToManyField(User, related_name='shared_list')

    def __str__(self) -> str:
        return self.title
    
    def add_user_to_list(self, user):

        self.users.add(user)        

    def remove_user_from_list(self, user):

        self.users.remove(user)


class ListItem(models.Model):

    checklist = models.ForeignKey(List, on_delete=models.CASCADE, related_name='item')
    title = models.CharField(max_length=200)
    status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
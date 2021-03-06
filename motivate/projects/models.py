from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Sum 

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    categories = models.JSONField (default=list)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField()
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owner_projects'
    )
    
    def pledge_total(self):
        sum = Pledge.objects.filter(project=self.id).aggregate(Sum('amount'))['amount__sum']
        return sum

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
    )
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='supporter_pledges'
    )
    
class TimeDonation(models.Model):
    time = models.IntegerField()
    comment = models.CharField(max_length=200)
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE
    )
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    date_started = models.DateTimeField()
    date_finished = models.DateTimeField()
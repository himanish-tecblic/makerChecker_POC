from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    
    def __str__(self):
        return self.name
    
    
class Agreement(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='agreements')
    
    def __str__(self):
        return self.title

class Review(models.Model):
    agreement = models.ForeignKey(Agreement, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    feedback = models.TextField()
    
    # def __str__(self):
    #     return self.reviewer
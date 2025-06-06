from django.db import models


class Record(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    
    def __str__(self):
        return(f'{self.last_name} {self.first_name}')
    
class Reviews(models.Model):
    user_id = models.ForeignKey(Record, on_delete = models.CASCADE)
    review = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return(f'{self.review}')
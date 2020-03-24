from django.db import models

# Create your models here.
class JobOffer(models.Model):
    company_email=models.EmailField()
    company_name = models.CharField(max_length=120)
    job_title = models.CharField(max_length=120)
    job_description = models.CharField(max_length=200)
    salary = models.IntegerField()
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{ self.job_title } by { self.company_name }"




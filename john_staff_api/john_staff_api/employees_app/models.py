from django.db import models

# Create your models here.
class employees(models . Model):
    objects=models.Manager()
    name=models.CharField(max_length=78)
    email=models.EmailField()
    p_number=models.CharField(max_length= 78)
    location=models.CharField(max_length=1000)


class StaffBase(models.Model):
    objects=models.Manager()
    f_name=models.CharField(max_length=87)
    l_name=models.CharField(max_length=87)
    email=models.EmailField()
    p_number=models.CharField(max_length=78)

class manager(models.Model):
    objects=models.Manager()
    applicant=models.ForeignKey(Applicant, on_delete=models.CASCADE)
    skills=models.CharField(max_length=1500)
    experience=models.CharField(max_length=5000)
    certification=models.TextField(blank=True, null=True)


class intern(models . Model):
    objects=models.Manager()
    name=models.CharField(max_length=78)
    email=models.EmailField()
    p_number=models.CharField(max_length= 78)
    location=models.CharField(max_length=1000)



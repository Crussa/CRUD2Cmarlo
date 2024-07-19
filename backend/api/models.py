from django.db import models

class Item(models.Model):
    first_name = models.CharField(max_length=100, default='')
    middle_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    address = models.CharField(max_length=200, default='')
    zip_code = models.CharField(max_length=10, default='')
    email = models.EmailField(default='')
    phone = models.CharField(max_length=15, default='')
    place_of_birth = models.CharField(max_length=100, default='')
    date_of_birth = models.DateField(default='')
    sex = models.CharField(max_length=10, default='')
    civil_status = models.CharField(max_length=50, default='')
    citizenship = models.CharField(max_length=50, default='')
    height = models.PositiveIntegerField(default=0)
    weight = models.PositiveIntegerField(default=0)
    blood_type = models.CharField(max_length=3, default='')
    occupation = models.CharField(max_length=100, default='')
    mother_first_name = models.CharField(max_length=100, default='')
    mother_middle_name = models.CharField(max_length=100, default='')
    mother_last_name = models.CharField(max_length=100, default='')
    father_first_name = models.CharField(max_length=100, default='')
    father_middle_name = models.CharField(max_length=100, default='')
    father_last_name = models.CharField(max_length=100, default='')
    sss_number = models.CharField(max_length=100, default='')
    pagibig_id_number = models.CharField(max_length=100, default='')
    tin_number = models.CharField(max_length=100, default='')
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.middle_name} {self.last_name}"

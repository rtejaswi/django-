from django.db import models

# Create your models here.
class School(models.Model):
    student_name = models.CharField(max_length = 30)
    student_class = models.CharField(max_length = 2)
    student_section = models.CharField(max_length = 1)
    student_roll_no = models.CharField(max_length = 5, unique = True)
    marks_obtained_in_percent = models.DecimalField(max_digits=5, decimal_places=3)
#username : tiger
#password : tiger123

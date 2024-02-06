from django.db import models

# Create your models here.
class Dept(models.Model):
     dept_no= models.IntegerField(primary_key=True)
     dname = models.CharField(max_length=100)
     location = models.CharField(max_length=100)

     def __str__(self) :
          return self.dname 
     
class Emp(models.Model):
    dept_no = models.ForeignKey(Dept ,on_delete=models.CASCADE)
    emp_no = models.IntegerField()
    emp_name = models.CharField(max_length=100)
    

    def __str__(self):
         return self.emp_name
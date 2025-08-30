from django.db import models

# Create your models here.
class Teacherstatus(models.TextChoices):
    PENDING="PENDING"
    APPROVED="APPROVED"
    DELETED="DELETED"


class Genderchoice(models.TextChoices):
    MALE="MALE"
    FEMALE="FEMALE"
    OTHER="OTHER"

class TeacherModel(models.Model):
    phone_number=models.CharField(max_length=11, unique=True)
    full_name=models.CharField(max_length=60)
    profile_picture=models.CharField(max_length=255)
    website =models.CharField(max_length=300, null=True,blank=True)
    status=models.CharField(max_length=15,choices=Teacherstatus.choices, default=Teacherstatus.PENDING)
    gender=models.CharField(max_length=10,choices=Genderchoice.choices, default=Genderchoice.MALE)
    password=models.CharField(max_length=300)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
       # return self.phone_number   for single attribute show in display
         return f"full_name={self.full_name} || phone_number={self.phone_number}"  #for multiple attribute show in display
    class Meta:
        verbose_name="Teacher"
        verbose_name_plural="Teachers"
        db_table="teacher"
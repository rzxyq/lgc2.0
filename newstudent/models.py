from django.db import models

class NewStudent(models.Model):
    name = models.CharField(max_length=35)
    netid = models.CharField(max_length=10)
    # hometown = models.CharField(max_length=35)
    year = models.CharField(max_length=20)
    college = models.CharField(max_length=50)
    major = models.CharField(max_length=200)
    minor = models.TextField()
    extracurricular = models.TextField()
    extra_sa = models.TextField(max_length=638,null=True)
    career = models.TextField()
    career_sa = models.TextField(max_length=638,null=True)
    sa1 = models.TextField(max_length=638,null=True)
    sa2 = models.TextField(max_length=638,null=True)
    sa3 = models.TextField(max_length=638,null=True)
    survey = models.TextField()
    partnering = models.TextField() 
    selected = models.BooleanField(default=False)
    upperclassman = models.ForeignKey('upperclassman.Upperclassman', null=True)

    def __str__(self):
        return self.name

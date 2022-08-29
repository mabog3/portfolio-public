from django.db import models

# see https://docs.djangoproject.com/en/4.1/ref/models/fields/#model-field-types for model field info and definitions 

class genericRole(models.Model):
    
    title = models.CharField(max_length=50)
    summary = models.TextField() # charfield a char input field 200 in letters 
    skills = models.ManyToManyField('Skill')
    startDate = models.DateField()
    endDate = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title 

    class Meta:
        abstract = True

class Job(genericRole): # class inherits models.Model
    jobTitle = models.CharField(max_length=50)
    company = models.CharField(max_length=50)

    def summary_as_list(self):
        return [x.strip() for x in self.summary.split('|')]

class Project(genericRole): 
    host = models.ManyToManyField('Host', blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    bullets = models.TextField()

    def bullets_as_list(self): 
        return [x.strip() for x in self.bullets.split('|')]

class Club(genericRole):
    jobTitle = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    clubLink = models.TextField(blank=True, null=True)
    def summary_as_list(self):
        return [x.strip() for x in self.summary.split('|')]

class Skill(models.Model):
    skillName = models.CharField(max_length=30)
    def __str__(self):
        return self.skillName 

class Host(models.Model):
    title = models.CharField(max_length=50)
    hostText = models.CharField(max_length=50, blank=True, null=True)
    hostLink = models.CharField(max_length=300, blank=True, null=True)
    def __str__(self):
        return self.title 
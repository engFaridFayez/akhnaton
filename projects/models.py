from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=100)
    titleImage = models.ImageField(upload_to='project_images/', default='coming.jpg')
    category = models.ForeignKey('Category', related_name='projects', on_delete=models.SET_NULL, null=True, blank=True)
    location = models.CharField(max_length=100,default="Giza")
    execution_period=models.CharField(max_length=100,default="Giza")
    client = models.CharField(max_length=100,default="HydePark")
    equipments =models.IntegerField(default=10)
    workers =models.IntegerField(default=10)
    engineers =models.IntegerField(default=10)
    info = models.CharField(max_length=500,default="Lorem ipsum")
    million = models.IntegerField(default=2)


    def __str__(self):
        return self.name
    

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images/', default='noProject.jpg')

    def __str__(self):
        return f"Image for {self.project.name}"
    
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
        class Meta:
            ordering = ['name']

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    send_copy = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.email}"

class EmploymentMessage(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    age = models.IntegerField()
    place_of_residence = models.CharField(max_length=200)
    job_applied_for = models.CharField(max_length=50)
    numbers_of_years_experience = models.IntegerField()
    message = models.TextField()
    cv = models.FileField(upload_to='cvs/')

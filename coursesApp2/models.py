from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def create_validator(self, postData):
        errors = {}
        if len(postData['course_name']) < 6:
            errors['name'] = "Course name is too short"
        if len(postData['description']) < 16:
            errors['desc'] = "Description is too short"
        return errors

class Course(models.Model):
    name = models.TextField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

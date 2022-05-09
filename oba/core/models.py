from django.db import models

# Create your models here
def upload_path(instance, filename):
    ext = filename.split('.')[-1]
    return '{0}/{1}.{2}'.format(instance.user.id, filename, ext)

# File and correspondng data
class File(models.Model):
    # file
    file = models.FileField(upload_to=upload_path)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
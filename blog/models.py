from django.db import models
from django.utils import timezone

class Post(models.Model):
    author=models.ForeignKey('auth.User')
    title=models.CharField(max_length=200)
    text=models.TextField()
    created_date=models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(blank=True, null=True)

    def publish(self):
        '''
        This method is use to Auto-Fill the published_date field
        of the Post class i.e our model
        '''
        self.published_date=timezone.now()
        self.save()

    def save(self,*args, **kwargs):
        #self.publish()
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

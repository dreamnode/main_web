from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class our_work(models.Model):
    title = models.CharField(max_length=100)
    brief = models.CharField(max_length=100)
    content = models.TextField()
    img_works = models.ImageField(default='default.jpg', upload_to='pictures')
    thumb_img = models.ImageField(default='default_thumb.jpg', upload_to='pictures')
    client = models.CharField(max_length=50)
    category = models.CharField(max_length=100)
    date = models.CharField(max_length=40)

    def __str__(self):
        return self.title


class branding(models.Model):
    title = models.CharField(max_length=100)
    brief = models.CharField(max_length=100)
    content = models.TextField()
    img_works = models.ImageField(default='default.jpg', upload_to='pictures')
    thumb_img = models.ImageField(default='default_thumb.jpg', upload_to='pictures')
    client = models.CharField(max_length=50)
    category = models.CharField(max_length=100)
    date = models.CharField(max_length=40)

    def __str__(self):
        return self.title

class ads(models.Model):
    title = models.CharField(max_length=100)
    brief = models.CharField(max_length=100)
    content = models.TextField()
    img_works = models.ImageField(default='default.jpg', upload_to='pictures')
    thumb_img = models.ImageField(default='default_thumb.jpg', upload_to='pictures')
    client = models.CharField(max_length=50)
    category = models.CharField(max_length=100)
    date = models.CharField(max_length=40)

    def __str__(self):
        return self.title
        
class dreamnode_social(models.Model):
    title = models.CharField(max_length=100)
    brief = models.CharField(max_length=100)
    content = models.TextField()
    img_works = models.ImageField(default='default.jpg', upload_to='pictures')
    thumb_img = models.ImageField(default='default_thumb.jpg', upload_to='pictures')
    client = models.CharField(max_length=50)
    category = models.CharField(max_length=100)
    date = models.CharField(max_length=40)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100)
    short_content = models.TextField()
    content = models.TextField(default="There can be no thought of finishing for ‘aiming for the stars.’ Both figuratively and literally, it is a task to occupy the generations. And no matter how much progress one makes, there is always the thrill of just beginning.")
    content_main = models.TextField(default="There can be no thought of finishing for ‘aiming for the stars.’ Both figuratively and literally, it is a task to occupy the generations. And no matter how much progress one makes, there is always the thrill of just beginning.There can be no thought of finishing for ‘aiming for the stars.’ Both figuratively and literally, it is a task to occupy the generations. And no matter how much progress one makes, there is always the thrill of just beginning.")
    heading_1 = models.CharField(max_length=100, default='Heading')
    heading_2 = models.CharField(max_length=100, default='reaching for the stars')
    image_main = models.ImageField(default='default.jpg', upload_to='pictures')
    image_other = models.ImageField(default='default.jpg', upload_to='pictures')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

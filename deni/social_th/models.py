from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    bio = models.TextField()
    image = models.ImageField(upload_to='avatar/')
    website = models.URLField()

    def __str__(self):
        return f'{self.first_name} - {self.last_name} '


class Follow(models.Model):
    follower = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.follower} - {self.following}'


class Post(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post')
    video = models.FileField(upload_to='reel')
    description = models.TextField()
    hashtag = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.created_at} posted'


class PostLike(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return f'{self.user} - {self.post} liked'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField()
    parent = models.ForeignKey('self', related_name='comment', null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} commented {self.post}'


class CommentLike(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    comment = models.TextField()
    like = models.ForeignKey(Comment, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'comment')

    def __str__(self):
        return f'{self.user} liked comment {self.comment}'


class Story(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='story/', null=True, blank=True)
    video = models.FileField(upload_to='story_video/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.created_at} update story'


class Save(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'



class SaveItem(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    save = models.ForeignKey(Save, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.save} - {self.post}'


class Chat(models.Model):
    person = models.ManyToManyField(UserProfile)
    created_date = models.DateField(auto_now_add=True)


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='chat_image/', null=True, blank=True)
    video = models.FileField(upload_to='chat_video/', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

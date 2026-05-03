from django.db import models 

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=128)
    message = models.CharField(max_length=1785)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"

class Project(models.Model):
	project_name = models.CharField(max_length=255)
	project_url = models.CharField(max_length=255)
	project_photo = models.ImageField(upload_to="project_imgs")
	project_description = models.CharField(max_length=178)
	
	def __str__(self):
		return self.project_name

class GithubHistory(models.Model):
	repo_name = models.CharField(max_length=64)
	repo_url = models.CharField(max_length=255)
	commit_url = models.CharField(max_length=255)
	commit_id = models.CharField(max_length=16, unique=True)
	message = models.CharField(max_length=255)
	uploaded_at = models.DateTimeField()
	def __str__(self):
		return self.repo_url
	
class YoutubeHistory(models.Model):
	title = models.CharField(max_length=64)
	video_id = models.CharField(max_length=32, unique=True)
	thumbnail_url = models.CharField(max_length=128)
	uploaded_at = models.DateTimeField()
	def __str__(self):
		return self.title
	
